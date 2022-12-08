# 40.	An array contains integer numbers: [[-38, 19], [5,40],[-7,11],[29,16]]. 
# Create a program that finds the smallest and largest values in the array and 
# in which row and column they are located.

arr = [[-38, 19],[5,40],[-7,11],[29,16]]

def indexes(value, arr):
    """
    
    """
    for i in arr:
        try:

            y = i.index(value)
            return f"X: {arr.index(i)}, Y: {y}"

        except ValueError:
            continue

maximum = max(arr[0])
minimum = min(arr[0])
for i in arr:
    if maximum < max(i):
        maximum = max(i)
    if minimum > min(i):
        minimum = min(i)

print(f"""Maximum value: {maximum}\nLocation: {indexes(maximum, arr)}
    \nMinimum value: {minimum}\nLocation: {indexes(minimum, arr)}
    """)