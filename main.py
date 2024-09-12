
# with open("english_words", "r") as file:
#   english = file.read()

# word = ""
# while len(word) != 5:
#   word = english[random.randint(0,len(english)-1)]
# print(word)
from enum import Enum
import random, time

attempts = 0
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
list = ["_","_","_","_","_"]
wrongletters = []

wordlist = ["daddy"]

word = wordlist[random.randint(0,len(wordlist)-1)]

print("how to play:")
print("------------------------------------------------------")
print("guess the 5 letter word in 6 attemmpts or under")
print("")

time.sleep(1)
print("if a letter in the player's guess is in the word and in the correct place, it will be capitalised ")
print("")

time.sleep(1)
print("if a letter in the player's guess is in the word, but the incorrect place it will be shown in lower case")
print("")

time.sleep(1)
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

  for i in range(len(word)):
    statuscheck[0][i] = word[i]

    statuscheck[2][i] = playerguess[i]


  for i in range(len(playerguess)):
    if playerguess[i] == word[i]:
        statuscheck[1][i] = "1"
        statuscheck[3][i] = "2"

  for i in range(len(playerguess)):
    for j in range(len(word)):
      if playerguess[i] == word[j] and statuscheck[1][j] == "0" and statuscheck[3][i] != "2":
        statuscheck[1][j] = "1"
        statuscheck[3][i] = "1"
        break

  for i in range(len(playerguess)):
    
    if playerguess[i] not in word and playerguess[i] not in wrongletters:
      wrongletters.append(playerguess[i])

  for i in range(len(playerguess)):

    if statuscheck[3][i] == "2":
      list[i] = statuscheck[2][i].upper()
      count += 1

    if statuscheck[3][i] == "1":
      list[i] = statuscheck[2][i]

    if statuscheck[3][i] == "0":
      list[i] = "_"
  
  print("")
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

  if attempts == 6: 
    print("you stink, game over")
    break
    
    