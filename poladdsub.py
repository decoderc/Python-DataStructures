class Poly:

    def __init__(self,liste1):
        self.one=liste1


    def __add__(self, off):
        a=''

        
        if len(self.one)>len(off.one):
            b=len(self.one)
            c=len(off.one)
            g=b-c
            
            while g>0:
                print g

                off.one.append(0)
                g-=1
                i=0
                while b>0:
                    toplam=self.one[i]+off.one[i]
                    h=list(str(toplam))
                    n=len(h)-1
                    b-=1
                    
                
        else:
            b=len(off.one)
            c=len(self.one)
            g=b-c
            while g>0:
                print g
                self.one.append(0)
                g-=1
                
            
        
         
            

          
        for i in range(0,len(h)):
            n=len(h)-1

            print str(h[i])+'x^'+str(n)+ ' +',
            n=n-1

    def __sub__(self,off):
        a=''
        for i in range(len(self.one)):
            fark=self.one[i]-off.one[i]
            a=a+str(fark)
            n=len(a)-1 
        for i in range(0,len(a)):
            print str(a[i])+'x^'+str(n)+ ' -',
            n=n-1
