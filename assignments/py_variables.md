# Python Variables

Each exercise presents a sequence of Python commands. Think carefully about each, predict what will be printed, and answer any questions.

You can later check your predictions with a Python REPL at https://pyodide.org/en/stable/console-v2.html

## 1. Basics

Variables hold values, and we can use them in place of those values.

```python
name = "Bregman"
age = 31
print(name)
print(age + 5)
```

What will be printed?

<br>
<br>

What will the value of `age` be after all the commands have been executed?

<br>
<br>

## 2. Reassignment

Re-assigning a variable overwrites the old value. Python doesn't "remember" the previous value once it's gone.

```python
score = 100
score = 150
score = 50
print(score)
```

What will be printed?

<div class="page"/>

## 3. Accessing Uninitialized Variables

Until you create a variable by assigning it a value, it does not exist.

```python
print(room)
room = 204
print(room)
```

What will be printed?

<br>
<br>

## 4. Relative Updates

Variables can appear on both sides of the equals sign (the **assignment operator**). Python evalutes the right side _first_, then updates the value of the variable on the left.

```python
count = 10
count = count + 5
count = count * 2
print(count)
```

What will be printed?

<br>
<br>

What would be printed if you swapped the order of the second and third commands?

<div class="page"/>

## 5. Multiple Variables

Each variable keeps track of its own value.

```python
apples = 5
bananas = 12
total_fruits = apples + bananas
apples = 10
print(total_fruit)
```

What will be printed?

<br>
<br>

## 6. Linked Variables?

Does assigning one variable to another _link_ them?

```python
f = 100
g = f
f = 42
print(g)
```

What will be printed?

<br>
<br>

Does `g = f` **link** `g` and `f`? What evidence supports your answer?

<div class="page"/>

## 7. Chain Link?

Here's an example of "chained assignment". Can multiple variables point to the exact same value at the same time?

```python
j = k = 2
j = j + 1
print(j)
print(k)
```

What will be printed?

<br>
<br>

Explain why.

<br>
<br>

## 8. "Seat Swap" (aka Tuple Unpacking)

Here's an example of "parallel assignment". This is a very "Pythonic" way to assign multiple values to multiple variables.

```python
p, q = "pint", "quart"
p, q = q, p
print(p)
```

What will be printed?

<br>
<br>

Explain why.
