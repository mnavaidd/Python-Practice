


filename = "navaid.txt"
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line)

print("Hurrah, I can read.")


