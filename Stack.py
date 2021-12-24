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

    def mb_balanced(self):
        cache = []
        crutch = {')': '(', '}': '{', ']': '['}
        while self.is_empty() != True:
            if  self.peek() in crutch and crutch[self.peek()] not in cache:
                return ("Несбалансированно")
            elif self.peek() in crutch and crutch[self.peek()] in cache:
                cache.remove(crutch[self.pop()])
            else:
                cache.append(self.pop())
        return ("Сбалансированно")



str_1 = "}{}{[]"
my_list = []
cache_2 = []

for item in str_1:
    my_list.append(item)

str_stack = Stack(my_list)
print(str_stack.mb_balanced())


