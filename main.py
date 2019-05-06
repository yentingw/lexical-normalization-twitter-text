from bestMatch import *

# Read in the txt files and make them into lists
def getToken():
    with open('misspell.txt', 'r') as token:
        tokenLs = [item.strip() for item in token]
        return  tokenLs

tokenLs = getToken()

def getDict():
    with open('dict.txt', 'r') as dictTxt:
        dictLs = [item.strip() for item in dictTxt]
        return  dictLs

dictLs = getDict()

def getAnswer():
    with open('correct.txt', 'r') as ans:
        ansLs = [item.strip() for item in ans]
        return  ansLs

ansLs = getAnswer()

# Convert misspelled tokens and dictionary with soundex, respectively (in bestMatch.py)
# For each token, find the best match within the converted dictionary (also in bestMatch.py).
# Compare the best match to the canonical form in correct.txt
# And use accuracy to evaluate the model
points = 0
for i in range(len(tokenLs)):
  match = bestMatch(tokenLs[i])
  # If best match is the canonical form, get 1 point
  if match == ansLs[i]:
    points += 1

# Calculate the final accuracy       
accuracy = round(points / len(tokenLs), 2)
print("Accuracy: " + str(accuracy))