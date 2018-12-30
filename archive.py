from binary_tree import TreeNode

def two_minimal_numbers_array(array):
    first_min = second_min = None
    maximum = max(array)

    # Первое минимальное значение
    for index, number in enumerate(array):
        if number <= maximum:
            maximum = number
            first_min = (number, index)
    
    maximum = max(array)
    # Второе минимальное значение, пропуская первое найденное
    for index, number in enumerate(array):
        if index != first_min[1]:
            if number <= maximum:
                maximum = number
                second_min = (number, index)

    # Возвращаем кортеж вида ((m1, i1), (m2, i2)), где mn - n-ое минимальное значение, in - его индекс
    return first_min, second_min

def create_bin_codes(main_node, bin_codes, code):
    if main_node.left_child is not None:
        # Идем влево - к символу добавляется 0
        code.append("0")
        # Если левый ребенок - символ, то добавляем ее и ее код в bin_codes
        if isinstance(main_node.left_child, str):
            bin_codes[main_node.left_child] = "".join(code)
            # Идем обратно - убираем последнюю цифру code
            code.pop()
        # Если нет - рекурсивно вызываем функцию с новым main_node
        else:
            create_bin_codes(main_node.left_child, bin_codes, code)
            # Идем обратно - убираем последнюю цифру code
            code.pop()
    if main_node.right_child is not None:
        # Идем вправо - к символу добавляется 1
        code.append("1")
        # Если правый ребенок - символ, то добавляем ее и ее код в bin_codes
        if isinstance(main_node.right_child, str):
            bin_codes[main_node.right_child] = "".join(code)
            # Идем обратно - убираем последнюю цифру code
            code.pop()
        # Если нет - рекурсивно вызываем функцию с новым main_node
        else:
            create_bin_codes(main_node.right_child, bin_codes, code)
            # Идем обратно - убираем последнюю цифру code
            code.pop()

source = """This is mostly to make sure my methodology is correct, but my basic question was is it worth it to check outside of a function if I need to access the function at all. I know, I know, premature optimization, but in many cases, its the difference between putting an if statement inside the function call to determine whether I need to run the rest of the code, or putting it before the function call. In other words, it takes no effort to do it one way or the other. Right now, all the checks are mixed between both, and I'd like the get it all nice and standardized.
            The main reason I asked is because the other answers I saw mostly referenced timeit, but that gave me negative numbers, so I switched to this:"""
# Словарь частот
letters = {}
# Отдельный список с частотой каждого символа
frequency = []
# Он нужен, так как в дальнейшем в словаре будут появляться значения
# класса TreeNode, которые не могут сравниваться с числами

# Заполнение словаря частот
for i in source:
    if not letters.get(i):
        letters[i] = 0
    letters[i] = letters[i] + 1

# Заполнение списка частот
for i in letters:
    frequency.append(letters[i])

# Проходимся по списку, оставляя в итоге 1 элемент
for i in range(len(letters)-1):
    # Возвращает кортеж вида ((m1, i1), (m2, i2)), где mn - n-ое минимальное значение, in - его индекс
    minimals = two_minimal_numbers_array(frequency)

    # Ключ первого минимального значения
    key_first = list(letters.keys())[minimals[0][1]]
    # Ключ второго минимального значения
    key_second = list(letters.keys())[minimals[1][1]]
    # Для того, чтобы вставлять в value каждого TreeNode
    node_key = key_first + key_second

    # Удаляем старые значения
    frequency.remove(minimals[0][0])
    frequency.remove(minimals[1][0])
    # Складываем значения и вставляем их на последнее место
    frequency.append(minimals[0][0] + minimals[1][0])

    # Здесь выполняется проверка, чтобы в потомках TreeNode не записывались сами строки,
    # длина которых > 1, а узлы, у которых value = этим строкам
    if len(key_first) > 1 and len(key_second) > 1:
        letters[node_key] = TreeNode(0, node_key, letters[key_first], letters[key_second])
    elif len(key_first) > 1:
        letters[node_key] = TreeNode(0, node_key, letters[key_first], key_second)
    elif len(key_second) > 1:
        letters[node_key] = TreeNode(0, node_key, key_first, letters[key_second])
    else:
        letters[node_key] = TreeNode(0, node_key, key_first, key_second)

    # Удаляем использованные элементы
    letters.pop(key_first)
    letters.pop(key_second)

# Берем значение первого (и единственного) элемента
final_tree = letters[next(iter(letters))]

del frequency, letters

# bin_codes - словарь, который содержит бинарный код для каждого символа
bin_codes = {}
# Переменная, содержащая бинарный код, в зависимости от движения по дереву
code = []

# Вызываем функцию обхода дерева с присвоением бинарного кода символам
create_bin_codes(final_tree, bin_codes, code)

del final_tree, code

# Кодирование строки
final_bin_string = ""
for letter in source:
    final_bin_string += bin_codes[letter]
    
# print(bin_codes)


def _to_Bytes(data):
    b = bytearray()
    for i in range(0, len(data), 8):
        b.append(int(data[i:i+8], 2))
        print(b)
    return bytes(b)

# Дальше - bin_codes в файл с помощью pickle, а final_bin_string в другой

# f = open("test.bin", "wb")
# f.write(_to_Bytes(final_bin_string))
# f.close()