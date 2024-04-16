
def isStandart(initialStates, listTransitions):

    if len(initialStates)==0:
        return True

    if len(initialStates)!=1:
        return False

    for transition in listTransitions:
        if transition[4]==initialStates[0]:
            return False

    return True 