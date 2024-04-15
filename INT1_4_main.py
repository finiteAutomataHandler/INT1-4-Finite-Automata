from INT1_4_displayFunctions import *
from INT1_4_readAutomatons import *

if __name__ == '__main__':

    print("INT1-4 ROUGIER Jules, VAIO Lorenzo, LEBRAS Valentin, BRAHAM Kenzan and MARCHAL Thomas")

    file = selectFile()
    alphabet, states, initialStates, finalStates, listTransitions = openFile(file)
    print('\n')
    print(alphabet)
    print('\n')
    print(states)
    print('\n')
    print(initialStates)
    print('\n')
    print(finalStates)
    print('\n')
    print(listTransitions)
    print('\n')

    choice = 0
    choiceList = ["1", "2", "3", "4", "5", "6", "7", "8"]

    while choice != "8":

        displayMenu()

        choice = input("\nYour choice : \n -> ")
        while choice not in choiceList:
            choice = input("\nPlease redo: \n -> ")

        if choice == "1":

            print("\n\n\n\n================== DISPLAY AUTOMATON ================== \n")
            displayAutomaton(alphabet, states, initialStates, finalStates, listTransitions)
            input("\nPress to continue\n")

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

