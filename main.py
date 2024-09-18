
#import about 50 different libraries with extremely similar names, each for seperate cases
from urllib.error import HTTPError
from urllib.request import urlopen, Request
import random, time, urllib.request,json


#function checks if a word is real
def isrealword(guess: str) -> bool:

#link goes to an api that returns an error if the word is not found in it's dictionary, inputed word concatenated onto link
   link = 'https://api.dictionaryapi.dev/api/v2/entries/en/'
   url = link + guess

#attempts to check if the link has a valid output, if it doesn't, gives the error (as an HTTP error ) to the variable err and checks if it is the "not found" error specifically (404), otherwise aborts the program
#pretends to be a webbrowser making the request because the api was being picky
   try:
      with urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'})) as response:
         return response.status == 200
   except HTTPError as err:
      if err.code == 404:
         return False
      else:
         print("something's gone horribly wrong")
         raise
      
#loops through input, making sure each letter is in the alphabet and not a special character
def charactercheck(playerguess: str) -> bool:
  for i in playerguess:
        if i not in alphabet:
          return False
        
  return True

attempts = 0
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
list = ["_","_","_","_","_"]
wrongletters = []

#read an api containing a random five letter word and assign it to wordpull
with urllib.request.urlopen('https://random-word-api.herokuapp.com/word?length=5') as response:
   wordpull = response.read()

#parse word from json file to make readable
word = json.loads(wordpull)[0]


print("how to play:")
print("------------------------------------------------------")
print("guess the 5 letter word in 6 attempts or under")
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
    

#backdoor to veiw the real word while testing
    if playerguess == "joshua":
      print(word)
      print("")
      continue

#length check

    if len(playerguess) != 5:
      print("not 5 letters")
      print("")
      continue
    
#type check

    if not charactercheck(playerguess):
      print("invalid characters")
      print("")
      continue

#calling the real word checking function, after making sure the palyer's guess is not correct, as there was some missalignment between the dictionaries of the word generator and checker, leading to the correct answers being labelled as invalid words
    if playerguess != word:
      if not isrealword(playerguess) :
        print("please enter a real word")

        # 1 second wait to prevent spam requests to the api, leading to getting blocked
        time.sleep(1)
        print("")
        continue
    
    time.sleep(1)
    print("")
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

#puts a capital letter in that spot if it was the correct letter
    if statuscheck[3][i] == "2":
      list[i] = statuscheck[2][i].upper()
      count += 1

#puts a lowercase if the letter was in the word but not the right spot
    if statuscheck[3][i] == "1":
      list[i] = statuscheck[2][i]

#puts an underscore if the letter was not in the word
    if statuscheck[3][i] == "0":
      list[i] = "_"
  
#prints the constructed output with a "none" if the list of known wrong letters has not been added to yet
  if len(wrongletters) == 0:
      print(list, "currently known wrong letters: none")

#prints the constructed output with the list of known wrong letters
  else:
    print(list, "currently known wrong letters:", wrongletters)

  print("")

#if the number of correct letters is 5, it means they got the word right and won
  if count == len(word):
    print("you guessed the correct word")
    break
  
  else:
    print("try again")
    attempts += 1
    print("number of guesses left:" , (6 - attempts))
    print("")

  if attempts == 6: 
    print("you stink, game over")
    print("the word was:" , word)
    break