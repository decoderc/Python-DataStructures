class kompleks:
    def __init__(self,reel,imj):
        self.reel=reel
        self.imj=imj
    def __str__(self):
        if  self.reel>0 and self.imj>0:
            return str(self.reel)+"+"+str(self.imj)+"i"
        elif self.reel<0 and self.imj<0:
            return str(self.reel)+str(self.imj)+"i"
        elif self.imj<0 and self.reel>0:
            return str(self.reel)+str(self.imj)+"i"
        elif self.reel<0 and self.imj>0:
            return str(self.reel)+"+"+str(self.imj)+"i"
        elif self.reel==0 and self.imj!=0:
            return str(self.imj)+"i"
        elif self.reel!=0 and self.imj==0:
            return str(self.reel)
        else:
            return "0+0i"
    def __add__(self,other):
        newreel=self.reel+other.reel
        newimj= self.imj+other.imj
        return kompleks(newreel,newimj)
    def __cikar__(self,other):
        newreel=self.reel-other.reel
        newimj= self.imj-other.imj
        return kompleks(newreel,newimj)
    def __carp__(self,other):
        newreel=self.reel*other.reel+self.imj*other.imj*(-1)
        newimj= self.reel*other.imj+self.imj*other.reel
        return kompleks(newreel,newimj)
    def __bol__(self,other):
        newreel=(self.reel*other.reel+self.imj*other.imj)/((other.reel**2)+(other.imj**2))
        newimj=(other.reel*self.imj-self.reel*other.imj)/((other.reel**2)+(other.imj**2))
        return kompleks(newreel,newimj)
    """ NOT: programin tek eksigi; bolme isleminde kesirleri algılamıyor,
       yani integer degerler uzerinden calisiyor"""
