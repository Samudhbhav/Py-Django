# Program to find total number of letters used if all numbers from 1 to 100 were written in words (excluding spaces or hyphens)

import time
start = time.time()
S = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
D = [0,3,6,6,5,5,5,7,6,6]
H = 7
total = 0
for i in range(1,100):
    b = i % 10 # singles digit
    a = ((i % 100) - b) / 10 # tens digit
    if a == 0 or a == 1: total += S[a * 10 + b] # Total from one to nineteen
    else: total += D[a] + S[b]            # Total from twenty to ninety nine 
total += S[1] + H # Adding one hundred to total
elapsed = time.time() - start
print "%s found in %s seconds" % (total,elapsed)  # Finding Elapsed time
