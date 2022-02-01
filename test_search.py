# test heuristic

import json
import matplotlib
import matplotlib.pyplot as plt
import statistics as stats
from collections import Counter
from search import *

def get_colors(word, guess):
    colors = ''

    for i in range(5):
        if word[i] == guess[i]:
            colors += 'g'
        elif word[i] != guess[i] and guess[i] in word:
            colors += 'y'
        else:
            colors += 'b'

    return colors

words = open('words.txt', 'r').read().split()
results = {}

for word in words:
    tries = 0
    constraints = []

    while True:
        guess = search(constraints)[0]
        tries += 1
        
        if word == guess:
            break

        colors = get_colors(word, guess)
        constraints += get_new_constraints(guess, colors)
    
    results[word] = tries

sorted_results = dict(sorted(results.items(),
                             key = lambda item: item[1],
                             reverse = True))

f = open('test_search.json', 'w')
f.write(json.dumps(sorted_results, indent = 4))
f.close()

result_dist = dict(Counter(results.values()))
n = len(words)
avg = stats.mean(results.values())
stddev = stats.stdev(results.values())

matplotlib.use('TkAgg')
plt.bar(result_dist.keys(), result_dist.values())
plt.title(f'# Wordle Guesses with Dawg Heuristic (n={n}, avg={avg:.1f}, stddev={stddev:.1f})')
plt.show()