class Stack:
    def __init__(self, values: list):
        self.values = values

    def is_empty(self):
        if len(self.values) == 0:
            return True
        else:
            return False

    def push(self, item):
        self.values.insert(0, item)

    def pop(self):
        if len(self.values) == 0:
            print("Empty Stack")
        else:
            cash = self.values[0]
            self.values.pop(0)
            return cash

    def peek(self):
        if len(self.values) == 0:
            print("Empty Stack")
            return None
        else:
            return self.values[0]

    def size(self):
        return len(self.values)



str_1 = "(((([{}]))))"

def mb_balanced(my_str):
    my_list = []

    for item in my_str:
        my_list.append(item)

    my_stEck = Stack(my_list)

    if my_stEck.values.count("(") == my_stEck.values.count(")"):
        if my_stEck.values.count("{") == my_stEck.values.count("}"):
            if my_stEck.values.count("[") == my_stEck.values.count("]"):
                print("Сбалансированно")
            else:
                print("Несбалансированно")
        else:
            print("Несбалансированно")
    else:
        print("Несбалансированно")

mb_balanced(str_1)
