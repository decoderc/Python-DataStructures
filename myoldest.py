def asalmi(sayi):
    i=0
    sayi=0
    kontrol=true
    raw_input("sayiyi gir"),sayi
    for i in range(2,(sayi-1),1):
        if(sayi%2==0):
            kontrol=false
        if(kontrol==true):
            print "girdiginiz sayi asaldir."
        else:
            print "girdiginiz sayi asal degildir."
            return sayi
            
