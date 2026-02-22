# Repeat Backwards in Python

Remember the "Repeat Backwards" program we wrote in Scratch? Let's rewrite it in Python. Copy the code below (using srccod.northridge.dev) and replace the `TODO` comments with the missing code.

Be sure to test your code. Try duplicating some items to be sure your code doesn't add duplicates to the list.

Once your code is working, answer the questions at the end.

```python
# TODO - create a variable `items` and assign to it an empty list

while True:
    user_input = input("What should I add to the list? ")
    if user_input == "":
        break
    # TODO - add a conditional that tests if the item is alreay in the list
        # TODO - add the new item to the list (runs only if conditional is true)

print("Here's your list in reverse:")
for item in reversed(items):
    print(item)

```

Questions:

1. Which lines of code cause the program to stop asking for additional items?
   <br><br>
2. How would you change the program to print the list in the order it was entered instead of backwards?
