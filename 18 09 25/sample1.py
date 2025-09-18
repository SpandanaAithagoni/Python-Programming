import os
import sys
from supabase import create_client, Client
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
sb: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# ---------- CREATE ----------
def add_member(name: str, email: str):
    return sb.table("members").insert({"name": name, "email": email}).execute().data

def add_book(title: str, author: str, category: str, stock: int):
    return sb.table("books").insert({
        "title": title, "author": author, "category": category, "stock": stock
    }).execute().data

# ---------- READ ----------
def list_books_with_availability():
    books = sb.table("books").select("*").execute().data or []
    borrows = sb.table("borrow_records").select("*").execute().data or []
    active_count = {}
    for b in borrows:
        if b.get("return_date") is None:
            active_count[b["book_id"]] = active_count.get(b["book_id"], 0) + 1
    result = []
    for book in books:
        borrowed = active_count.get(book["book_id"], 0)
        available = max(book["stock"] - borrowed, 0)
        result.append({**book, "borrowed": borrowed, "available": available})
    return result

def search_books(keyword: str):
    expr = f"title.ilike.%{keyword}%,author.ilike.%{keyword}%,category.ilike.%{keyword}%"
    return sb.table("books").select("*").or_(expr).execute().data

def get_member_with_borrowed(member_id: int):
    member = sb.table("members").select("*").eq("member_id", member_id).execute().data
    if not member:
        return None
    records = sb.table("borrow_records").select("*").eq("member_id", member_id).execute().data
    books = {b["book_id"]: b for b in (sb.table("books").select("*").execute().data or [])}
    for r in records:
        r["book_title"] = books.get(r["book_id"], {}).get("title")
    return {"member": member[0], "borrow_records": records}

# ---------- UPDATE ----------
def update_book_stock(book_id: int, new_stock: int):
    return sb.table("books").update({"stock": new_stock}).eq("book_id", book_id).execute().data

def update_member_email(member_id: int, new_email: str):
    return sb.table("members").update({"email": new_email}).eq("member_id", member_id).execute().data

# ---------- DELETE ----------
def delete_member(member_id: int):
    active = [b for b in (sb.table("borrow_records").select("*").eq("member_id", member_id).execute().data or []) if b["return_date"] is None]
    if active:
        return {"error": "Member has active borrowed books, cannot delete."}
    return sb.table("members").delete().eq("member_id", member_id).execute().data

def delete_book(book_id: int):
    active = [b for b in (sb.table("borrow_records").select("*").eq("book_id", book_id).execute().data or []) if b["return_date"] is None]
    if active:
        return {"error": "Book is currently borrowed, cannot delete."}
    return sb.table("books").delete().eq("book_id", book_id).execute().data

# ---------- BORROW / RETURN ----------
def borrow_book(member_id: int, book_id: int):
    book = sb.table("books").select("*").eq("book_id", book_id).execute().data
    if not book:
        return {"error": "Book not found"}
    book = book[0]
    active = [b for b in (sb.table("borrow_records").select("*").eq("book_id", book_id).execute().data or []) if b["return_date"] is None]
    if len(active) >= book["stock"]:
        return {"error": "No copies available"}
    return sb.table("borrow_records").insert({"member_id": member_id, "book_id": book_id}).execute().data

def return_book(record_id: int):
    return sb.table("borrow_records").update({"return_date": datetime.utcnow().isoformat()}).eq("record_id", record_id).execute().data

# ---------- REPORTS ----------
def report_overdue(days: int = 14):
    brs = sb.table("borrow_records").select("*").execute().data or []
    cutoff = datetime.utcnow() - timedelta(days=days)
    overdue = []
    for r in brs:
        if r["return_date"] is None:
            try:
                bd = datetime.fromisoformat(r["borrow_date"].replace("Z", "+00:00"))
                if bd < cutoff:
                    overdue.append(r)
            except Exception:
                pass
    return overdue

def report_most_borrowed(top_n: int = 5):
    brs = sb.table("borrow_records").select("*").execute().data or []
    counts = {}
    for r in brs:
        counts[r["book_id"]] = counts.get(r["book_id"], 0) + 1
    sorted_books = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:top_n]
    books = {b["book_id"]: b for b in (sb.table("books").select("*").execute().data or [])}
    return [{"book_id": bid, "title": books.get(bid, {}).get("title"), "borrow_count": cnt} for bid, cnt in sorted_books]

def report_currently_borrowed():
    brs = sb.table("borrow_records").select("*").execute().data or []
    members = {m["member_id"]: m for m in (sb.table("members").select("*").execute().data or [])}
    books = {b["book_id"]: b for b in (sb.table("books").select("*").execute().data or [])}
    return [{
        "record_id": r["record_id"],
        "member_name": members.get(r["member_id"], {}).get("name"),
        "book_title": books.get(r["book_id"], {}).get("title"),
        "borrow_date": r["borrow_date"]
    } for r in brs if r["return_date"] is None]

# ---------- CLI MENU ----------
def menu():
    while True:
        print("\n=== Online Library Management ===")
        print("1. Register Member")
        print("2. Add Book")
        print("3. List Books")
        print("4. Search Books")
        print("5. Show Member Details")
        print("6. Update Book Stock")
        print("7. Update Member Email")
        print("8. Delete Member")
        print("9. Delete Book")
        print("10. Borrow Book")
        print("11. Return Book")
        print("12. Report: Overdue")
        print("13. Report: Most Borrowed")
        print("14. Report: Currently Borrowed")
        print("0. Exit")

        choice = input("Choice: ").strip()
        if choice == "1":
            print(add_member(input("Name: "), input("Email: ")))
        elif choice == "2":
            print(add_book(input("Title: "), input("Author: "), input("Category: "), int(input("Stock: "))))
        elif choice == "3":
            for b in list_books_with_availability(): print(b)
        elif choice == "4":
            for r in search_books(input("Keyword: ")): print(r)
        elif choice == "5":
            print(get_member_with_borrowed(int(input("Member ID: "))))
        elif choice == "6":
            print(update_book_stock(int(input("Book ID: ")), int(input("New stock: "))))
        elif choice == "7":
            print(update_member_email(int(input("Member ID: ")), input("New Email: ")))
        elif choice == "8":
            print(delete_member(int(input("Member ID: "))))
        elif choice == "9":
            print(delete_book(int(input("Book ID: "))))
        elif choice == "10":
            print(borrow_book(int(input("Member ID: ")), int(input("Book ID: "))))
        elif choice == "11":
            print(return_book(int(input("Record ID: "))))
        elif choice == "12":
            for r in report_overdue(int(input("Days (default 14): ") or 14)): print(r)
        elif choice == "13":
            for r in report_most_borrowed(int(input("Top N (default 5): ") or 5)): print(r)
        elif choice == "14":
            for r in report_currently_borrowed(): print(r)
        elif choice == "0":
            sys.exit(0)
        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()
