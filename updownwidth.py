import random as rd
# randint 사용하여 +- 5% 등락 폭 조정
def rdlist():
    fruits = 100 * rd.randint(-5, 5)
    foods = 500 * rd.randint(-5, 5)
    cutlery = 800 * rd.randint(-5, 5)
    game = 1000 * rd.randint(-5, 5)
    return fruits, foods, cutlery, game