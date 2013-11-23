class Poly:

    def __init__(self,liste1):
        self.one=liste1
    def __add__(self, off):
        if len(self.one)>len(off.one) or len(off.one)>len(self.one):
            if len(self.one)>len(off.one):
                while len(self.one)>=len(off.one):                    
                    off.one.append(0)                   
            else:
                while len(off.one)>len(self.one):
                    self.one.append(0)                   
                 
        t=0
        b=len(self.one)
        a=list(self.one)
        while b>t:
            toplam= self.one[t]+off.one[t]            
            a[t]=toplam
            t=t+1            
                
        n=len(a)-1 
        for i in range(0,len(a)):
            print str(a[i])+'x^'+str(n)+ ' +',
            n=n-1

    def __mul__(self,off):
        if len(self.one)>len(off.one) or len(off.one)>len(self.one):
            if len(self.one)>len(off.one):
                while len(self.one)>=len(off.one):                    
                    off.one.append(0)                   
            else:
                while len(off.one)>len(self.one):
                    self.one.append(0)                   
                 
        t=0
        b=len(self.one)
        a=list(self.one)
        while b>t:
            toplam= self.one[t]*off.one[t]            
            a[t]=toplam
            t=t+1       
                
        n=len(a)-1
        t=0
        
        while len(a)>t:
            if a[t]==0:
                del a[t]
                t=t-1
            else:
                t=t+1
                               
        for i in range(0,len(a)):
            
            print str(a[i])+'x^'+str(n)+ ' +',
            n=n-1
            
    def __div__(self,off):
        r=len(off.one)
        if len(self.one)>len(off.one) or len(off.one)>len(self.one):
            if len(self.one)>len(off.one):
                while len(self.one)>=len(off.one):                    
                    off.one.append(0)
        else:
            while len(off.one)>len(self.one):
                self.one.append(0)
        
         
        
        
        t=0
        p=len(off.one)
        d=off.one
        n=len(self.one)-1
        m=len(off.one)-1
        while len(self.one)>r:
            while p>0:
                c=self.one[t]/off.one[t]
                off.one[t]=c*off.one[t]
                p-=1
                
                self.one[t]=self.one[t]-off.one[t]
                
                if self.one[t]==0:
                    del self.one[t]
                else:
                    t+=1
                    
                
            
            
            
            
