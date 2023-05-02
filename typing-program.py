# Importing libraries here
import time

# Greetings to user
print("\t\t\tWelcome to K-Type App!\n"
      "\tTest your typing speed!")

# Game function starts here
def game_start():

    # List of sentence examples
    sentenceList = ["He always carries a book.",
                    "The quick, brown fox",
                    "She is so beautiful.",
                    "Math is really good",
                    "Some people are really weird."]

    sentenceLen = int(len(sentenceList))  # Length of the list

    i = 0   # For indexing

    start_time = time.time()  # Start the timer

    # Game starts here
    while True:
        # Let the user know what to type
        print(f'Your sentence:\n'
              f'\t{sentenceList[i]}')

        time.sleep(0.5)             # Wait half a second

        # Take the user input here
        userType = input('-: ')

        # If the sentence is correct
        if userType == sentenceList[i]:
            # If there is no sentence left, finish the loop and print the time
            if i == sentenceLen-1:
                stop_time = time.time()     # Stop the timer
                print(f'\nYou successfully completed in {int(stop_time - start_time) - 1} seconds.')
                break

            i += 1          # Add 1 to i on every loop
            print('\n')
            continue        # Return to loop

        # If the sentence is incorrect
        else:
            print('Incorrect! Try again!\n')
            continue        # Return to loop



# Asking user to see the rules or start the app
def user_options():

    # Global statement for userInput
    global userInput

    try:
        # Taking user input as an integer
        userInput = int(input('\nSee the rules | 1\n'
                              'Start the app | 2 : '))

    # Exception handling for non-integer values
    except ValueError:
        print('Invalid input, try again.\n')
        return user_options()

    # If user wants to see the rules
    if userInput == 1:
        print('\n')
        print('=-'*34)
        print('\t'*7, 'RULES')
        print('-='*34)

        # Showing user the rules
        print("\tAfter you start, the program is going to give you 5 sentences.\n"
              "\t\t\t\tHow fast can you type ?  (: \n")

        # A little fancy way to starting the game function
        i = 0
        j = 3
        while i < 3:
            time.sleep(1.3)
            print(f'Game starts in {j}...')
            i += 1
            j -= 1

        time.sleep(1.5)         # Wait 1.5 secs to start the game
        print('\n')
        return game_start()     # Send user to the game function

    # If user wants to start the app directly
    elif userInput == 2:
        # A little fancy way to starting the game function
        i = 0
        j = 3
        while i < 3:
            time.sleep(1.3)
            print(f'Game starts in {j}...')
            i += 1
            j -= 1

        time.sleep(1.5)  # Wait 1.5 secs to start the game
        print('\n')
        return game_start()  # Send user to the game function



user_options()
