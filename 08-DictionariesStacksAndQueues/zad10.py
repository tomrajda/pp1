# 10.	Create an array with 5 dictionaries, each containing a country and its 
# population. Then, using ‘while’ loop, display the array contents.

countries = [
    {
       "Afghanistan": 34161000
    },
    {
       "Denmark": 5893000
    },
    {
       "Kazakhstan": 19261000
    },
    {
       "Nigeria": 217376000
    },
    {
       "Vatican City": 800
    }
]

i = 0

while i <= (len(countries) - 1):
    for k, v in countries[i].items():
        print(f"{k}: {v}")
    i += 1