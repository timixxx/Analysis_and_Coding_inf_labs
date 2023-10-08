import numpy as np


def main_fano(l, h, p):
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
        main_fano(l, k, p)
        main_fano(k + 1, h, p)


codes = dict()


class tree_node:
    def __init__(self, prob, symbol, left=None, right=None):
        self.prob = prob
        self.symbol = symbol
        self.left = left
        self.right = right
        self.code = ''

    def getTree(self):
        mas = [str(self.prob), str(self.symbol), str(self.left), str(self.right), str(self.code)]
        return mas


def codes_calc(node, val=''):
    newVal = val + str(node.code)

    if (node.left):
        codes_calc(node.left, newVal)
    if (node.right):
        codes_calc(node.right, newVal)
    if (not node.left and not node.right):
        codes[node.symbol] = newVal

    return codes


class node:
    def __init__(self) -> None:
        self.sym = ''
        self.pro = 0.0
        self.arr = [0] * 20
        self.top = 0


p = [node() for _ in range(20000)]


def count_ins(data):
    symbols = dict()
    for element in data:
        if symbols.get(element) == None:
            symbols[element] = 1
        else:
            symbols[element] += 1
    return symbols


def probability_calc(n, p):
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


def Output_Encoded(data, coding):
    encoding_output = []
    for c in data:
        #  print(coding[c], end = '')
        encoding_output.append(coding[c])

    string = ''.join([str(item) for item in encoding_output])
    return string


def make_code(n, p):
    Code = []
    for i in range(n - 1, -1, -1):
        test = ''
        for j in range(p[i].top + 1):
            test = test + str(p[i].arr[j])
        Code.append([[p[i].sym, test, p[i].pro]])
    return Code


def tree_decode(data):
    symbol_with_probs = count_ins(data)
    symbols = symbol_with_probs.keys()
    probabilities = symbol_with_probs.values()
    nodes = []

    for symbol in symbols:
        nodes.append(tree_node(symbol_with_probs.get(symbol), symbol))

    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.prob)
        right = nodes[0]
        left = nodes[1]
        left.code = 0
        right.code = 1
        newNode = tree_node(left.prob + right.prob, left.symbol + right.symbol, left, right)
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)

    huffman_encoding = codes_calc(nodes[0])
    new_codes = str(huffman_encoding).replace(", ", ",\n")
    with open("shannon_codes.txt", 'w', encoding='utf-8') as file:
        file.write(new_codes)
    #print(huffman_encoding)
    encoded_output = Output_Encoded(data, huffman_encoding)
    return encoded_output, nodes[0]


def sh_encode(value):
    total = 0
    str = np.array(list(value))
    uniq_elem = np.unique(str, return_counts=True)
    n = len(uniq_elem[0])
    i = 0
    for i in range(n):
        p[i].sym += uniq_elem[0][i]
    probability = uniq_elem[1] / len(str)
    code_sh, tree = tree_decode(value)
    file = open("text_codded_shannon.txt", 'w',
                encoding='utf-8')
    file.write(code_sh)
    for i in range(n):
        p[i].pro = probability[i]
        total = total + p[i].pro
        if total > 1:
            total = total - p[i].pro
            i -= 1

    i += 1
    p[i].pro = 1 - total
    probability_calc(n, p)
    for i in range(n):
        p[i].top = -1
    main_fano(0, n - 1, p)
    code = make_code(n, p)

    return code


def start_encode(value):
    codes_sh = sh_encode(value)
    new_codes = str(codes_sh).replace("],", "]\n")
    #with open("shannon_codes.txt", 'w', encoding='utf-8') as file:
        #file.write(new_codes)
    coded_sh_file = sh_encode_text(value, codes_sh)
    with open("text_coded_shannon.txt", 'w', encoding='utf-8') as file:
        file.write(coded_sh_file)


def sh_encode_text(text, Code):
    coded_text = ""
    for i in text:
        for j in Code:
            if i == j[0][0]:
                coded_text = coded_text + str(j[0][1])
    return coded_text


def sh_decoded(encoded_data, fano_tree):
    tree_head = fano_tree
    decoded_output = []
    for x in encoded_data:
        if x == '1':
            fano_tree = fano_tree.right
        elif x == '0':
            fano_tree = fano_tree.left
        try:
            if fano_tree.left.symbol is None and fano_tree.right.symbol is None:
                pass
        except AttributeError:
            decoded_output.append(fano_tree.symbol)
            fano_tree = tree_head

    string = ''.join([str(item) for item in decoded_output])
    return string
