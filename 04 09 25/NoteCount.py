def NoteC(n):
    NCount = 0

    if n >= 2000:
        count = n // 2000
        print("2000 x", count)
        NCount += count
        n = n % 2000

    if n >= 500:
        count = n // 500
        print("500 x", count)
        NCount += count
        n = n % 500

    if n >= 100:
        count = n // 100
        print("100 x", count)
        NCount += count
        n = n % 100

    if n >= 50:
        count = n // 50
        print("50 x", count)
        NCount += count
        n = n % 50

    if n >= 10:
        count = n // 10
        print("10 x", count)
        NCount += count
        n = n % 10

    if n >= 5:
        count = n // 5
        print("5 x", count)
        NCount += count
        n = n % 5

    if n >= 2:
        count = n // 2
        print("2 x", count)
        NCount += count
        n = n % 2

    if n >= 1:
        count = n // 1
        print("1 x", count)
        NCount += count
        n = n % 1

    return NCount

w = int(input("Enter the amount: "))
total_notes = NoteC(w)
print("Total number of notes:", total_notes)
