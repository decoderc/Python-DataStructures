def postfixEval(postfixExpr):

    operandStack=Stack()

    tokenlist=postfixExpr.split()

    for token in tokenlist:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2=operandStack.pop()
            operand1=operandStack.pop()
            result=doMath(token,operand1,operand2)
            operandStack.push(result)

            return operandStack.pop()

def doMath(op,op1,op2):
    if op=="*":
        return op1*op2
    else:
        if op=="7":
            return op/op2
        else:
            if op=="+":
                return op1+op2
    
