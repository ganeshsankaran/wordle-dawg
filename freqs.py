# calculate letter frequencies

from collections import Counter
import json

words = open('words.txt', 'r').read().split()

first_chars = [word[0] for word in words]
second_chars = [word[1] for word in words]
third_chars = [word[2] for word in words]
fourth_chars = [word[3] for word in words]
fifth_chars = [word[4] for word in words]

# aggregate chars by count
first_char_dist = Counter(first_chars)
second_char_dist = Counter(second_chars)
third_char_dist = Counter(third_chars)
fourth_char_dist = Counter(fourth_chars)
fifth_char_dist = Counter(fifth_chars)

pos_to_char_dist = {
    0: first_char_dist,
    1: second_char_dist,
    2: third_char_dist,
    3: fourth_char_dist,
    4: fifth_char_dist
}

freqs = {}
for pos in pos_to_char_dist:
    freqs[pos] = {}

for pos, dist in pos_to_char_dist.items():
    for char, freq in dist.items():
        freqs[pos][char] = freq

f = open('freqs.json', 'w')
f.write(json.dumps(freqs, indent = 4))
f.close()