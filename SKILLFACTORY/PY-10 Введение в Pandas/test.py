import numpy as np

def get_unique_loto(num):
    res = list()
    for i in range(num):
        res.append(np.random.choice(101, replace=False, size=(5, 5)))
    res = np.array(res)
    return res
print(get_unique_loto(3))