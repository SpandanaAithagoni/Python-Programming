def clean(set1):
    return set(email.lower() for email in set1)

def unique(d1, d2, d3):
    return d1 | d2 | d3

def threedays(d1, d2, d3):
    return d1 & d2 & d3

def exactlyOneday(d1, d2, d3):
    ed1 = d1 - (d2 | d3)
    ed2 = d2 - (d1 | d3)
    ed3 = d3 - (d1 | d2)
    return ed1 | ed2 | ed3

def overlap(d1, d2, d3):
    pd12 = d1 & d2
    pd23 = d2 & d3
    pd31 = d1 & d3
    return pd12, pd23, pd31

day1 = {"Amaira@g.com", "NAIRA@g.com", "naithik@g.com", "amaira@g.com"}
day2 = {"naira@g.com", "naksh@g.com", "KAIRA@g.com", "anvika@g.com"}
day3 = {"Esha@g.com", "naira@g.com", "Kaira@g.com", "hrithi@g.com"}

d1 = clean(day1)
d2 = clean(day2)
d3 = clean(day3)

all_unique = unique(d1, d2, d3)
three_days = threedays(d1, d2, d3)
one_day = exactlyOneday(d1, d2, d3)
pd12, pd23, pd31 = overlap(d1, d2, d3)

print("No. of unique attendees:", len(all_unique))
print("Unique attendees:", sorted(all_unique))
print("No. of attendees for all 3 days:", len(three_days))
print("3 days attendees:", sorted(three_days))
print("No. of attendees for only 1 day:", len(one_day))
print("1 day attendees:", sorted(one_day))
print("Day1 and Day2:", len(pd12))
print(sorted(pd12))
print("Day2 and Day3:", len(pd23))
print(sorted(pd23))
print("Day1 and Day3:", len(pd31))
print(sorted(pd31))