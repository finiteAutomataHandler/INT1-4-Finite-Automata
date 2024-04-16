from prettytable import PrettyTable

def displayMenu():
    print("\n\n\n\n================== MAIN MENU ==================\n")
    print("1. Display the table of the automate")
    print("2. Check automaton characteristics (Deterministic/Complete/Standard)")
    print("3. Standardize the automaton")
    print("4. Obtain an equivalent complete deterministic FA")
    print("5. Obtain an equivalent minimal FA")
    print("6. Word Recognition")
    print("7. Obtain a complementary automate") #also check word recognition
    print("8. Quit")

def displayCaracteristics():
    print("\n\n\n\n================ CARACTERISTICS MENU ================\n")
    print("1. Check if deterministic")
    print("2. Check if complete")  
    print("3. Check if standard")
    print("4. Quit")

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