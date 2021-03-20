import numpy as np
import random


def degree_sequence_checker(a: list) -> bool:
    a = np.asarray(a)
    if a[a % 2 == 1].size % 2:
        return False
    while True:
        a[::-1].sort()
        if a[a == 0].size == a.size:
            return True
        if a[0] < 0 or a[0] >= a.size or a[a < 0].size > 0:
            return False
        for (i,), el in np.ndenumerate(a):
            if 0 < i <= a[0]:
                a[i] = el - 1
        a[0] = 0


exampleCorrect = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]
exampleCorrectFromLecture1 = [6, 4, 3, 2, 2, 2, 1, 1]
exampleCorrectFromLecture2 = [6, 5, 4, 3, 2, 1, 1]
exampleCorrectFromLecture3 = [6, 4, 3, 3, 2, 2, 2]
exampleCorrectFromLecture0 = [4, 2, 3, 2, 3, 2]
exampleWrong = [4, 4, 3, 3, 1, 2]
print(degree_sequence_checker(exampleCorrectFromLecture3))
