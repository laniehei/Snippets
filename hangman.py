import turtle
import random


def hangman():
## This function plays the game of hangman ##
  words = ('abate', 'chicanery', 'disseminate', 'latent', 'distill', 'gainsay', 'coagulate','dissolution',
  'garrulous','laud','abeyance', 'coda', 'dissonance','goad','lethargic', 'abscond', 'cogent', 'distend',
  'gouge','levee','abstemious','commensurate') #sets the words for the game
  index = random.randint(0,len(words)-1) #chooses a random word from the list
  word = words[index] #picks word (this is a string)


  turtle.setworldcoordinates(0,0,100,100) #sets the coordinate
  turtle.hideturtle() #hides the turtle; we don't need to see it
  turtle.speed(0) #switches to max speed of the turtle

  turtle.penup() #the penup command causes the turtle not to draw

 # the following block creates the gallows #
  turtle.goto(50,50)
  turtle.pendown()
  turtle.forward(5)
  turtle.left(90)
  turtle.forward(20)
  turtle.left(90)
  turtle.forward(5)
  turtle.left(90)
  turtle.forward(1)
  turtle.penup()
  turtle.goto(55,50)
  turtle.pendown()
  turtle.left(90)
  turtle.forward(5)

  turtle.penup()
  wordassign = list(word) #creates a list of the word to establish where the correctly guessed letter should go
  turtle.goto(25,25)
  initspace = (len(word))*'_ ' #creates the initial list of letters for the game
  spacelist = list(initspace) #for changing later, because strings are immutable
  turtle.pendown()
  turtle.write(''.join(spacelist),font = ('Ariel','18','normal')) #creates the lines for the word, join ties together the list
  turtle.penup()


  letters = 0 #index of letter input to zero
  x = 1 #index of incorrect guesses to zero
  used = [] #creates an empty list to add used letters to
  tries = 6 #this is the number of times that the player can guess before they lose
  while x <= tries and letters < len(word): #runs while the player hasn't lost or won
    alphabet = turtle.textinput('Hangman','enter a letter') #guess a letter
    alphabet = alphabet.lower() #lowercase of the letter
    numalphabet = alphabet #provides method to check if the string is muliple characters

    turtle.goto(20,20)
    turtle.pendown()
    turtle.write('Letters Guessed:',font = ('Ariel','10','normal')) #provides instruction on the guessed letters
    turtle.penup()

    turtle.goto(60,50)
    turtle.pendown()
    turtle.pencolor('white') #white out previous messages
    turtle.write('You Have Already Entered This Letter.',font = ('Ariel','10','normal')) #lets the player know they have already guessed this letter
    turtle.pencolor('black') #changes the pen color back
    turtle.penup()

    if 'alphabet' == '' or len(numalphabet) > 1: #catches if the player enters an empty string or multiple letters
        turtle.goto(60,45)
        turtle.pendown()
        turtle.write('Please Enter a Singular Letter.',font = ('Ariel','10','normal')) #outputs the error message of the above condition
        turtle.penup()
    elif alphabet in word and alphabet not in used: #if the correct letter has been chosen
        ww = writeword(alphabet,spacelist,wordassign) #implements the writeword function and assigns the resulting tuple to an object
        (updatespacelist, n) = ww #unpack tuple
        letters = letters + n #if this becomes equal to the length of the word, the player will win
        spacelist = updatespacelist #updates the spacelist outside of the writeword function so the original spacelist won't be used
        used.append(alphabet) #adds the correct letter to the alphabet so they don't enter it again
    elif alphabet in used: #alerts the player to a letter that has already been played
        turtle.goto(60,50)
        turtle.pendown()
        turtle.write('You Have Already Entered This Letter.',font = ('Ariel','10','normal')) #visually alerts the player that they have already been played
        turtle.penup()
    else: #if an incorrect letter has been chosen
        turtle.pendown()
        stickman(x) #implements the stickman function to draw the man
        x = x + 1 #iterates by 1 to the next part of the stickman for the next time the stickman() fucntion is called
        used.append(alphabet) #alerts the player that this incorrect letter has already been played (adds it to the used list)
    turtle.goto(20,18)
    turtle.pendown()
    turtle.write(''.join(used),font = ('Ariel','10','normal')) #writes the letters already guessed

  if x >= tries: #when the player loses
      turtle.penup()
      turtle.goto(5,50)
      turtle.pendown()
      turtle.write('You Lose',font = ('Ariel','50','normal')) #displays message "you lose"
  else: #when the player wins
      turtle.penup()
      turtle.goto(5,50)
      turtle.pendown()
      turtle.write('You Win',font = ('Ariel','50','normal')) #displays message "you win"

# after the game is over the following happens #
  turtle.penup()
  turtle.goto(5,46)
  turtle.pendown()
  turtle.write('Click To Exit',font = ('Ariel','18','normal')) #displays instruction to the user
  turtle.exitonclick() #allows player to exit the game by clicking


def stickman(x):
## the following function draws the stickman when an incorrect letter is chosen ##
    if x == 1: #head
        turtle.penup()
        turtle.goto(50,67)
        turtle.pendown()
        turtle.circle(1)
        turtle.penup()
    elif x == 2: #torso
        turtle.penup()
        turtle.goto(50,67)
        turtle.pendown()
        turtle.right(90)
        turtle.forward(3)
        turtle.left(90)
        turtle.penup()
    elif x == 3: #arm
        turtle.penup()
        turtle.goto(50,67)
        turtle.pendown()
        turtle.right(30)
        turtle.forward(1)
        turtle.left(30)
        turtle.penup()
    elif x == 4: #arm
        turtle.penup()
        turtle.goto(50,67)
        turtle.pendown()
        turtle.left(180+30)
        turtle.forward(1)
        turtle.right(180+30)
        turtle.penup()
    elif x == 5: #leg
        turtle.penup()
        turtle.goto(50,64)
        turtle.pendown()
        turtle.right(30)
        turtle.forward(1)
        turtle.left(30)
        turtle.penup()
    else: #leg
        turtle.penup()
        turtle.goto(50,64)
        turtle.pendown()
        turtle.left(180+30)
        turtle.forward(1)
        turtle.right(180+30)
        turtle.penup()

def writeword(alphabet,spacelist,wordassign):
## the following function writes the correctly guessed letter in the space provided ##
    turtle.goto(25,25)
    c = 0
    indexing = []
    temp = wordassign
    while c < len(temp): #loops over the word to check to see how many times the letter occurs
        if alphabet == temp[c]: #if the letter chosen is in the word...
            indexing.append(c) #add the letter to the list 'indexing'
        c = c + 1 #iterates to the end of the word
    for i in range(0,len(indexing)): #loops over the length of the list of indexing
        spacelist[2*indexing[i]] = alphabet #creates the new list
    n = len(indexing) #creates variable for list of letters for later when it needs to be determined if the player won
    ww = (spacelist, n) #creates tuple to easy extract it from the function
    turtle.pendown()
    turtle.write(''.join(spacelist),font = ('Ariel','18','normal')) #writes the resulting new list, including the correct letters
    turtle.penup()
    return ww #ensures spacelist, number of letters is updated

hangman() #automatically plays the game upon running