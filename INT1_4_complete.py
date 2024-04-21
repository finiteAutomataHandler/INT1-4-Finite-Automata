
def isComplete(alphabet, states, finalStates, listTransitions):

    for state in states:

        letters = []

        for transition in listTransitions:

            if transition[0] == state:
                if (transition[2] not in letters):
                    letters.append(transition[2])

        if sorted(alphabet) != sorted(letters):
            return False

    return True



def completeAutomaton(alphabet, states, initialStates, finalStates, transitions):
    for state in states:
        letters = set()
        for transition in transitions:
            decomposed_transition = transition.split(",")
            if decomposed_transition[0] == state:
                actual_letter = decomposed_transition[1]
                if actual_letter not in letters:                        
                    letters.add(actual_letter)

        # for values in letters:

        for l_alphabet in alphabet:
            if ("P," + l_alphabet + ",P") not in transitions:           
                transitions.append("P," + l_alphabet + ",P")
            if l_alphabet not in letters:
                transitions.append(state + "," + l_alphabet + ",P")     

    states.append("P")                                                  

    return alphabet, states, initialStates, finalStates, transitions


