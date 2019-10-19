class PriorQueue:
    def __init__(self):
        self.queue = []
        self.size = 0

    def insert(self, element):
        # если очередь пуста, просто вставляем элемент
        if self.size == 0:
            self.queue.append(element)
            self.size += 1
            return

        # иначе вставляем в очередь, ключ - частота
        for i in range(self.size):
            if self.queue[i].frequency > element.frequency:
                self.queue.insert(i, element)
                break

            if i == self.size - 1:
                self.queue.insert(i + 1, element)

        self.size += 1

    def remove(self):
        self.size -= 1
        return self.queue.pop(0)


    def __repr__(self):
        return "{}".format(self.queue)

    def __len__(self):
        return self.size


class Node:
    def __init__(self, letter, frequency, first_child=None, second_child=None):
        self.letter = letter
        self.frequency = frequency
        self.left_child = None
        self.right_child = None

        if first_child == None or second_child == None: return

        if first_child.frequency <= second_child.frequency:
            self.left_child = first_child
            self.right_child = second_child
        else:
            self.right_child = first_child
            self.left_child = second_child

    def __repr__(self):
        return "({0}, {1})".format(self.letter, self.frequency)
