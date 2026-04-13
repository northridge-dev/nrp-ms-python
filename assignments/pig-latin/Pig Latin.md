# Pig Latin Translator

# Part 1: Tuples

Add this code to `pig_latin.py`. **It is test code. You will delete it after you're finished.**

```python
VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

# Access elements using indexes (just like a list)
print(VOWELS[0])       # First element
print(VOWELS[1])       # Second element
print(VOWELS[-1])      # Last element

# Get the length
print(len(VOWELS))     # How many items?

# Check if something is in the tuple
print('a' in VOWELS)   # Is 'a' a vowel?
print('z' in VOWELS)   # Is 'z' a vowel?
```

Notice that `VOWELS` stores something that _looks_ like a list, but it uses parentheses (`()`) instead of square brackets (`[]`). This is called a **tuple**.

A tuple is like a list, but it can't be changed after you create it. We use a tuple here because the vowels will never change.

## Questions

1. What does `VOWELS[0]` return?
   <br><br>
2. What about `VOWELS[6]`?
   <br><br>
3. What is `len(VOWELS)`?
   <br><br>
4. Write code to check if 'y' is in `VOWELS`. What does it return?
   <br>

**Delete the test code before moving on to the next part!**

<div class="page"/>

# Part 2: String Basics

Pig Latin is about manipulating words. Let's start with some string basics.

Add this code to `pig_latin.py`. **It is test code. You will delete it after you're finished.**

```python
word = "hello"

print(word[0])       # First character
print(word[1])       # Second character
print(word[-1])      # Last character
print(word[1:])      # Everything except the first character
print(word[:-1])     # Everything except the last character
```

## Testing

Run the code and write what each `print` outputs:

```python
mascot = "Knight"
```

- `mascot[0]`:
- `mascot[1]`:
- `mascot[-1]`:
- `mascot[1:3]`:
- `mascot[:-1]`:

## Questions

1. What happens if you try to access `mascot[10]`? Try it and see.
   <br><br><br>
2. What is `"apple"[0]` return?
   <br><br><br>
3. What does `mascot[:]` return?
   <br><br><br>

**Delete the test code before moving on to the next part!**

<div class="page"/>

# Part 3: String Methods

Python has many built-in methods for working with strings.

Add this code to `pig_latin.py`. **It is test code. You will delete it after you're finished.**

```python
testWords = ["hello", "HELLO", "Hello", "123hello", "hello123", "abc"]

for word in testWords:
    print(f"word: {word}")
    print(f"  isalpha(): {word.isalpha()}")  # Are all characters letters?
    print(f"  isupper(): {word.isupper()}")  # Are all letters uppercase?
    print(f"  istitle(): {word.istitle()}")  # Is it Title Case?
    print(f"  lower(): {word.lower()}")     # Convert to lowercase
    print()
```

## Questions

1. What does `isalpha()` return for "hello123"?
   <br><br><br>
2. What does `isalpha()` return for "hello"?
   <br><br><br>
3. What does `"Hello".lower()` return?
   <br><br><br>
4. What does `"hello".upper()` return?
   <br><br><br>
5. What does `"hello".title()` return?
   <br><br><br>

**Delete the test code before moving on to the next part!**

<div class="page"/>

# Part 4: The Split Method

To translate a sentence, we need to break it into individual words.

Add this code to `pig_latin.py`. **It is test code. You will delete it after you're finished.**

```python
message = "hello world how are you"
words = message.split()

print(words)
print(f"Number of words: {len(words)}")

for word in words:
    print(word)
```

## Questions

1. What does `split()` return?
   <br><br><br>
2. What happens if you call `split()` on "one,two,three"?
   <br><br><br>
3. How would you get each word from the phrase "I-am-going-home"?
   <br><br><br>

**Delete the test code before moving on to the next part!**

<div class="page"/>

# Part 5: While Loops to Strip Characters

We need to handle words that have punctuation, like "hello," or "'ello".

Add this code to `pig_latin.py`. **It is test code. You will delete it after you're finished.**

```python
word = ",,!hello"

# Strip non-letters from the START
prefixNonLetters = ''
while len(word) > 0 and not word[0].isalpha():
    prefixNonLetters += word[0]
    word = word[1:]

print(f"prefixNonLetters: '{prefixNonLetters}'")
print(f"word: '{word}'")

# Strip non-letters from the END
suffixNonLetters = ''
while len(word) > 0 and not word[-1].isalpha():
    suffixNonLetters = word[-1] + suffixNonLetters
    word = word[:-1]

print(f"suffixNonLetters: '{suffixNonLetters}'")
print(f"word: '{word}'")
```

## Questions

1. What does `not word[0].isalpha()` check for?
   <br><br><br>
2. Why do we use `word = word[1:]` instead of `word += word[1:]`?
   <br><br><br>
3. What is the difference between `prefixNonLetters += word[0]` and `suffixNonLetters = word[-1] + suffixNonLetters`?
   <br><br><br>

**Delete the test code before moving on to the next part!**

<div class="page"/>

# Part 6: Finding Consonants

In Pig Latin, words that start with a consonant have the consonant cluster moved to the end.

Add this code to `pig_latin.py`. **It is test code. You will delete it after you're finished.**

```python
VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')
word = "school"

# Find and remove consonant prefix
prefixConsonants = ''
while len(word) > 0 and word[0] not in VOWELS:
    prefixConsonants += word[0]
    word = word[1:]

print(f"prefixConsonants: '{prefixConsonants}'")
print(f"word: '{word}'")
```

