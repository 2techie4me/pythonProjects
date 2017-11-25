# Silly sentences 
import time
name = ['Cerys', 'Owen', 'Jack', 'Iris', 'Lynda']
verb = ['buys', 'rides', 'fights', 'eats', 'astroturfs', 'sells']
noun = ['lion', 'bicycle', 'plane', ]
from random import randint
def pick(words):
    num_words = len(words)
    num_picked = randint(0, num_words - 1)
    word_picked = words[num_picked]
    return word_picked
while True:
    print(pick(name), pick(verb), 'a', pick(noun), end='.\n')
    time.sleep(3)
    #
    #input()
