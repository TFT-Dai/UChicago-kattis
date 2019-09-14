#https://uchicago.kattis.com/problems/uchicago.rpn

def postfix_calculator(token):
    int_op = ["+", "*", "=="]
    bool_op = ["and", "or"]
    boolean = ["true", "false"]
    stack = []
    ptr = 0
    while ptr < len(token):
        if token[ptr].isdigit() or token[ptr] in boolean:
            stack.append(token[ptr])
            ptr += 1
        else:
            if len(stack) < 2:
                return "SYNTAX ERROR"
            v1 = stack.pop()
            v2 = stack.pop()
            if (v1.isdigit() and v2 in boolean) or (v1 in boolean and v2.isdigit()):
                return "TYPE ERROR"
            if token[ptr] in int_op and v1 in boolean and v2 in boolean:
                return "TYPE ERROR"
            if token[ptr] in bool_op and v1.isdigit() and v2.isdigit():
                return "TYPE ERROR"
            ep = [v1.title(), token[ptr], v2.title()]
            tmp = str(eval(" ".join(ep))).lower()
            stack.append(tmp)
            ptr += 1

    if len(stack) != 1:
        return "SYNTAX ERROR"
    return stack[0]

Token = list(input().split())
print(postfix_calculator(Token))
