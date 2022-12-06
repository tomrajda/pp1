# 9.	An array contains a list of Polish names: Genowefa, Onufry, Celestyna, 
# Alojzy, Pankracy. Create a program that displays the longest name 
# (consisting of the largest number of characters).

names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

lengths = []
for name in names:
    lengths.append(len(name))

print(f"Names:", end=" ")
for i in names:
    print(i, end=" ")
print()
print(f"Longest name: {names[lengths.index(max(lengths))]}")