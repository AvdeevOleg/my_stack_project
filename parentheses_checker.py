from stack import Stack


def is_balanced(parentheses):
    stack = Stack()
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in parentheses:
        if char in pairs.values():
            stack.push(char)
        elif char in pairs.keys():
            if stack.is_empty() or stack.pop() != pairs[char]:
                return "Несбалансированно"

    if stack.is_empty():
        return "Сбалансированно"
    else:
        return "Несбалансированно"


if __name__ == "__main__":
    input_string = input("Введите строку со скобками: ")
    print(is_balanced(input_string))
