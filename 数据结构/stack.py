class Stack:
    def __init__(self):
        self.stack = []

    def stack_push(self, a):
        self.stack.append(a)

    def stack_pop(self):
        self.stack.pop()

    def get_top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def __str__(self):
        return str(self.stack)

def brace_match(str):
    stack = Stack()
    match = {'(' : ')', '[' : ']', '{' : '}'}
    for a in str:
        if a == '(' or a == '[' or a == '{':
            stack.stack_push(a)
        else:
            if stack.get_top() != None and a in match[stack.get_top()]:
                stack.stack_pop()
            else :
                return False
    return True

print(brace_match("[{]}"))