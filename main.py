
# with open("english_words", "r") as file:
#   english = file.read()

# word = ""
# while len(word) != 5:
#   word = english[random.randint(0,len(english)-1)]
# print(word)

import random, time, urllib.request,json





attempts = 0
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
list = ["_","_","_","_","_"]
wrongletters = []

#read an api containing a five letter word and assign it to wordpull
with urllib.request.urlopen('https://random-word-api.herokuapp.com/word?length=5') as response:
   wordpull = response.read()

#parse word from json file to make readable
word = json.loads(wordpull)[0]

print("how to play:")
print("------------------------------------------------------")
print("guess the 5 letter word in 6 attempts or under")
print("")

time.sleep(2)
print("if a letter in the player's guess is in the word and in the correct place, it will be capitalised ")
print("")

time.sleep(2)
print("if a letter in the player's guess is in the word, but the incorrect place it will be shown in lower case")
print("")

time.sleep(2)
print("if a letter in the player's guess is not in the word, it will be placed aside")
print("------------------------------------------------------")
print("")



#start of game

while attempts != 6:

#player input and validation

  while True:

    playerguess = input("guess the word (5 letters): ")
    playerguess = playerguess.lower()
    print("")
    
    valid = True

#backdoor to find word while testing
    if playerguess == "joshua":
      print(word)
      continue



#length check

    if len(playerguess) != 5:
      valid = False
    
#type check

    for i in playerguess:
      if i not in alphabet:
        valid = False
      
    if valid == False:
      print("invalid input, try again")
      print("")

    else:
      break
  
  count = 0
  statuscheck = [["","","","",""], #word goes here
                ["0","0","0","0","0"], #whether each letter of word has been used, 0 for no, 1 for yes
                ["","","","",""], #playerguess goes here
                ["0","0","0","0","0"]] #type of correlation between playerguess and words letter, 0 = not in the word, 1 = in the word but in wrong place, 2 in the word and in the right place


# assign word to line 0 of array and guess to line 2
  for i in range(len(word)):
    statuscheck[0][i] = word[i]

    statuscheck[2][i] = playerguess[i]


# initial check for each letter of the guess, for if the guess directly matches the letter in that spot
  for i in range(len(playerguess)):
    if playerguess[i] == word[i]:
        statuscheck[1][i] = "1"
        statuscheck[3][i] = "2"

# for each currently unused letter of the guess, check every letter in the word for if it matches and has not been used yet
  for i in range(len(playerguess)):
    for j in range(len(word)):
      if playerguess[i] == word[j] and statuscheck[1][j] == "0" and statuscheck[3][i] != "2":
        statuscheck[1][j] = "1"
        statuscheck[3][i] = "1"
        break

# any letters in the guess that aren't in the word added to list
  for i in range(len(playerguess)):
    
    if playerguess[i] not in word and playerguess[i] not in wrongletters:
      wrongletters.append(playerguess[i])

#construct an output using the letters and their assignments
  for i in range(len(playerguess)):

    if statuscheck[3][i] == "2":
      list[i] = statuscheck[2][i].upper()
      count += 1

    if statuscheck[3][i] == "1":
      list[i] = statuscheck[2][i]

    if statuscheck[3][i] == "0":
      list[i] = "_"
  
  
  if len(wrongletters) == 0:
      print(list, "currently known wrong letters: none")


  else:
    print(list, "currently known wrong letters:", wrongletters)

  if count == len(word):
    correct = True
    print("you guessed the correct word")
    break
  
  else:
    print("try again")
    attempts += 1
    print("number of guesses:" , attempts)
    print("")

  if attempts == 6: 
    print("you stink, game over")
    print("the word was:" , word)
    break
    
    