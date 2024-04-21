def recognize_word(word, alphabet, states, initial_states, final_states, list_transitions):
    current_states = initial_states

    for char in word:
        if char not in alphabet:
            return False  # Invalid character in the word

        next_states = []

        for state in current_states:
            transitions_for_state = [transition for transition in list_transitions if transition[0] == state and transition[1] == char]

            if transitions_for_state:
                next_states.extend([transition[2] for transition in transitions_for_state])

        if not next_states:
            return False  # No valid transition for the current state and character

        current_states = next_states

    # Check if any of the current states are final states
    return any(state in final_states for state in current_states)

def read_word():
    word = input("Enter a word (type 'end' to stop): ").strip()
    return word

def complementary_automaton(alphabet, states, initial_states, final_states, list_transitions):

    complementary_final_states = set(states) - set(final_states)  # Complement of final states

    # Compute transitions for the complementary automaton
    transitions = {}
    for state in states:
        for char in alphabet:
            if (state, char) not in list_transitions:
                transitions[(state, char)] = final_states
            else:
                transitions[(state, char)] = set(states) - set(list_transitions[(state, char)])

    # Return the complementary automaton
    return alphabet, states, initial_states, complementary_final_states, transitions

def recognize_word(alphabet, states, initial_states, final_states, list_transitions):
    while True:
        word = read_word()

        if word == 'end':
            break

        if recognize_word(word, alphabet, states, initial_states, final_states, list_transitions):
            print("Recognized: Yes")
        else:
            print("Recognized: No")
