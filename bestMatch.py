# Find the best match from the dictionary for a misspelled token

import Levenshtein as lev
from soundex import *

# Convert the dictionary with soundex. Referred as soundexDict
soundexDict = []
for i in dictLs:
  soundexDict.append(soundex(i))

def bestMatch(token):
  # Convert the token with soundex
  soundexToken = soundex(token)

  # Find the exact same soundex code in the soundexDict, and save their index numbers 
  candidateIndex = []
  for i in range(len(soundexDict)):
    if soundexToken == soundexDict[i]:
      candidateIndex.append(i)
  
  # Use the index numbers of the matches, extract the original words from the original dictionary
  candidateLs = []
  for i in candidateIndex:
    candidateLs.append(dictLs[i])
  
  # Use Levenshtein Distance (edit distance) to compare every potential match to the misspelled token, 
  # and return the most similar one as the best match
  maxRatio = 0
  bestMatch = ""
  for i in candidateLs:
    # The higher the ratio, the more similar the two strings are
    ratio = lev.ratio(token, i)
    if ratio > maxRatio:
      maxRatio = ratio
      bestMatch = i
  return bestMatch
