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


names=["A","B","C","D","E"]
def DuckDuckGoose(names,k):
    position = k-1
    index =0
    list_len=len(names)
    while list_len>1 :
        index=(position+index)% list_len
        print(names.pop(index))
        list_len -=1



if __name__ =="__main__":

    pass
