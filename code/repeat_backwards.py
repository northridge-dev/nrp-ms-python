items = []
user_input = None

while user_input != "":
    user_input = input("What should I add to the list? ")
    if user_input != "" and user_input not in items:
        items.append(user_input)

print("Here's your list in reverse:")
for item in reversed(items):
    print(item)