def parChecker(symbolString):#SYMBOLSTRING "()()(" GİBİ İFADEDİR. 

    s = Stack()#BOŞ YIĞIT

    balanced = True
    index = 0#GÖSTERGE(İNDİSLERİ TUTAR.)

    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():#YIĞIT BOŞSA DENGE "FALSE" OLUR.
                balanced = False
            else:
                top = s.pop()#EN ÜSTTEKİ İNDEKSİ YIĞITTAN ÇEK.
                if not matches(top,symbol):#EN ÜSTTEKİ İNDEKSİ ÇEKTİK,DENGE "FALSE" OLUR.
                       balanced = False

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False
