def lz_encode(inputfile, codedfile):
    file_input = open(inputfile,  'r', encoding='utf-8')
    file_coded = open(codedfile, 'w', encoding='utf-8')
    input_text = file_input.read().lower()

    codes_dict = {input_text[0]: '1'}
    file_coded.write('0' + input_text[0])
    input_text = input_text[1:]
    code_found = ''
    code_num = 2
    for symb in input_text:
        code_found += symb
        if code_found not in codes_dict:
            codes_dict[code_found] = str(code_num)
            if len(code_found) == 1:
                file_coded.write('0' + code_found)
            else:
                file_coded.write(codes_dict[code_found[0:-1]] + code_found[-1])
            code_num += 1
            code_found = ''
    return True


def lz_decode(coded_file, decoded_file):
    coded_file = open(coded_file, 'r', encoding='utf-8')
    decoded_file = open(decoded_file, 'w', encoding='utf-8')
    text_from_file = coded_file.read()
    dict_of_codes = {'0': '', '1': text_from_file[1]}
    decoded_file.write(dict_of_codes['1'])
    text_from_file = text_from_file[2:]
    combination = ''
    code = 2
    for char in text_from_file:
        if char in '1234567890':
            combination += char
        else:
            dict_of_codes[str(code)] = dict_of_codes[combination] + char
            decoded_file.write(dict_of_codes[combination] + char)
            combination = ''
            code += 1
    coded_file.close()
    decoded_file.close()
