from binary_tree import TreeNode


# Finding two minimal numbers from an array
def two_minimal_numbers_array(array):
    first_min = second_min = None
    maximum = max(array)

    # First minimal value
    for index, number in enumerate(array):
        if number <= maximum:
            maximum = number
            first_min = (number, index)
    
    maximum = max(array)
    # Second minimal value
    for index, number in enumerate(array):
        if index != first_min[1]:
            if number <= maximum:
                maximum = number
                second_min = (number, index)

    return first_min, second_min


# Creating binary code for every symbol 
def create_bin_codes(main_node, bin_codes, code):
    if main_node.left_child is not None:
        # If we turn left, "0" is added to current bin code
        code.append("0")
        # If the left child is a symbol, we add it and its code into bin_codes
        if isinstance(main_node.left_child, str):
            bin_codes[main_node.left_child] = "".join(code)
            # If we go back, we delete the last code's number
            code.pop()
        # If not - we recursively call the function with new main_node
        else:
            create_bin_codes(main_node.left_child, bin_codes, code)
            # If we go back, we delete the last code's number
            code.pop()
    if main_node.right_child is not None:
        # If we turn right, "0" is added to current bin code
        code.append("1")
        # If the left child is a symbol, we add it and its code into bin_codes
        if isinstance(main_node.right_child, str):
            bin_codes[main_node.right_child] = "".join(code)
            # If we go back, we delete the last code's number
            code.pop()
        # If not - we recursively call the function with new main_node
        else:
            create_bin_codes(main_node.right_child, bin_codes, code)
            # If we go back, we delete the last code's number
            code.pop()

source = input()

# Frequency dict
letters = {}
# A list with every symbol's frequency 
frequency = []
# We need it, because later we will have letters keys of TreeNode class
# that can't be compared with ints


# Filling the frequency dict
for i in source:
    if not letters.get(i):
        letters[i] = 0
    letters[i] = letters[i] + 1

# Filling the frequency list
for i in letters:
    frequency.append(letters[i])

# Проходимся по списку, оставляя в итоге 1 элемент
for i in range(len(letters)-1):
    # Returns a ((m1, i1), (m2, i2)) tuple, where mn - minimal value, in - its index
    minimals = two_minimal_numbers_array(frequency)

    # First element's minimal value
    key_first = list(letters.keys())[minimals[0][1]]
    # Second element's minimal value
    key_second = list(letters.keys())[minimals[1][1]]
    # For every TreeNode's value
    node_key = key_first + key_second

    # Deleting old values
    frequency.remove(minimals[0][0])
    frequency.remove(minimals[1][0])
    # Adding values and inserting them in the end
    frequency.append(minimals[0][0] + minimals[1][0])

    if len(key_first) > 1 and len(key_second) > 1:
        letters[node_key] = TreeNode(0, node_key, letters[key_first], letters[key_second])
    elif len(key_first) > 1:
        letters[node_key] = TreeNode(0, node_key, letters[key_first], key_second)
    elif len(key_second) > 1:
        letters[node_key] = TreeNode(0, node_key, key_first, letters[key_second])
    else:
        letters[node_key] = TreeNode(0, node_key, key_first, key_second)

    # Deleting used elements
    letters.pop(key_first)
    letters.pop(key_second)

# First element's value
final_tree = letters[next(iter(letters))]

del frequency, letters

# This dict contains bin code for every symbol
bin_codes = {}
# This variable contains bin code for current symbol in the create_bin_codes function
code = []

# Calling the function with tree traversal
create_bin_codes(final_tree, bin_codes, code)

del final_tree, code

# String encoding
final_bin_string = ""
for letter in source:
    final_bin_string += bin_codes[letter]
    
# print(bin_codes)
