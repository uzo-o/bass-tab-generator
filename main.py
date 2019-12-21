import random

#welcome
print("〜♫ Bass Tab Generator ♫〜")
print()

#string display that will continue to change
strings = ["E","A","D","G"]

print("How To Read the Tab")
print("-----------")
print(strings[0]+"  "+strings[1]+"  "+strings[2]+"  "+strings[3])
print("-- -- -- --")
print("x  |   |  | (1st note played: xth fret on E string)")
print("|  x   |  | (2nd note played: xth fret on A string)")
print("|  |   x  | (3rd note played: xth fret on D string)")
print("|  |   |  | (...)")
print("|  |   |  x (Nth note played: xth fret on G string)")

print("\nTo use the generator, specify the note you would like to add one at a time.\nThe tab will print at the end.\nShall we get started?\n")

mode = input("You are in manual mode. (You will enter your own notes)\n(You can press r to switch to random mode or press any key to continue)\n")

#user lists
userLetters = []
userNumbers = []

if mode == "r":
  #random mode
  print("\nYou are in random mode. (Random notes will be generated. Maybe they'll inspire you?)")
  numNotes = int(input("\nHow many notes will be in this tab? "))
  noteOptions = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","-"]
  for i in range(numNotes):
    chosenString = random.choice(strings)
    chosenNote = random.choice(noteOptions)
    n = 0
    while n < len(strings):
      if strings[n] != chosenString:
        userLetters.append(strings[n])
        userNumbers.append("-")
      else:
        userLetters.append(chosenString)
        userNumbers.append(chosenNote)
      n += 1

  title = input("\nWhat is this song called? ")
  print()
  print("♪ " + title + " Bass Tab ♪")
  print()
  print("-----------")
  print(strings[0]+"  "+strings[1]+"  "+strings[2]+"  "+strings[3])
  print("-- -- -- --")

  while len(userNumbers) != 0:
    i = 0
    print(userNumbers[i]+"  "+userNumbers[i+1]+"  "+userNumbers[i+2]+"  "+userNumbers[i+3])
    userNumbers.remove(userNumbers[i])
    userNumbers.remove(userNumbers[i])
    userNumbers.remove(userNumbers[i])
    userNumbers.remove(userNumbers[i])
else: 
  #manual mode
  editing = "yes"

  while editing != "f":
    #user input
    letterInsert = input("\nInsert a string letter: ").upper()
    while letterInsert not in strings:
      letterInsert = input("Insert a string letter (Must be E, A, D, or G): ").upper()

    numberInsert = str(input("Insert a fret number: "))
    while int(numberInsert) > 20 or int(numberInsert) < 0:
      numberInsert = str(input("Insert a fret number (Must be between 0 and 20): "))

    n = 0
    while n < len(strings):
      if strings[n] != letterInsert:
        userLetters.append(strings[n])
        userNumbers.append("-")
      else:
        userLetters.append(letterInsert)
        userNumbers.append(numberInsert)
      n += 1
    
    editing = input("(Enter f to finalize the tab, b to add a blank row, or press any key to continue)")
    if editing == "b":
      for i in range(len(strings)):
        userLetters.append(strings[i])
        userNumbers.append("-")

  title = input("\nWhat is this song called? ")
  print()
  print("♪ " + title + " Bass Tab ♪")
  print()
  print("-----------")
  print(strings[0]+"  "+strings[1]+"  "+strings[2]+"  "+strings[3])
  print("-- -- -- --")

  while len(userNumbers) != 0:
    i = 0
    print(userNumbers[i]+"  "+userNumbers[i+1]+"  "+userNumbers[i+2]+"  "+userNumbers[i+3])
    userNumbers.remove(userNumbers[i])
    userNumbers.remove(userNumbers[i])
    userNumbers.remove(userNumbers[i])
    userNumbers.remove(userNumbers[i])
