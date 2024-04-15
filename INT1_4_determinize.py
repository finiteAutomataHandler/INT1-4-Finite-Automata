
def isDeterministic(alphabet, states, initalStates, listTransitions):

    if len(alphabet) == 0:
        return True

    if len(initalStates) != 1:
        return False

    for state in states:

        letters = []

        for transtition in listTransitions:

            if transtition[0] == state:
                
                currentLetter = transtition[2]

                if currentLetter in letters:
                    return False
                
                letters.append(currentLetter)

    return True
                








