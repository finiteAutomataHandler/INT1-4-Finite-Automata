
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

