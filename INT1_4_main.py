from INT1_4_displayFunctions import *
from INT1_4_readAutomatons import *
from INT1_4_determinize import *
from INT1_4_complete import *
from INT1_4_standart import *

if __name__ == '__main__':

    print("INT1-4 ROUGIER Jules, VAIO Lorenzo, LEBRAS Valentin, BRAHAM Kenzan and MARCHAL Thomas")

    file = selectFile()
    alphabet, states, initialStates, finalStates, listTransitions = openFile(file)
    print(alphabet)
    print(states)
    print(initialStates)
    print(finalStates)
    print(listTransitions)

    choice = 0
    choiceList = ["1", "2", "3", "4", "5", "6", "7", "8"]
    optionList = ["1", "2", "3", "4"]

    while choice != "8":

        displayMenu()

        choice = input("\nYour choice : \n -> ")
        while choice not in choiceList:
            choice = input("\nPlease redo : \n -> ")

        if choice == "1":

            #1. Display the table of the automate
            print("\n\n\n\n================== DISPLAY AUTOMATON ================== \n")
            displayAutomaton(alphabet, states, initialStates, finalStates, listTransitions)
            input("\nPress to continue\n")

        elif choice == "2":

            #2. Check automaton caracteristics (Deterministic/Complete/Standart)
            displayCaracteristics()

            option = input("\nYour choice : \n -> ")
            while option not in optionList:
                option = input("\nPlease redo : \n -> ")

            if option == "1":

                #1. Check if deterministic
                deterministic = isDeterministic(alphabet, states, initialStates, listTransitions)
                if deterministic:
                    print("This automaton is deterministic !")
                else:
                    print("This automaton is not deterministic")

                input("\nPress to continue\n")

            elif option == "2":

                #2. Check if complete
                complete = isComplete(alphabet, states, finalStates, listTransitions)
                if complete:
                    print("This automaton is complete")
                else:
                    print("This automaton is not complete")

                input("\nPress to continue\n")

            elif option == "3":

                standart = isStandart(initialStates, listTransitions)
                if standart:
                    print("This automaton is standart")
                else:
                    print("This automaton is not standart")
                
                input("\nPress to continue\n")

            elif option == "4":

                #4. Quit
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

