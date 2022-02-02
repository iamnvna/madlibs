import random

print("Welcome to madlib! This program accepts four inputs \n"
      "and throws out a sentence. \n")

ready = input("Ready (Y/N): ")
while True:
    if ready.lower() == "y":
        adj = input("Adjective: ")
        verb1 = input("Verb: ")
        verb2 = input("Verb: ")
        famous_person = input("Famous Person: ")
        
        madlib1 = f"\nComputer programming is so {adj}, it makes me so excited all the time because" \
                  f" I love to {verb1}. Stay hydrated and {verb2} like {famous_person}."
        
        madlib2 = f"\nHuman Anatomy is so {adj}, it triggers me all the time because" \
                  f" I hate to {verb1}. Stay away and {verb2} like {famous_person}."
        
        madlib = random.choice([madlib1, madlib2])
        print(madlib)
        
        go_again = input("Go again? (Y/N): ")
        if go_again.lower() == "y":
            continue
        else:
            break
    else:
        quit()

# Commentary
"""
Line 1:
      Line 1 is the random python module. It allows us to choose randomly between two or more choices.

Line 3-4:
      Lines 3 & 4 is the usual print statement used here to welcome users to the program.

Line 6:
      Line 6 accepts a user input (Y/N) and evaluates it to tell if the user wants to run the proqram
      or quit.

Line 7:
      The while True loop here allows the user to iterate through the code again when any of the user
      input evaluates to continue in the block of code. The evaluation for this code is done at Line 23-
      27.

Line 9-12:
      Note that line 8, evaluates the input from line 6 and runs the appropriate block of code. The code
      in line 9-12 are variables that accept various inputs from the user that fill up the madlib sentences.

Line 14-15, 17-18:
      These set of lines are the output statements which combine with the inputs collected from the user.
      One set is positive, and the other is negative. The idea is to allow the program make a random choice
      between the two and hopefully throw the user off depending on either their inputs were positive or
      negative.

Line 20-21:
      The two sets of lines are passed as a list into the random.choice() method from the random module
      imported and the program makes a random decision between which one to print. The out put is printed
      in line 21.

Line 23-27:
      This block of code evaluates a users response to if they want to play again or not and runs the
      appropriate code.

Line 28-29:
      Where the user input evaluates to 'n' or any other input from line 6, the program quits.
"""