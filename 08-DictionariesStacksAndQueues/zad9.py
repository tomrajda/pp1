# 9.	Create a dictionary describing a mobile phone. Use at least 6 key-value 
# pairs of data. Use different value types. Then, using 'for' loop, display the
# contents of the dictionary. To read a key and value, use the items() method.

phone = {
    "camera": True,
    "resolution": 1000,
    "RAM memory": "2 GB",
    "Android": 4.3,
    "Screen size": 7,
    "Brand": "Samsung"
}

for key, value in phone.items():
    print(f"{key}: {value}")