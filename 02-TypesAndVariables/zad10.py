msg = """**Sum of the two input numbers**"""
print(msg)

sum = 0
for _ in range(2):
    num = int(input("Type number: "))
    sum += num

print(f"Result: {sum}")
