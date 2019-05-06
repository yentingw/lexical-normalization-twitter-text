# Project 1: very tweetz. such non-canonickal. amayze

> Aim

For each misspelled token in misspell.txt, filter out its best match(es) in dict.txt,
and then compare the best match(es) to the canonical form in correct.txt.

> Methods

Step 1: Convert all words in dict.txt with soundex(), which I acquired from:
https://medium.com/@yash_agarwal2/soundex-and-levenshtein-distance-in-python-8b4b56542e9e
Please refer to soundex.py, and line 6 - 9 in bestMatch.py

Step 2: Convert each misspelled token with soundex(), and find the exact same soundex code in the converted dictionary.
Insert every match into a candidate list. Please refer to line 11 - 24 in bestMatch.py

Step 3: Among the candidate list, use Levenshtein Distance (commonly known as edit distance)
to find the best match to the misspelled token. Please refer to line 27 - 35 in bestMatch.py
The Leveshitein module is acquired from https://pypi.org/project/python-Levenshtein/

Step 4: Compare the best match to the canonical form, and calculate the accuracy. Please refer from line 30 in main.py.

> Result

For each best match, it is either a hit (gain 1 point) or not when comparing to the canonical form.
Divide the total points by the number of tokens to generate accuracy.

The accuracy of my model is 76%.