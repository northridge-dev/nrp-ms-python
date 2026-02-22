# Python Lists

## Instructions

1. Read each code snippet
2. Predict what it will output --> write your prediction
3. Type out the code and run it --> write the actual output
4. If your prediction was wrong, try to figure out why

Once you're finished, answer the questions at the end.

## Snippet 1

```python
teams = ["cubs", "brewers", "reds"]
print(teams)
```

_Prediction_
<br><br>
_Actual_
<br><br>

## Snippet 2

```python
teams = ["cubs", "brewers", "reds"]
print(teams[1])
```

_Prediction_
<br><br>
_Actual_
<br><br>

## Snippet 3

```python
teams = ["cubs", "brewers", "reds"]
print(teams[2])
```

_Prediction_
<br><br>

_Actual_

<div class="page"/>

## Snippet 4

```python
teams = ["cubs", "brewers", "reds"]
print(teams[0])
```

_Prediction_
<br><br>
_Actual_
<br><br>

## Snippet 5

```python
teams = ["cubs", "brewers", "reds"]
print(teams[3])
```

_Prediction_
<br><br>
_Actual_
<br><br>

## Snippet 6

```python
teams = ["cubs", "brewers", "reds"]
print(teams[-1])
```

_Prediction_
<br>
_Actual_
<br>

## Snippet 7

```python
teams = ["cubs", "brewers", "reds"]
print(teams[-1])
```

_Prediction_
<br>
_Actual_
<br>

<div class="page"/>

## Snippet 8

```python
teams = ["cubs", "brewers", "reds"]
print(teams)
print(len(teams))
teams.append("cardinals")
print(len(teams))
```

_Prediction_
<br><br>
_Actual_
<br><br>

## Snippet 9

```python
teams = ["cubs", "brewers", "reds"]
teams.append("cardinals")
print(teams[0])
print(teams[-1])
```

_Prediction_
<br><br>
_Actual_
<br><br>

## Snippet 10

```python
teams = ["cubs", "brewers", "reds", "cardinals"]
teams.insert(0, "pirates")
print(teams)
print(len(teams))
print(teams[0])
print(teams[-1])
```

_Prediction_
<br><br>
_Actual_
<br><br>

## Snippet 11

```python
teams = ["cubs", "brewers", "reds", "cardinals"]
teams.insert(2, "pirates")
print(teams[1])
print(teams[2])
print(teams[3])
```

_Prediction_
<br><br>
_Actual_
<br><br>

## Questions

1. Show how to create a list of numbers and assign it to a variable called `numbers`.
   <br>
2. The number inside of brackets following a variable that holds a list is called an **index**, for example, `teams[1]`. What do indexes do when the number inside the bracket is:
   - the number is positive?
   - the number is zero?
   - the number is negative?
     <br>
3. What does the `len` function do when you pass it a list?
   <br>
4. What happens if you try to use an index that is greater than or equal to the length of the list?
   <br>
5. What does the `append` method do when you call it on a list?
   <br>
6. The `insert` method takes two arguments, a number and a value. What does it do when you call it on a list?
