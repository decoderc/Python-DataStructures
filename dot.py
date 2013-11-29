nokta_sayisi = input("kullanilacak nokta sayisi:")
nokta_dizisi = range(nokta_sayisi)

print nokta_sayisi

# Birlestir (id_, start, end) ######################################### 
def Birlestir(id_, start, end):
        for i in range(int(start), int(end)+1):
                nokta_dizisi[i] = int(id_)
####################################################################### 

while True:
        girdi = raw_input("Baglanti (or. 6-9) / Birlestir ('B') / Cikis ('end') ? : ")
        if girdi == "end":
            print "cikis zamani"
            break
        
#######################################################################        
        elif (girdi == 'B') or (girdi == 'b'): # Birlestirme
                birlestir_str = raw_input("id-start-end ? :");
                par_id, par_start, par_end = birlestir_str.split('-')
                Birlestir(par_id, par_start, par_end)
#######################################################################
        else:
                
                ilk_nokta, ikinci_nokta = girdi.split("-")
                ilk_nokta, ikinci_nokta = int(ilk_nokta), int(ikinci_nokta)

                if (ilk_nokta > nokta_sayisi) or (ikinci_nokta > nokta_sayisi):
                    print "Sinir deger asimi"

                gecici= nokta_dizisi[ilk_nokta]
                
                if gecici != nokta_dizisi[ikinci_nokta]:
                    sayac = 0
                    while sayac < nokta_sayisi:
                        if nokta_dizisi[sayac] == gecici:
                            nokta_dizisi[sayac] = nokta_dizisi[ikinci_nokta]
                        sayac += 1

                print girdi + " ",
        print "Yeni durum: " + str(nokta_dizisi)
