from INT1_4_displayFunctions import *
from INT1_4_readAutomatons import *
from INT1_4_determinize import *
from INT1_4_complete import *
from INT1_4_standart import *
from INT1_4_Minimize import *
from INT1_4_Complementary_and_recognition import *

if __name__ == '__main__':

    print("INT1-4 ROUGIER Jules, VAIO Lorenzo, LEBRAS Valentin, BRAHAM Kenza and MARCHAL Thomas")

    print("\n\n\n")
    print("░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░      ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓██████████████▓▒░░▒▓████████▓▒░ ")
    print("░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        ")
    print("░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        ")
    print("░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░ ░▒▓█▓▒░     ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░   ")
    print("░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        ")
    print("░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        ")
    print(" ░▒▓█████████████▓▒░░▒▓████████▓▒░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░")
    print("\n\n\n")

    file = selectFile()
    alphabet, states, initialStates, finalStates, listTransitions = openFile(file)

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

                standard = isStandard(initialStates, listTransitions)

                if standard:
                    print("This automaton is standard")

                else:
                    print("This automaton is not standard")

                input("\nPress to continue\n")

            elif option == "4":

                #4. Quit
                break

        elif choice == "3":

            # 3. Standardize the automaton
            standard = isStandard(initialStates, listTransitions)
            if standard:
                print("This automaton is already standardized")
            else:
                print("This automaton is not standardized, creating a new version now :")
                std_alphabet, std_states, std_initialStates, std_finalStates, std_listTransitions = standardizeAutomaton(
                alphabet, states, initialStates, finalStates, listTransitions)
                displayAutomaton(std_alphabet, std_states, std_initialStates, std_finalStates, std_listTransitions)

            input("\nPress to continue\n")

        elif choice == "4":

            #1. Check if deterministic and complete else determinize if necessary then complete
            deterministic = isDeterministic(alphabet, states, initialStates, listTransitions)
            complete = isComplete(alphabet, states, finalStates, listTransitions)
        
            if not (deterministic or complete):
                if not deterministic:
                    print("This  automaton is not deterministic\n")
                    alphabet, states, initialStates, finalStates, listTransitions = determinize(alphabet, states, initialStates, finalStates, listTransitions)
                if not complete:
                    print("This  automaton is not complete\n")
                    alphabet, states, initialStates, finalStates, listTransitions = completeAutomaton(alphabet, states, initialStates, finalStates, listTransitions)
            
            print("The deterministic and complete automaton :\n")
            displayAutomaton(alphabet, states, initialStates, finalStates, listTransitions)


            input("\nPress to continue\n")

        elif choice == "5":

            if isDeterministic(alphabet, states, initialStates, listTransitions) == False or isComplete(alphabet, states, finalStates, listTransitions) == False:
                print("The automaton is not deterministic or complete, we are unable to minimize it for now.")
            else:
                #5. Obtain an equivalent minimal FA
                minimized = minimize(alphabet, states, initialStates, finalStates, listTransitions)
                print("Minimized DFA:")
                print(alphabet, states, initialStates, finalStates, listTransitions)
                print(minimized)
                displayAutomaton(minimized[0], minimized[1], minimized[2], minimized[3], minimized[4])
            
        elif choice == "6":

            word_recognition(alphabet, states, initial_states, final_states, list_transitions)

        elif choice == "7":
            complementary_automaton = complementary_automaton(alphabet, states, initialStates, finalStates, listTransitions)
            print("Complementary Automaton:")
            displayAutomaton(complementary_automaton[0],complementary_automaton[1], complementary_automaton[2], complementary_automaton[3], complementary_automaton[4])

            word_recognition(complementary_automaton[0],complementary_automaton[1], complementary_automaton[2], complementary_automaton[3], complementary_automaton[4])
            
        elif choice == "8":

            #8. Quit
            break

    print("\n\nSee you later !")

