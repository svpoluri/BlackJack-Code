# Blackjack card game
import random
#================================================
# constants, lists, and dictionaries
#The entire dictionary for an ordered deck is stored here so it can be called to later
basedeck = dict()
cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'] #Defines card types in list
spades = [] #Creates an empty list for each suit
hearts = []
clubs = []
diamonds = []
for i in range(13): #adds a letter representing each suit to its respective list 13 times (the number of card types)
    spades += "S"
    hearts += "H"
    clubs += "C"
    diamonds += "D"
for i in range(13): #adds the card types to each suit to create lists of strings
    spades[i] = str(cards[i]) + spades[i]
    hearts[i] = str(cards[i]) + hearts[i]
    diamonds[i] = str(cards[i]) + diamonds[i]
    clubs[i] = str(cards[i]) + clubs[i]
spades.extend(hearts) #adds each list together
spades.extend(clubs)
spades.extend(diamonds)
for i in range(52): #creates the dictionary itself by looking at the card type of each item in the list and setting it equal to the appropriate blackjack value
    if 'A' in spades[i][0]:
        basedeck[spades[i]] = 11
    elif 'K' in spades[i][0] or 'Q' in spades[i][0] or 'J' in spades[i][0] or '0' in spades[i][1]:
        basedeck[spades[i]] = 10
    else:
        basedeck[spades[i]] = int(spades[i][0])
#=================================================
# creates the deck of 52 cards

def makeDeck():
    """This function actually turns the dictionary into a list so that it can be shuffled, this results in each dictionary term becoming (key, value) in the list"""
    t = [(c, p) for c, p in basedeck.items()] #turns dictionary into list of lists containing (card, point value)
    return(t)


#=================================================
# Deals a card from the Deck. May have a parameter
# 'hand' that is  passed by reference and is
# modified in the function by appending a card
# to a hand. It also removes the dealt card from
# Deck so that it is not drawn again.
def deal(deck):
    """This function simply takes the top card of the deck and returns it to the main function"""
    card = deck.pop(0)
    return(card)

#==================================================
# Shuffles the cards by recreating the data using
# random. It should include a call to random.seed().
def shuffle(deck):
    """This function shuffles the ordered decklist into a random one"""
    random.seed(a=None)
    random.shuffle(deck)
    return(deck)

#==================================================
def total(hand, sub):
    """This function calculates the point total in a hand and returns it, by taking the hand and subtractor of the dealer or player respectively"""
    tot = 0
    for i in range(len(hand)): #simply uses the dictionary to determine the point value of each card
        tot += basedeck[hand[i]]
    tot = tot - (10 * sub) #then subtracts the amount of times 10 has been subtracted due to an ace bringing a player over
    return(tot) #returns the total back

#==================================================
def score(dw, pw):
    """This function takes the amount of dealer wins and player wins and prints them with their respective phrases"""
    print("Dealer Wins: ", dw)
    print("Player Wins: ", pw)

