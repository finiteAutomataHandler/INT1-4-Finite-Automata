from prettytable import PrettyTable

def displayMenu():
    print("\n\n\n\n================== MAIN MENU ==================\n")
    print("1. Display the table of the automate")
    print("2. Check automaton caracteristics (Deterministic/Complete/Standart)")  
    print("3. Standardize the automate")
    print("4. Obtain an equivalent complete deterministic FA")
    print("5. Obtain an equivalent minimal FA")
    print("6. Word Recognation")
    print("7. Obtain a complementary automate") #also check word recognition
    print("8. Quit")

def getStateArrow(i, initialStates, finalStates):
    if i in initialStates and i in finalStates:
        return ("<-->")
    else:
        if i in initialStates:
            return ("-->")
        else:
            if i in finalStates:
                return ("<--")
            else:
                return ("")


def displayAutomaton(alphabet, states, initialStates, finalStates, listTransitions):

    table = PrettyTable()

    listInitials = []
    listStates = []

    for i in states:

        listInitials.append(getStateArrow(i, initialStates, finalStates))
        listStates.append(i)

    table.add_column("Status", listInitials)
    table.add_column("States", listStates)

    for letter in alphabet:

        displayTransitions = []

        for state in states:
            transitionString = ""

            for transition in listTransitions:
                splitTransitions = transition.split(",")
                if splitTransitions[0] == state and splitTransitions[1] == letter:
                    transitionString += splitTransitions[2] + ","

            if transitionString == "":
                transitionString += "---"

            displayTransitions.append(transitionString.strip(","))

        table.add_column("Transition " + letter, displayTransitions)

    table.align = "c"
    print(table)