from INT1_4_displayFunctions import *

if __name__ == '__main__':

    print("INT1-4 ROUGIER Jules, VAIO Lorenzo, LEBRAS Valentin, BRAHAM Kenzan and MARCHAL Thomas")

    choice = 0
    choiceList = ["1", "2", "3", "4", "5", "6", "7", "8"]

    while choice != "8":

        displayMenu()

        choice = input("\nYour choice : \n -> ")
        while choice not in choiceList:
            choice = input("\nPlease redo: \n -> ")

        if choice == "1":

            #1. Display the table of the automate
            break

        elif choice == "2":

            #2. Check automaton caracteristics (Deterministic/Complete/Standart)
            break

        elif choice == "3":

            #3. Standardize the automate
            break

        elif choice == "4":

            #4. Obtain an equivalent complete deterministic FA
            break

        elif choice == "5":

            #5. Obtain an equivalent minimal FA
            break

        elif choice == "6":

            #6. Word Recognation
            break

        elif choice == "7":

            #7. Obtain a complementary automate
            break

        elif choice == "8":

            #8. Quit
            break

    print("\n\nSee you later !")

