names = set()

while True:
    s = input()
    if s.strip() == "":
        break
    name = s.strip()

    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)

for n in names:
    print(n)
