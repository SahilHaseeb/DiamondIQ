
# Beginner Level (Questions 1 to 10)

# Q1. Length of a String

s = "hello world"
print("Q1 Length:", len(s))

# Q2. Uppercase & Lowercase

s = "Python3"
print("Q2 Uppercase:", s.upper())
print("Q2 Lowercase:", s.lower())

# Q3. Count a Character

s = "banana"
ch = "a"
print("Q3 Count:", s.count(ch))

# Q4. First & Last Character

s = "drawer"
if not s:
    print("Q4 Empty input")
else:
    print("Q4 First:", s[0], "Last:", s[-1])

# Q5. Check Substring Presence

s = "data science"
sub = "science"
print("Q5 Present:", sub in s)

# Q6. Slice a String

s = "programming"
start = 3
end = 8
print("Q6 Slice:", s[start:end])

# Q7. Reverse a String
s = "Python"
print("Q7 Reversed:", s[::-1])

# Q8. Replace Substring
s = "I love apples. Apples are great!"
print("Q8 Replaced:", s.replace("apples", "oranges"))

# Q9. Split and Join
s = "split this sentence"
words = s.split()
print("Q9 Joined:", "-".join(words))

# Q10. Strip Whitespace
s = "   padded text  "
print("Q10 Stripped:", s.strip())


# Q11. Count Vowels & Consonants

s = "Hello, World! 123"
vowels = 0
consonants = 0
for ch in s:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
print("Q11 Vowels:", vowels, "Consonants:", consonants)

# Q12. Palindrome Check (ignore case and non-alphanumerics)
s = "A man, a plan, a canal: Panama!"
clean = ""
for ch in s:
    if ch.isalnum():
        clean += ch.lower()
print("Q12 Palindrome:", clean == clean[::-1])


# Q14. Find All Indices of a Substring (overlaps allowed)
s = "aaaa"
sub = "aa"
indices = []
for i in range(len(s) - len(sub) + 1):
    if s[i:i + len(sub)] == sub:
        indices.append(i)
print("Q14 Indices:", indices)

# Q15. Character Frequency Dictionary
s = "Baa Baa Black Sheep"
freq = {}
for ch in s.lower():
    if ch != " ":
        freq[ch] = freq.get(ch, 0) + 1
print("Q15 Frequency:", freq)

# Q16. Anagram Checker
s1 = "Listen"
s2 = "Silent"
letters1 = ""
for ch in s1:
    if ch.isalpha():
        letters1 += ch.lower()
letters2 = ""
for ch in s2:
    if ch.isalpha():
        letters2 += ch.lower()
print("Q16 Anagram:", sorted(letters1) == sorted(letters2))


# Q18. Longest Word in a Sentence
sentence = "Find the longest_word here!"
words = []
current = ""
for ch in sentence:
    if ch.isalpha():
        current += ch
    else:
        if current != "":
            words.append(current)
        current = ""
if current != "":
    words.append(current)

longest = ""
for w in words:
    if len(w) > len(longest):
        longest = w
print("Q18 Longest word:", longest)

# Q19. Remove Duplicate Characters but Keep Order
s = "banana"
result = ""
for ch in s:
    if ch not in result:
        result += ch
print("Q19 Unique:", result)
