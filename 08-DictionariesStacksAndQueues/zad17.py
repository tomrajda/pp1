# 17.	The website http://api.nbp.pl contains data on exchange rates published 
# by the National Bank of Poland. The service provides data in json or xml 
# formats. Display the last ten Euro exchange rates in json format in the 
# browser window. Save the data to the euro.json file. Then write a program 
# that displays the data from the euro.json file in the following format:

# Date            Buying Rate     Selling Rate
# ============================================
# 2019-10-25      3.8150          3.9820
# ...             ...             ...

import json

head = "Date                  Buying Rate       Selling Rate"
print(head)

for _ in range(len(head)):
    print("=", end="")
print()

with open('nbp.json', 'r') as file:
    data = json.load(file)

    for k1, v1 in data.items():
        if k1 == "rates":
            for i in v1:
                for k2, v2 in i.items():
                    if k2 in ["effectiveDate","bid","ask"]:
                        print(f"{v2}            " , end="")
                print()

