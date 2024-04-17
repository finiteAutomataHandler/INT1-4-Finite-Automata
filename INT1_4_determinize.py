
def isDeterministic(alphabet, states, initialStates, listTransitions):

    if len(alphabet) == 0:
        return True

    if len(initialStates) != 1:
        return False

    for state in states:

        letters = []

        for transition in listTransitions:

            if transition[0] == state:
                
                currentLetter = transition[2]

                if currentLetter in letters:
                    return False
                
                letters.append(currentLetter)

    return True
                
def determinizeAutomaton (alphabet, states, initialStates, finalStates, listTransitions):
    newStates=[]
    newTransitions=[]
    newInitialState = ','.join(sorted(initialStates))
    newFinalStates = []

    tempStates= [newInitialState]
    newStates.append(newInitialState)

    if any(state in finalStates for state in initialStates):
        newFinalStates.append(newInitialState)

    while tempStates:
        currentState = tempStates.pop(0)
        currentParts = currentState.split(',')

        for letter in alphabet:
            nextStates = set()
            for part in currentParts:
                for transition in listTransitions:
                    if transition.startswith(f"{part},{letter}"):
                       _, _, end_state = transition.split(',')
                       nextStates.add(end_state) 
            newState = ','.join(sorted(nextStates))
            if newState:
                if newState not in newStates:
                    newStates.append(newState)
                    tempStates.append(newState)
                    if any(state in finalStates for state in newState.split(',')):
                        newFinalStates.append(newState) 
                newTransitions.append(f"{currentState},{letter},{newState}")

    usefulStates = set()
    stack = [newInitialState]
    while stack : 
        state = stack.pop()
        if state not in usefulStates:
            usefulStates.add(state)
            for transition in newTransitions:
                startState, letter, endState = transition.split(',')
                if startState == state:
                    stack.append(endState)
    
    detTransitions = [t for t in newTransitions if t.split(',')[0] in usefulStates]
    detStatesList = list(usefulStates)
    detfinalStates = [s for s in newFinalStates if state in usefulStates]

    return alphabet, detStatesList, [newInitialState], detfinalStates, detTransitions


