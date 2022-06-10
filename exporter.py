from test_gen import *

exercises = [ex1, ex2, ex3, ex4, ex5, ex6, ex7, ex8,ex9, ex10, ex11, ex12,ex13, ex14, ex15, ex16,ex17, ex18, ex19, ex20 ]


def create_test(i: int):
    random.shuffle(exercises)
    test = ""
    for j, ex in enumerate(exercises, 1):
        test += f"{j}) "
        test += ex() + "\n\n"
        # test += "```\n\n"
        
    with open(f'tests/test_{i}.txt', 'w') as f:
        f.write(test)
        
def create_tests(n: int):
    for i in range(n):
        create_test(i)
        
if __name__ == '__main__':
    create_tests(60)

