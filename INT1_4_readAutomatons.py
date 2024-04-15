def selectFile():
    print("Please, enter the automaton id :\n")
    fileId = int(input(""))
    while (fileId < 0 or fileId > 44):
        print("\nPlease redo :")
        fileId = int(input(""))

    return "./INT1-4-automatons/INT1_4_" + str(fileId) + ".txt"

def filtrerList(listName, numLine, firstCharIndex, separator):
    return listName[numLine][firstCharIndex:].split(separator)


def openFile(url):
    with open(url, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()

        alphabet = filtrerList(lines, 0, 4, ',')

        states = filtrerList(lines, 1, 4, ',')

        initialStates = filtrerList(lines, 2, 4, ',')

        finalStates = filtrerList(lines, 3, 4, ',')

        listTransitions = []
        for line in lines[4:]:
            listTransitions.append(line)

        if len(alphabet) == 1 and alphabet[0] == "":
            alphabet = []

    return alphabet, states, initialStates, finalStates, listTransitions