
def isStandard(initialStates, listTransitions):

    if len(initialStates)==0:
        return True

    if len(initialStates)!=1:
        return False

    for transition in listTransitions:
        if transition[4]==initialStates[0]:
            return False

    return True


def standardizeAutomaton(alphabet, states, initialStates, finalStates,listTransitions):
    # Copying the parameters from a given automaton
    std_alphabet = alphabet[:]
    std_finalStates = finalStates[:]
    std_initialStates = initialStates[:]
    std_states = states[:]
    std_transitions = listTransitions[:]

    # Adding the entry "i"
    std_initialStates[0] = 'i'
    # Deleting all the other entry states
    del std_initialStates[1:]
    std_states.append('i')

    # Modifying the transitions, so they come from i to the needed state
    # Loop through each initial state associated transition and add new transitions to std_transitions

    for initial_state in initialStates:
        for transition in listTransitions:
            start_state, symbol, end_state = transition.split(',')
            if transition.startswith(initial_state):
                new_transition = f'i,{symbol},{end_state}'
                if new_transition not in std_transitions:
                    std_transitions.append(new_transition)

    print("This is the standardized version of the automaton :\n")
    print("Alphabet :", std_alphabet)
    print("Initial States :", std_initialStates)
    print("Final States :", std_finalStates)
    print("List of States :", std_states)
    print("List of transitions :", std_transitions)
    return std_alphabet, std_states, std_initialStates, std_finalStates, std_transitions