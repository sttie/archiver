from classes import *

def create_bin_codes(main_node, bin_codes, code):
    if main_node.left_child is not None:
        code.append("0")

        if len(main_node.left_child.letter) == 1:
            bin_codes[main_node.left_child.letter] = "".join(code)
            code.pop()
        else:
            create_bin_codes(main_node.left_child, bin_codes, code)
            code.pop()

    if main_node.right_child is not None:
        code.append("1")

        if len(main_node.right_child.letter) == 1:
            bin_codes[main_node.right_child.letter] = "".join(code)
            code.pop()
        else:
            create_bin_codes(main_node.right_child, bin_codes, code)
            code.pop()


def make_tree(source, encoding="ascii"):
    freq = None
    if encoding == "ascii": freq = [0] * 128
    # TODO: utf-8 support
    elif encoding == "utf-8": pass

    main_queue = PriorQueue()

    for i in source:
        freq[ord(i)] += 1

    for i in range(len(freq)):
        if freq[i] == 0: continue
        main_queue.insert(Node(chr(i), freq[i]))

    for i in range(len(main_queue) - 1):
        first_node = main_queue.remove()
        second_node = main_queue.remove()

        new_parent = Node(first_node.letter + second_node.letter,
                            first_node.frequency + second_node.frequency,
                                first_node, second_node)

        main_queue.insert(new_parent)

    return main_queue.remove()


source = input()
tree = make_tree(source)

bin_codes = {}
code = []
create_bin_codes(tree, bin_codes, code)
del tree, code

for i in source:
    print(bin_codes[i], end="")
print()

# еще поэксперементируй с void* в Си
