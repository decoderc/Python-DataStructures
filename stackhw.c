class Stack:
    def __init__(self,n):
        self.sinir=n
        self.items=[]

    def isEmpty(self):
        return self.items == []

    def push(self,item):
       
        if len(self.items)+1<self.sinir:
        
            self.items.append(item)
        else:
            print "limit doldu lutfen baska sayi girmeyiniz"
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

        


def ay(n):
    s = Stack(n)    
    key=''
    unkey=''
    balanced = True
    k=True
    index = 0
    infile=open("index.html.txt",'r')
    text=infile.read()
    infile.close()    
    a=[]
    
    try:
    
        while index<len(text):        
            if text[index]=="":
                break
        
            elif text[index] =='<'  and text[index+1]!='/':
                key=''            
                while text[index]!='>':          
                    if text[index]!='>'and text[index]!='<':   
                        key+=text[index]
                    index=index+1               
                s.push(key)
        
            elif text[index+1]=='/':           
                unkey=''
            
                while text[index]!='>':
                    if text[index]!='>'and text[index]!='<' and text[index]!='/': 
                        unkey=unkey+text[index]                    
                    index+=1
                a.append(unkey)           
            index=index+1
            
    except IndexError:
        pass

    
    x=-1
    y=0
    u=0
    lenght=len(a)
                
    denge=True     
   
    j=-1
    if len(s.items)>len(a)and denge:
        while True:
            i=s.items[j]
            
            if i not in a:
                f=i
                break
            j=j-1   
        print f, " kodlu acma islemine karsilik gelen kapama kodu bulunamamistir"   
    for i in a:
        if s.isEmpty():
                print 'a'
        
        if i in s.items :
            
            
            
            index=s.items.index(i)
            
            yeniindex=len(s.items)-index
                
            while yeniindex>0:
                if s.isEmpty():
                    break
                else:
                    s.pop()
                    yeniindex-=1
        else:            
            print "----",a[u],"---- yapmis oldugunuz kapamanin uygun olmadigi tespit edildi lutfen duzeltiniz"
            break
        u+=1
    if s.isEmpty():
        print "yapilan acma ve kapama islemleri dogrudur"
       

   
    
        
            
                        
        
  
"""
    if len(s.items)==len(a):
        while len(s.items)>0 and balanced:
            if s.items[x]==a[y]:
                if  s.isEmpty(): 
                    balanced=False    
                    
                else:
                    balanced=True
                    s.pop()
            else:
                balanced=False
                
            y=y+1
        
    elif len(s.items)<len(a):
        k=False
        balanced=False
    elif len(s.items)>len(a):
        k=True    

    if balanced and s.isEmpty():
        print "yapilan islemler ve kapamalar dogrudur"
    
    elif k == False and balanced==False :
        print " eksik acma"
    elif k:
        print " eksik kapama 
"""

ay(50)




        
       

    

            
            
            
            
    
        
