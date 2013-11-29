def maks(kesirler):
    maksimum = float('-inf') #listedeki kesirlerden en buyugunun degeri
    aranan_indeks = 0 # listedeli en buyuk kesrin indeksi

    for i in range(0, len(kesirler)):
        
        eleman = kesirler[i]
        if (eleman[0] == '-'): #pay negatif
            if(eleman[eleman.find('/')+1] == '-'): #pay ve payda negatif, kesir pozitif
                pay = float(eleman[(eleman.find('-')+1):(eleman.find('/'))])
                eleman = eleman[(eleman.find('/')):]
                payda = float(eleman[(eleman.find('-')+1):])
                deger = pay/payda
                if (deger > maksimum):
                    maksimum = deger
                    aranan_indeks = i

            else: # pay negatif payda pozitif
                pay = float(eleman[(eleman.find('-')+1):(eleman.find('/'))])
                eleman = eleman[(eleman.find('/')):]
                payda = float(eleman[(eleman.find('/')+1):])
                deger = (pay/payda)*(-1.0) # kesir negatifti
                if (deger > maksimum):
                    maksimum = deger
                    aranan_indeks = i

        else: 
            if(eleman[eleman.find('/')+1] == '-'): #pay pozitif, payda negatif
                pay = float(eleman[:(eleman.find('/'))])
                eleman = eleman[(eleman.find('/')):]
                payda = float(eleman[(eleman.find('-')+1):])
                deger = (pay/payda) * (-1.0)
                if (deger > maksimum):
                    maksimum = deger
                    aranan_indeks = i

            else: # pay ve payda pozitif
                pay = float(eleman[:(eleman.find('/'))])
                eleman = eleman[(eleman.find('/')):]
                payda = float(eleman[(eleman.find('/')+1):])
                deger = pay/payda
                if (deger > maksimum):
                    maksimum = deger
                    aranan_indeks = i

    print 'EN BUYUK KESIR : '
    print kesirler[aranan_indeks]
    
#######################################################
# kesirli sayilari string olarak tutariz

ornek = ['3/5', '7/-12', '8/7', '100/-4', '100/1061', '7/12', '60/61', '7/6', '61/60']

maks(ornek)
