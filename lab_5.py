ind = [1, 2, 4, 8]


def prohodka(data: list):
    bit_data = [data,
                [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0],
                [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]]
    for i in range(1, 5):
        print(bit_data[i], end=' ')
        count = 0
        for j in range(12):
            el = bit_data[i][j]
            count += data[j] * bit_data[i][j]
        if i == 1:
            data[0] = count % 2
            print(f"r{i} = {data[0]}")
        elif i == 2:
            data[1] = count % 2
            print(f"r{i} = {data[1]}")
        elif i == 3:
            data[3] = count % 2
            print(f"r{i} = {data[3]}")
        elif i == 4:
            data[7] = count % 2
            print(f"r{i} = {data[7]}")

    return data

def encode(data: int):
    data = [int(a) for a in str(data)]
    print(f"{data} - Изначальное состояние")
    for i in ind:
        data.insert(i - 1, 0)
    print(f"{data} - Добавление контрольных бит")
    print('Заполняем контрольные биты... \n{0}\n'.format(data))
    data = prohodka(data)

    print(f"\n{data} - Заполнение контрольных бит")
    c = 3
    data[c] = 0 if data[c] else 1
    print(f"{data} Добавляем ошибку. Ошибка на позиции {c+1}\n")

    return data


def decode(data: list):
    for_check = [data[0], data[1], data[3], data[7]]
    data1 = list(data)
    data = prohodka(data)

    for_final = [data[0], data[1], data[3], data[7]]
    sum = dict(zip(ind, for_final))
    m_ind = 0
    for el in sum:
        m_ind += el if sum[el] else 0
    print(f"Ошибка в позиции № {m_ind}")
    m_ind -= 1
    data1[m_ind] = 0 if data[m_ind] else 1
    print(data1)
    data1.pop(0)
    data1.pop(0)
    data1.pop(1)
    data1.pop(4)
    print(f"{data1} - Конечный вариант")


data = encode(10001111)
decode(data)
