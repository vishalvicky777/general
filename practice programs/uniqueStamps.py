import sys
num = input("Enter number of stamps: ")
print(num)
items = []
items2 = []

for i in range(0, int(num)):
    stamp_country = input("Enter Stamp Country: " )
    items.append(stamp_country)

for item in items:
    if item in items2:
        print("found")
        continue
    else:
        items2.append(item)
        continue

print(len(items2))