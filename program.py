import random
def run_game():
  r=int(input("Guess a random number : "))
  n=random.randint(1,9)
  if n == r:
    print("Guessed the correct number the number was",n)
  else:
    print("You guessed the wrong number the number was",n )
def main():
  run_game()
  play_again()
def play_again():
  #while is a format of loop which will make the code running until the given value is false
    while True:
        retry = input("Would you like to play again?(yes or no) : ")
        if retry == "yes":
            main()
        if retry == "no":
          #Just crashes the code
            exit()
        else:
            print("I'm sorry I could not recognize what you entered")
main()
