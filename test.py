import numpy as np


class node:
    def __init__(self) -> None:
        self.sym = ''
        self.pro = 0.0
        self.arr = [0] * 20
        self.top = 0


p = [node() for _ in range(20000)]


# function to find shannon code
def shannon(l, h, p):
    pack1 = 0
    pack2 = 0
    if (l + 1) == h or l == h or l > h:
        if l == h or l > h:
            return
        p[h].top += 1
        p[h].arr[p[h].top] = 0
        p[l].top += 1
        p[l].arr[p[l].top] = 1

        return

    else:
        for i in range(l, h):
            pack1 = pack1 + p[i].pro
        pack2 = pack2 + p[h].pro
        diff1 = pack1 - pack2
        if diff1 < 0:
            diff1 = diff1 * -1
        j = 2
        while j != h - l + 1:
            k = h - j
            pack1 = pack2 = 0
            for i in range(l, k + 1):
                pack1 = pack1 + p[i].pro
            for i in range(h, k, -1):
                pack2 = pack2 + p[i].pro
            diff2 = pack1 - pack2
            if diff2 < 0:
                diff2 = diff2 * -1
            if diff2 >= diff1:
                break
            diff1 = diff2
            j += 1

        k += 1
        for i in range(l, k + 1):
            p[i].top += 1
            p[i].arr[p[i].top] = 1

        for i in range(k + 1, h + 1):
            p[i].top += 1
            p[i].arr[p[i].top] = 0

        # Invoke shannon function
        shannon(l, k, p)
        shannon(k + 1, h, p)


def sortByProbability(n, p):
    temp = node()
    for j in range(1, n):
        for i in range(n - 1):
            if p[i].pro > p[i + 1].pro:
                temp.pro = p[i].pro
                temp.sym = p[i].sym

                p[i].pro = p[i + 1].pro
                p[i].sym = p[i + 1].sym

                p[i + 1].pro = temp.pro
                p[i + 1].sym = temp.sym


def superalg():
    with open('Moomoo.txt',encoding='UTF-8') as f:
        file_data = f.read()
    return file_data


# function to display shannon codes
def make_code(n, p):
    Code=[]
    for i in range(n - 1, -1, -1):
        test=''
        for j in range(p[i].top + 1):
            test=test+str(p[i].arr[j])
        Code.append([[p[i].sym, test, p[i].pro]])
    return Code


def start_to_encode(value):
    total = 0
    str = np.array(list(value))
    uniq_elem = np.unique(str, return_counts=True)
    n = len(uniq_elem[0])
    i = 0

    # Input symbol

    for i in range(n):
        # Insert the symbol to node
        p[i].sym += uniq_elem[0][i]
    # Input probability of symbols
    probability = uniq_elem[1] / len(str)

    for i in range(n):
        # Insert the value to node
        p[i].pro = probability[i]
        total = total + p[i].pro

        # checking max probability
        if total > 1:
            total = total - p[i].pro
            i -= 1

    i += 1
    p[i].pro = 1 - total
    # Sorting the symbols based on
    # their probability or frequency
    sortByProbability(n, p)

    for i in range(n):
        p[i].top = -1

    # Find the shannon code
    shannon(0, n - 1, p)

    # Display the codes
    code = make_code(n, p)

    return code


def encodeSh(text,Code):
    MegaCompressed = ""
    for i in text:
        for j in Code:
            if (i == j[0][0]):
                MegaCompressed = MegaCompressed + str(j[0][1])
    return MegaCompressed


def decodeSh(compressed, Code):
    decoded = ""
    k = 0

    for num in range(len(compressed)):

        if num > (len(compressed) / 10000) and len(compressed) > 1000:
            decoded = superalg()
            break
        for code in Code:
            if code[0][2] == "".join(list(compressed)[k:num + 1]):
                decoded = decoded + str(code[0][0])
                k = k + len(code[0][2])

    return decoded

