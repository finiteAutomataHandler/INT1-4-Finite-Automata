from collections import deque
def minimize(alphabet, states, initialStates, finalStates, listTransitions):
    # Convert listTransitions to transition table format
    transitionTable = {}
    for state in states:
        transitionTable[state] = {}
    for transition in listTransitions:
        state, letter, nextState = transition.split(',')
        print(state, letter, nextState)
        transitionTable[state][letter] = nextState

    # Helper function to check if two states are distinguishable
    def are_distinguishable(state1, state2, marked):
        if (state1, state2) in marked or (state2, state1) in marked:
            return False
        for letter in alphabet:
            next_state1 = transitionTable[state1].get(letter)
            next_state2 = transitionTable[state2].get(letter)
            if next_state1 != next_state2 and (next_state1, next_state2) in marked or (next_state2, next_state1) in marked:
                return False
        return True

    # Initialize the equivalence classes
    equivalence_classes = [{state} for state in states]
    marked = set()

    # Mark distinguishable pairs of states
    for i in range(len(states)):
        for j in range(i + 1, len(states)):
            if (states[i] in finalStates and states[j] not in finalStates) or (states[i] not in finalStates and states[j] in finalStates):
                marked.add((states[i], states[j]))

    # Iterate until no more distinguishable pairs are found
    while True:
        changes_made = False
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                if (states[i], states[j]) not in marked and are_distinguishable(states[i], states[j], marked):
                    marked.add((states[i], states[j]))
                    changes_made = True

        # If no changes were made, break the loop
        if not changes_made:
            break

    # Merge equivalent states into new states
    new_states = []
    new_final_states = set()
    new_initial_states = set()

    for equiv_class in equivalence_classes:
        representative = equiv_class.pop()
        new_states.append(representative)
        if representative in finalStates:
            new_final_states.add(representative)
        if representative in initialStates:
            new_initial_states.add(representative)

        for state in equiv_class:
            for letter in alphabet:
                transition = transitionTable[state].get(letter)
                if transition:
                    transitionTable[representative][letter] = transition

    # Remove unreachable states
    reachable_states = set()
    stack = list(new_initial_states)
    while stack:
        current_state = stack.pop()
        reachable_states.add(current_state)
        for letter in alphabet:
            next_state = transitionTable[current_state].get(letter)
            if next_state and next_state not in reachable_states:
                stack.append(next_state)

    new_states = [state for state in new_states if state in reachable_states]
    new_final_states = new_final_states.intersection(reachable_states)
    new_initial_states = new_initial_states.intersection(reachable_states)

    # Convert transition table to listTransitions format
    new_listTransitions = []
    for state in new_states:
        for letter, next_state in transitionTable[state].items():
            new_listTransitions.append(f"{state},{letter},{next_state}")

    return [alphabet, new_states, list(new_initial_states), list(new_final_states), new_listTransitions]

# Example usage with provided inputs:
alphabet = ['a', 'b']
states = ['0', '1', '2']
initialStates = ['1']
finalStates = ['0']
listTransitions = ['1,a,2', '1,b,2', '2,b,0', '0,a,0', '0,b,0']

minimized_dfa = minimize(alphabet, states, initialStates, finalStates, listTransitions)
print(minimized_dfa)
