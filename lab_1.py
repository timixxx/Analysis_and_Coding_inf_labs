import lz78
import sh_fano
import numpy as np
from PIL import Image


def code():
    file = input("Enter the filename:")
    my_string = np.asarray(Image.open(file), np.uint8)
    print("Enetered string is:", my_string)

    lz78.lz_encode('Moomoo.txt', 'text_coded.txt')
    lz_coded_file = open('text_coded.txt', 'r', encoding='utf-8')
    lz_coded = lz_coded_file.read().lower()
    sh_fano.start_encode(lz_coded)


def decode():
    for_tree = open('text_coded.txt', 'r', encoding='utf-8')
    tree_c = for_tree.read().lower()
    code_sh, tree = sh_fano.tree_decode(tree_c)
    f2 = open("text_codded_shannon.txt", 'r', encoding='utf-8')
    data_coded = f2.read()
    decoded = sh_fano.sh_decoded(data_coded, tree)
    with open("text_decoded_shannon.txt", 'w', encoding='utf-8') as file:
        file.write(decoded)
    lz78.lz_decode('text_decoded_shannon.txt', 'text_decoded.txt')


if __name__ == '__main__':
    code()
    #decode()
