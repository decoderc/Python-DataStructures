def dengeli_mi(sembol):
    s=Stack()
    denge=True
    indeks=0
    while indeks<len(sembol) and denge:
        str=sembol[indeks]
        if str in "([{":
            s.push(str)
        else:
            if s.isEmpty():
                denge=False
            else:
                top=s.pop()
                if not matches(top,str):
                       denge=False
        indeks=indeks+1
    
        if denge and s.isEmpty():
            return True
        else:
            return False

def matches(acik,kapali):
    aciklar="([{"
    kapalilar=")]}"
    return aciklar.indeks(acik)==kapali.indeks(kapali)
            
