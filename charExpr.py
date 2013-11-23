def chkExpr(expr):
    opens='[('
    close='])'

    tokenList=expr.split()
    parStack=Stack()

    for token in tokenList:
        if token in opens:
            parStack.push(token)
        elif token in close:
                if parStack.isEmpty():
                    return False
                erc=opens.index(parStack.pop())
                if token!=close[erc]:
                    return False
                if parStack.isEmpty():
                    return True
                else:
                    return False
            
