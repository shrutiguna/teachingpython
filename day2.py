# 1. functions
# 2. Files
# 3.dictionary
# 4.json
# 5. git


file= open("shoppingList.txt","r")
content= file.read()
file.close()

items=content.split("\n")
items.sort()

for item in items:
    print("-"+item)