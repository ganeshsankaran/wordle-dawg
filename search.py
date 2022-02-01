# search words by constraints

import json

scores = json.loads(open('scores.json', 'r').read())

# ignore my poor OOP design
class Green:
    def __init__(self, char, pos):
        self.char = char
        self.pos = pos

    def __eq__(self, word):
        return word[self.pos] == self.char

class Yellow:
    def __init__(self, char, pos):
        self.char = char
        self.pos = pos

    def __eq__(self, word):
        return self.char in word and word[self.pos] != self.char

class Black:
    def __init__(self, char):
        self.char = char

    def __eq__(self, word):
        return self.char not in word

def get_new_constraints(word, colors):
    constraints = []

    for i in range(5):
        if colors[i] == 'g':
            constraints.append(Green(word[i], i))
        elif colors[i] == 'y':
            constraints.append(Yellow(word[i], i))
        else:
            constraints.append(Black(word[i]))

    return constraints

def search(constraints = []):
    results = {}

    # get words satisfying all constraints
    for word, score in scores.items():
        if all([word == c for c in constraints]):
            results[word] = score
    
    # sort search results by score
    sorted_results = dict(sorted(results.items(),
                                 key = lambda item: item[1],
                                 reverse = True))
    
    return list(sorted_results)