# =================================================
def main():
  """This function runs the entire blackjack game, complete with many function calls and exceptions to rules that need to be explained"""
  playing = True #Makes sure the game starts since it runs while playing = true
  newdeck = shuffle(makeDeck()) #makes a new random list called "newdeck" consisting of shuffled cards
  print(newdeck) #prints the list of cards
  dealerWins = 0 #sets variables for keeping score
  playerWins = 0
  ranout = 0 #this "ranout" variable keeps track of when the deck has run out of cards and is put here as 0 because right now it is false, the deck has cards.
  while playing:
      if len(newdeck) < 4: #This conditional statement checks if there are enough cards to start a game, if not, it ends the program and prints the score
          print("You ran out of cards in the deck.  Thanks for playing!")
          playing = False
          score(dealerWins, playerWins) #calls the score function to print out the score tallies
          break
      else:
          #Starting Hands
          dealerHand = [] #sets an empty list for the dealer's hand
          dealerTotal = 0 #sets 0 for the dealer's point value
          playerHand = [] #same as above but for player
          playerTotal = 0
          dsubtractor = 0 #dsubtractor (for dealer) and subtractor (for player) keep track of how many times 10 has been subtracted from a total hand value in case the hand has an ace when the hand goes over 21
          subtractor = 0
          dealerHand.append(deal(newdeck)[0]) #adds a new card to the dealers hand from the top of the deck
          dealerTotal = total(dealerHand, dsubtractor) #calls the total function to determine the dealer's score
          dealerSeepoint = dealerTotal #creates a variable that stores what the dealer's revealed card is
          dealerHand.append(deal(newdeck)[0])
          dealerTotal = total(dealerHand, dsubtractor)
          print("The dealer's revealed card is: ", [dealerHand[0]]) #prints what cards the player can see in the dealers hand
          print("Meaning the dealer's revealed total is: ", dealerSeepoint) #prints what the total of the dealer's revealed hand is
          if dealerTotal == 22: #if the total is 22 on the first deal, this sets it back to 12 since the hand has to have contained two aces
              dealerTotal = dealerTotal - 10
              dsubtractor += 1 #since a 10 was subtracted, dsubtractor increases
          if dealerTotal == 21: #if the dealer gets a blackjack, they win
              print("The dealer's hand was ", dealerHand) #prints what happened
              print("Meaning the dealer got 21, blackjack.")
              print("Sorry you lose, better luck next time.")
              dealerWins += 1 #adds to the number of dealer wins
          playerHand.append(deal(newdeck)[0]) #gives the player their cards
          playerHand.append(deal(newdeck)[0])
          playerTotal = total(playerHand, subtractor) #calls the total function to determine the player's score
          if playerTotal == 22:
              playerTotal = playerTotal - 10
              subtractor += 1
          if dealerTotal != 21: #this is an interesting conditional where if the dealer gets blackjack, it changes the print from being in present tense to past tense, to indicate that the player has lost
              print("The cards in your hand are: ", playerHand)
              print("Meaning your total is:", playerTotal)
          elif dealerTotal == 21:
              print("The cards in your hand were: ", playerHand)
              print("Meaning your total was:", playerTotal)
          if playerTotal == 21 and dealerTotal != 21: #checks if the player got a natural and the dealer did not, because the dealer wins in tied scenarios
              print("Congratulations, you got blackjack!  You win!")
              playerWins += 1 #adds to the number of player wins
          no = 0 #sets up the appropriately named conditional: "no" which checks whether or not the player has busted before running the dealer's draw code
          while playerTotal < 21 and dealerTotal != 21: #checks if the player can be "hit" and that the dealer hasn't already won
              if len(newdeck) != 0: #conditional that checks if there are cards in the deck that can be used for "hitting"
                  response = input("Would you like to hit (y or n)? ") #asks player if they want to "hit"
                  if response == 'y': #if the player says y
                      playerHand.append(deal(newdeck)[0]) #adds a card to the players hand
                      playerTotal = total(playerHand, subtractor)
                      if playerTotal < 21: #if the player is under 21, it prints the players hand and runs the "hit" program again
                          print("The cards in your hand are: ", playerHand)
                          print("Meaning your total is: ", playerTotal)
                      elif playerTotal > 21: #if the player is over 21, it checks a few things
                          counter = 0 #sets a counter that counts how many aces are in a player's hand
                          for i in range(len(playerHand)): #checks for aces in player's hand
                              if 'A' == playerHand[i][0]:
                                  counter += 1
                          while counter > subtractor and playerTotal > 21: #if the player is over 21, and has aces that are still 11s, this part will convert the remaining aces into 1s until the function is under 21
                              playerTotal = playerTotal - 10
                              subtractor += 1 #increases subtractor everytime a 10 is subtracted so the total can be calculated with subtractor
                          if playerTotal > 21: #however, if even the aces can't keep the player under 21, then they bust
                              print("The cards in your hand are: ", playerHand)
                              print("Meaning your total is: ", playerTotal)
                              print("Sorry you have busted, you lose.  Better luck next time.")
                              no = 1 #no is increased to 1 to show that the player has busted, so there is "no" need to run the dealer draw code
                              dealerWins += 1 #increases dealer wins
                          elif playerTotal == 21: #if the player ends up getting 21, they are forced to stay as the dealer draws
                              print("The cards in your hand are: ", playerHand)
                              print("Meaning your total is: ", playerTotal)
                              print("You have no choice but to stay.")
                          else: #if the player's aces keep them under 21, then their hand is printed and the "hit" program runs again
                              print("The cards in your hand are: ", playerHand)
                              print("Meaning your total is: ", playerTotal)
                      else: #if the player's hand is equal to 21, they are forced to stay as the dealer then draws
                          print("The cards in your hand are: ", playerHand)
                          print("Meaning your total is: ", playerTotal)
                          print("You have no choice but to stay.")
                  elif response == 'n': #if the player wishes not to hit, then can choose to not hit
                      print("You will stay with the cards: ", playerHand)
                      print("Meaning your total is:", playerTotal)
                      break
                  elif response == 'quit': #this allows the player to quit in the middle of a round if they so wish
                      playing = False
                      break
                  else: #if the player gives an invalid command, they have the opportunity to try again!
                      print("Please Try Again.")
              else:
                  ranout = 1 #if there are no more cards in the deck, ranout is set to 1
                  break
          while dealerTotal < 21 and no == 0: #runs the draw program for the dealer while they are under 21 and the player hasn't busted
              if len(newdeck) != 0: #same way of checking if the deck is out of cards like in the playerTotal part
                  if dealerTotal < 17: #the dealer has to hit if they are under 17, so this program does that
                      dealerHand.append(deal(newdeck)[0]) #almost everything below is the same as the playerTotal function so go back up if you need these things explained
                      dealerTotal = total(dealerHand, dsubtractor)
                      if dealerTotal > 21:
                          counter = 0
                          for i in range(len(dealerHand)):
                              if 'A' == dealerHand[i][0]:
                                  counter += 1
                          while counter > dsubtractor and dealerTotal > 21:
                              dealerTotal = dealerTotal - 10
                              dsubtractor += 1
                          if dealerTotal > 21: #if the dealer busts, the player gets a win
                              print("The cards in the dealer's hand were: ", dealerHand)
                              print("Meaning the dealer's total is: ", dealerTotal)
                              print("The dealer has busted! You win!")
                              playerWins += 1
                              break
                      elif dealerTotal == 21: #if the dealer gets 21, they automatically win since they win ties
                          print("The cards in the dealer's hand were: ", dealerHand)
                          print("Meaning the dealer's total is: ", dealerTotal)
                          print("The dealer got 21, you lose.")
                          dealerWins += 1
                          break
                  elif dealerTotal >= 17: #if the dealer is above 17 then the program stops hitting
                      break
              else:
                  ranout = 1 #same ranout as before, keeping track of if there are cards in the deck to be drawn
                  break
          if ranout == 1: #if cards cannot be drawn from the deck, it prints out a nice message and the final tallies
              print("You ran out of cards in the deck.  Thanks for playing!")
              score(dealerWins, playerWins) #calls the score function with the amount of dealer wins and player wins and then the function prints them out
              playing = False
          if playerTotal == 21 and len(playerHand) == 2: #in the case that the player gets 21 on the first draw, it prints the score, the wins are not incremented here because they are incremented earlier in the function, and even though the player has 21, if the dealer also had 21, they win, which is taken care of earlier in the function
              score(dealerWins, playerWins)
              playing = would() #each time this appears, it is asking the player if they would like to continue playing, if not, then the program ends.
          elif playerTotal > 21: #if the player busts, it displays the scores, again the score is incremented earlier in the function when that happens
              score(dealerWins, playerWins)
              playing = would()
          elif dealerTotal >= 21: #if the dealer busts or gets 21 then the score is displayed, again the scores are incremented earlier in the function when these things happen
              score(dealerWins, playerWins)
              playing = would()
          elif playerTotal <= dealerTotal: #if the dealer ties or beats the player without going over 21, then the dealers score is incremented and the tallies are displayed
              print("The cards in the dealer's hand were: ", dealerHand)
              print("Meaning the dealer's total is: ", dealerTotal)
              print("You lose. The dealer had equal to or more points than you without going over 21.")
              dealerWins += 1
              score(dealerWins, playerWins)
              playing = would()
          elif playerTotal > dealerTotal: #if the player beats the dealer, then the score is incremented and the tallies are displayed
              print("The cards in the dealer's hand were: ", dealerHand)
              print("Meaning the dealer's total is: ", dealerTotal)
              print("You win! You had more points than the dealer without going over 21!")
              playerWins += 1
              score(dealerWins, playerWins)
              playing = would()

def would():
    """Asks the player if they want to continue, depending on their answer, it returns a true or false"""
    a = input("Would you like to continue playing (y or n)? ")
    if a == 'y':
        c = True
    elif a == 'n':
        c = False
    else: #if the player does not answer a 'y' or 'n', it asks the player to try again and recalls the would function
        print("Command not understood, try again.")
        return(would())
    return(c)

main() #calls the main function and starts the game
