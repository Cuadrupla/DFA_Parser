import argparse, pathlib
from dfa_parser_engine import reading

sigma = []
delta = {}
states = {}


def check_word(word):
    for letter in word:
        if letter not in sigma:
            raise Exception('[ERROR]: A letter from this word is not in the current alphabet.')


good = False


def parse_word(string, state):
    global good
    if (states[state] == "S/F" or states[state] == "F") and len(string) == 0:
        good = True
    elif len(string) != 0:
        for i in delta[state]:
            for j in range(0, len(delta[state][i])):
                if string.find(delta[state][i][j]) == 0:
                    parse_word(string[len(delta[state][i][j]):], i)
    else:
        raise Exception('[ERROR]: The given word isn\'t good')
    return good


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Given a specific file and a specific string parse and validate that the DFA accepts the word')
    parser.add_argument('file', type=pathlib.Path)
    parser.add_argument('string', type=str)
    args = parser.parse_args()

    try:
        reading(sigma, delta, states, args.file)
        check_word(args.string)
    except Exception as exception:
        print(exception.args)
        exit()

    start_state = None
    for state in states:
        if states[state] == "S" or states[state] == "S/F":
            start_state = state

    if start_state is not None:
        try:
            if parse_word(args.string, start_state):
                print("The word is accepted by this DFA.")
            else:
                print("[ERROR]: The given word isn\'t good'")
        except Exception as exception:
            print(exception.args)
