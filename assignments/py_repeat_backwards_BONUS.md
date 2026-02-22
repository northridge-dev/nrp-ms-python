# BONUS: Modified Repeat Backwards in Python

Here's a variation on the "Repeat Backwards" program we just rewrote in Python. Read it through and make a prediction about how it will behave. Then, type it out and run it to see if your prediction was correct.

```python
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
```

Questions:

1. Describe how this program is different from the previous "Repeat Backwards" program.
   <br><br>
2. Describe how you think the program keeps track of how many times each item was entered.
   <br><br>
3. Does the program still need the `items` list? Why or why not?
   <br><br>
