def _2to16(binarynumber):

    digits = '0123456789ABCDEF'
    s = Stack()
    d = Stack()    

    index=0
    decnumber = 0     
    while binarynumber > 0: 
        
        rem=binarynumber%10
        s.push(rem)
        binarynumber=binarynumber/10
        index = index + 1 
    
    while not s.isEmpty():
        index = index - 1
        decnumber = decnumber + s.pop()*(2**index)
       # index = index - 1

    while decnumber > 0:
        kalan = decnumber % 16
        d.push(kalan)
        decnumber = decnumber/16
        
    newnumber = ""
    while not d.isEmpty():
        newnumber=newnumber +digits[d.pop()]
        
    return newnumber
