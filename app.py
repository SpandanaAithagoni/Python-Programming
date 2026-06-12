
import streamlit as st

st.set_page_config(
    page_title="Python Mini Projects Dashboard",
    page_icon="🐍",
    layout="wide"
)

st.title("🐍 Python Mini Projects Dashboard")

menu = st.sidebar.selectbox(
    "Choose Program",
    [
        "Hello World",
        "Alphabet Checker",
        "Even or Odd",
        "Positive or Negative",
        "Vowel or Consonant",
        "Leap Year",
        "Divisible by 5 and 11",
        "Greatest of Three Numbers",
        "Swap Numbers",
        "Student Details",
        "Simple Interest",
        "Current Bill",
        "Area and Perimeter",
        "Volume Calculator",
        "KM to Miles",
        "Days to Years and Months",
        "Addition Function",
        "Subtraction Function",
        "Arithmetic Operations"
    ]
)

if menu == "Hello World":
    st.header("Hello World")
    if st.button("Show"):
        st.success("Hello World")

elif menu == "Alphabet Checker":
    st.header("Alphabet Checker")
    text = st.text_input("Enter a character")
    if st.button("Check Alphabet"):
        if text.isalpha():
            st.success("It is an alphabet")
        else:
            st.error("It is not an alphabet")

elif menu == "Even or Odd":
    st.header("Even or Odd")
    num = st.number_input("Enter Number", step=1)
    if st.button("Check"):
        if num % 2 == 0:
            st.success("Even Number")
        else:
            st.warning("Odd Number")

elif menu == "Positive or Negative":
    st.header("Positive or Negative")
    num = st.number_input("Enter Number")
    if st.button("Find"):
        if num >= 0:
            st.success("Positive Number")
        else:
            st.error("Negative Number")

elif menu == "Vowel or Consonant":
    st.header("Vowel or Consonant")
    char = st.text_input("Enter Character")
    if st.button("Check Character"):
        if char.lower() in ['a', 'e', 'i', 'o', 'u']:
            st.success("Vowel")
        else:
            st.warning("Consonant")

elif menu == "Leap Year":
    st.header("Leap Year Checker")
    year = st.number_input("Enter Year", step=1)
    if st.button("Check Leap Year"):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            st.success("Leap Year")
        else:
            st.error("Not a Leap Year")

elif menu == "Divisible by 5 and 11":
    st.header("Divisibility Check")
    num = st.number_input("Enter Number", step=1)
    if st.button("Check Divisibility"):
        if num % 5 == 0 and num % 11 == 0:
            st.success("Divisible by both 5 and 11")
        else:
            st.error("Not Divisible by both 5 and 11")

elif menu == "Greatest of Three Numbers":
    st.header("Greatest of Three Numbers")
    a = st.number_input("Number 1")
    b = st.number_input("Number 2")
    c = st.number_input("Number 3")

    if st.button("Find Greatest"):
        st.success(f"Greatest Number = {max(a,b,c)}")

elif menu == "Swap Numbers":
    st.header("Swap Numbers")

    a = st.number_input("A")
    b = st.number_input("B")

    if st.button("Swap"):
        st.write("Before Swapping")
        st.write(f"A = {a}, B = {b}")

        a, b = b, a

        st.write("After Swapping")
        st.write(f"A = {a}, B = {b}")

elif menu == "Student Details":
    st.header("Student Details")

    roll = st.number_input("Roll Number", step=1)
    name = st.text_input("Student Name")

    s1 = st.number_input("Subject 1")
    s2 = st.number_input("Subject 2")
    s3 = st.number_input("Subject 3")

    if st.button("Calculate Result"):
        total = s1 + s2 + s3
        avg = total / 3

        st.write("Name:", name)
        st.write("Roll Number:", roll)
        st.write("Total:", total)
        st.write("Average:", round(avg, 2))

elif menu == "Simple Interest":
    st.header("Simple Interest Calculator")

    p = st.number_input("Principal Amount")
    t = st.number_input("Time")
    r = st.number_input("Rate")

    if st.button("Calculate SI"):
        si = (p * t * r) / 100
        total = p + si

        st.success(f"Simple Interest = {si}")
        st.success(f"Total Amount = {total}")

elif menu == "Current Bill":
    st.header("Electricity Bill")

    cno = st.number_input("Consumer Number", step=1)
    cname = st.text_input("Consumer Name")
    pmr = st.number_input("Present Month Reading")
    lmr = st.number_input("Last Month Reading")

    if st.button("Generate Bill"):
        units = pmr - lmr
        bill = units * 3.80

        st.write("Consumer Number:", cno)
        st.write("Consumer Name:", cname)
        st.write("Units Consumed:", units)
        st.write("Current Bill:", bill)

elif menu == "Area and Perimeter":
    st.header("Area and Perimeter")

    r = st.number_input("Circle Radius")
    l = st.number_input("Rectangle Length")
    b = st.number_input("Rectangle Breadth")

    if st.button("Calculate"):
        pi = 3.14

        area_c = pi * r * r
        per_c = 2 * pi * r

        area_r = l * b
        per_r = 2 * (l + b)

        st.write("Rectangle Area:", area_r)
        st.write("Rectangle Perimeter:", per_r)

        st.write("Circle Area:", round(area_c, 2))
        st.write("Circle Perimeter:", round(per_c, 2))

elif menu == "Volume Calculator":
    st.header("Volume Calculator")

    s = st.number_input("Cube Side")
    r = st.number_input("Cylinder Radius")
    h = st.number_input("Cylinder Height")

    if st.button("Calculate Volume"):
        cube = s ** 3
        cylinder = 3.14 * r * r * h

        st.write("Cube Volume:", cube)
        st.write("Cylinder Volume:", round(cylinder, 2))

elif menu == "KM to Miles":
    st.header("KM to Miles")

    km = st.number_input("Kilometers")

    if st.button("Convert"):
        miles = km / 0.621
        st.success(f"Miles = {round(miles,2)}")

elif menu == "Days to Years and Months":
    st.header("Days Converter")

    days = st.number_input("Enter Days")

    if st.button("Convert Days"):
        years = days / 365
        months = days / 30

        st.write("Years:", round(years, 2))
        st.write("Months:", round(months, 2))

elif menu == "Addition Function":
    st.header("Addition Function")

    if st.button("Add 10 + 20"):
        st.success(10 + 20)

elif menu == "Subtraction Function":
    st.header("Subtraction Function")

    a = st.number_input("A")
    b = st.number_input("B")

    if st.button("Subtract"):
        st.success(a - b)

elif menu == "Arithmetic Operations":
    st.header("Arithmetic Operations")

    x = st.number_input("First Number", value=5)
    y = st.number_input("Second Number", value=2)

    if st.button("Calculate Operations"):
        st.write("Addition:", x + y)
        st.write("Subtraction:", x - y)
        st.write("Multiplication:", x * y)
        st.write("Division:", x / y if y != 0 else "Undefined")
        st.write("Power:", x ** y)
```
