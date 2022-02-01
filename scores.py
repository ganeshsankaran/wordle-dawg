# calculate word scores

import json

words = open('words.txt', 'r').read().split()
freqs = json.loads(open('freqs.json', 'r').read())

scores = {}

# calculate word scores
# multiply frequencies
for word in words:
    score = 1
    for pos in range(5):
        score *= freqs[str(pos)][word[pos]]
    scores[word] = score

# sort word scores
scores = dict(sorted(scores.items(), 
                     key = lambda item: item[1], 
                     reverse = True))
    
f = open('scores.json', 'w')
f.write(json.dumps(scores, indent = 4))
f.close()