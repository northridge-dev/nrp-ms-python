item_count = {} 
items = []

while True:
    user_input = input("What should I add to the list? ")
    if user_input == "":
        break
    item_count[user_input] = item_count.get(user_input, 0) + 1
    if user_input not in items:
        items.append(user_input)
    
print("Here's your list in reverse:")
for item in reversed(items):
    print(f"{item_count[item]} x {item}")
