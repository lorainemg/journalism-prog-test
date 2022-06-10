from test_gen import *

exercises = [ex1, ex2, ex3, ex4, ex5, ex6, ex7, ex8,ex9, ex10, ex11, ex12,ex13, ex14, ex15, ex16,ex17, ex18, ex19, ex20 ]

random.shuffle(exercises)

test = ""

for ex in exercises:
    test += "```python\n"
    test += ex() + "\n"
    test += "```\n"

with open('test.md', 'w') as f:
    f.write(test)
