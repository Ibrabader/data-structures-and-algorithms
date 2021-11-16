def checker(symbol):
    stack = []
    i=0
    while  i < len (symbol):
        if symbol[i] in ["(", "{", "["]:
            stack.append(symbol[i])
        elif symbol[i] in [")", "}", "]"]:
            if len(stack) ==0:
                return False
            item = stack.pop()
            if item == '(':
                if symbol[i] != ")":
                    return False
            if item == '{':
                if symbol[i] != "}":
                    return False
            if item == '[':
                if symbol[i] != "]":
                    return False
        i+=1
    return True

# if __name__ =="__main__"
