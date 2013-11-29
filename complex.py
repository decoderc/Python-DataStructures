
#!/usr/bin/python
# -*- coding: utf-8 -*-

class Kompleks:
    
    def __init__(self,reel,sanal):
        self.re=reel
        self.imj=sanal
    
    def __str__(self):
        return str(self.re)+str(self.imj)+"i"
    
    def show(self):
		print self.re,self.imj,"i"
		
	#def __add__(self,other):
	#	newre=self.re+other.re
	#	newimj=self.imj+other.imj
		
#test demo
mycomplex= Kompleks(2,5) 
