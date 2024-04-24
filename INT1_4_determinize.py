
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
                
def determinize(alphabet, states, initialStates, finalStates, listTransitions):

    if 'ε' in alphabet:
        tempTransitions = []
        tempTerm = []

        for transition in listTransitions:
            if "ε" in transition:

                splitTransition = transition.split(",")

                for secondTransition in listTransitions:

                    newTransition = ""
                    splitSecondTransition = secondTransition.split(",")

                    if splitTransition[2] == splitSecondTransition[0]:
                        newTransition += splitTransition[0] + secondTransition[1:]

                        if "ε" in newTransition:
                            listTransitions.append(newTransition)

                        else: 
                            tempTransitions.append(newTransition)
                    
                    elif splitTransition[2] in finalStates and splitTransition[0] not in tempTerm:
                        tempTerm.append(splitTransition[0])
            
            else:
                tempTransitions.append(transition)

        finalStates = tempTerm
        listTransitions = tempTransitions

    # print(alphabet)
    # print(states)
    # print(initialStates)
    # print(finalStates)
    # print(listTransitions)


    newInitialState = ""
    for initialState in initialStates:
        newInitialState += str(initialState)

    newTransitions = []
    newTransitionsBase = []

    for letter in alphabet:
        resultTransition = ""

        for transition in listTransitions:
            splitTransition = transition.split(",")

            if letter == splitTransition[1] and splitTransition[0] in initialStates:
                if splitTransition[2] not in resultTransition:
                    resultTransition += splitTransition[2]
        
        if resultTransition != "":
            newTransitionsBase.append(resultTransition)
            newTransitions.append(newInitialState + "," + letter + "," + resultTransition)


    for newState in newTransitionsBase:
        for letter in alphabet:

            resultTransition = ""

            for state in newState:
                for transition in listTransitions:
                    splitTransition = transition.split(",")
                    if letter == splitTransition[1] and splitTransition[0] == state:
                        if splitTransition[2] not in resultTransition:
                            resultTransition += splitTransition[2]
            
            if resultTransition not in newTransitionsBase and resultTransition != "":
                newTransitionsBase.append(resultTransition)

            if resultTransition != "":
                newTransitions.append(newState + "," + letter + "," + resultTransition)

            regroupStates = []

            for transition in newTransitions:
                newTransition = transition.split(",")
                if newTransition[0] not in regroupStates:
                    regroupStates.append(newTransition[0])
                if newTransition[2] not in regroupStates:
                    regroupStates.append(newTransition[2])

    newFinals = []   
    for state in regroupStates:
        for j in state:
            if j in finalStates and state not in newFinals:
                newFinals.append(state)

    newAlphabet = []
    for letter in alphabet:
        if letter != "ε":
            newAlphabet.append(letter)

    return (newAlphabet, regroupStates, regroupStates[0], newFinals, newTransitions)
                                                 

            

                        









