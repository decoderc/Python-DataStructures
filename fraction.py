class fraction:
    
    def __init__(self,top,bottom):
        self.num=top
        self.den=bottom
    
    def __str__(self):
        return str(self.num)+"/"+str(self.den)
    
    def show(self):
        print self.num,"/",self.den
    
    def __add__(self,otherfraction):
         newnum=self.num*otherfraction.den+self.den*otherfraction.num
         newden=self.den*otherfraction.den
         common=god(newnum,newden)
         return fraction(newnum/common,newden/common)
    
    def __sub__(self,otherfraction):
        newnum=self.num*otherfraction.den-self.den*otherfraction.num
        newden=self.den*otherfraction.den
        common=god(newnum,newden)
        return fraction(newnum/common,newden/common)
    
    def __mul__(self,otherfraction):
        newnum=self.num*otherfraction.num
        newden=self.den*otherfraction.den
        common=god(newnum,newden)
        return fraction(newnum/common,newden/common)
    
    def __div__(self,otherfraction):
        newnum=self.num*otherfraction.den
        newden=self.den*otherfraction.num
        common=god(newnum,newden)
        return fraction(newnum/common,newden/common)
    
    def __cmp__(self,otherfraction):
        num1=self.num*otherfraction.den
        num2=self.den*otherfraction.num
        if num1 < num2:
           return -1
        else:
            if num1==num2:
           return 0
        else:
           return 1
    
    def __pow__(self,sayi):
        newnum=self.num**sayi
        newden=self.den**sayi
        common=god(newnum,newden)
        return fraction(newnum/common,newden/common)