## Questions

1. What is `prefixConsonants` for the word "string"?
   <br><br><br>
2. What is `word` after the loop for "string"?
   <br><br><br>
3. What happens if the word starts with a vowel (like "apple")?
   <br><br><br>

**Delete the test code before moving on to the next part!**

<div class="page"/>

# Part 7: Building the Translation

Now let's put the Pig Latin rules together.

Add this code to `pig_latin.py`. **It is test code. You will delete it after you're finished.**

```python
VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')
word = "hello"

# Assume already stripped non-letters and lowercase
prefixConsonants = ''
while len(word) > 0 and word[0] not in VOWELS:
    prefixConsonants += word[0]
    word = word[1:]

# Add the pig latin ending
if prefixConsonants != '':
    word = word + prefixConsonants + 'ay'
else:
    word = word + 'yay'

print(f"pig latin: '{word}'")
```

## Questions

Use the code you wrote to test the output for these words:

1. What does the code output for "hello"?
   <br><br><br>
2. What does the code output for "apple"?
   <br><br><br>
3. What does the code output for "strong"?
   <br><br><br>

**Delete the test code before moving on to the next part!**

<div class="page"/>

# Part 8: Building the Complete Translator

Now let's put it all together. Clear out `pig_latin.py` to start fresh and add the following:

## Step 1: Constants

```python
VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')
```

<div class="page"/>

## Step 2: The Translation Function

```python
def englishToPigLatin(word):
    # Separate the non-letters at the start of this word:
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
    if len(word) == 0:
        return prefixNonLetters

    # Separate the non-letters at the end of this word:
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters = word[-1] + suffixNonLetters
        word = word[:-1]

    # Remember if the word was in uppercase or titlecase.
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower()  # Make the word lowercase for translation.

    # Separate the consonants at the start of this word:
    prefixConsonants = ''
    while len(word) > 0 and word[0] not in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

    # Add the pig latin ending to the word:
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'

    # Set the word back to uppercase or titlecase:
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    # Add the non-letters back to the start or end of the word.
    return prefixNonLetters + word + suffixNonLetters
```

<div class="page"/>

## Step 3: The Main Program

```python
def main():
    print("Igpay Atinlay (Pig Latin)")
    print()
    print("Enter your message: ")
    message = input('> ')

    # Split the message into words and translate each one
    output = ''
    for word in message.split():
        output += englishToPigLatin(word) + ' '

    print(output)

main()
```

<div class="page"/>

# Part 9: Experiments

Now that your translator works, try these experiments:

1. **Test different inputs:** Try translating the following. Write down the output.
   - "hello world"
   - "Apple"
   - "SQUARE"
   - "123test"

2. **Handle capitalization:** Let's see how the code handles capitalization. Write down the ouput for each of the following:
   - "Hello"
   - "hello"
   - "HELLO"
   - "HeLLo"

3. **Edge cases:** Try entering just punctuation like "!!!". What happens?
   <br><br><br>

<div class="page"/>

# Part 10: Questions

1. What does the outer `for` loop in the main function do?
   <br><br><br>
2. Why do we need to strip non-letters before checking for consonants?
   <br><br><br>
3. What is the difference between `word += 'ay'` and `word = word + 'ay'`?
   <br><br><br>
4. Explain step-by-step what happens when you translate the word "knights":
   <br><br><br><br><br><br><br>
5. What would happen if we removed the line `word = word.lower()`?
   <br><br><br>

<div class="page"/>

# Part 11: Challenge 1 - Word Counter

Add a feature that counts and displays statistics about the translation:

- How many words were translated
- How many words started with vowels (used "yay")
- How many words started with consonants (used "ay")

For example, if the user enters "hello world apple":

- "hello" → "ellohay" (consonant)
- "world" → "orldway" (consonant)
- "apple" → "appleyay" (vowel)

Your output should say something like:

```
Translated 3 words.
- 1 started with vowels (added "yay")
- 2 started with consonants (added "ay")
```

Hint: You can have the `englishToPigLatin` function return more than one value - the translated word AND whether it started with a vowel. Or you can check if the result ends with "yay" or "ay".

<div class="page"/>

# Part 12: Challenge 2 - Step-by-Step Mode

Add a "verbose" mode that shows each step of the translation for every word:

For example, if the user enters "hello":

```
Translating "hello":
  1. Original word: "hello"
  2. Lowercase: "hello"
  3. Consonant prefix: "h"
  4. Remaining word: "ello"
  5. Add "h" + "ay": "ellohay"
  Result: "ellohay"
```

For "apple":

```
Translating "apple":
  1. Original word: "apple"
  2. Lowercase: "apple"
  3. Consonant prefix: "" (none)
  4. Add "yay": "appleyay"
  Result: "appleyay"
```

Hint: You can create a separate function that calls the same logic but prints messages along the way!

<div class="page"/>

# Part 13: Web Version

You can play a web version of the Pig Latin translator at [https://northridge.dev/pig-latin](https://northridge.dev/pig-latin).

## Questions

Ask how to look at the source code for the web version. Scan through it. It's in a different programming language (JavaScript), but you should be able to follow most of it.

1. Find the function that determines if a character is a letter.
   - What is it called?
     <br><br><br>
   - Write out the logic that determines if a character is a letter.
     <br><br><br>
   - Explain how you think it works.
     <br><br><br><br><br><br>
2. How does the web version detect if a word starts with a vowel?
   <br><br><br>
