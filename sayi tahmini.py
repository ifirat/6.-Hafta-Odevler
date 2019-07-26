
print("LUTFEN AKLINIZDA 0-100 ARASI BIR SAYI TUTUNUZ... ")

tahmin = 50
yuksek =[100]
dusuk = [0]

while True:
    
    if not tahmin==99:
        tahmin = (max(dusuk) + min(yuksek))/2
        tahmin = int(tahmin)
    else:
        tahmin = tahmin + 1
        
    print("PC' nin tahmini = " , tahmin)

    sonuc = input("Tahminimiz buyukse '-', Kucukse '+', Dogru ise 'enter' tusuna basiniz :")

    if sonuc=="+":
        dusuk.append(tahmin)

    elif sonuc=="-":
        yuksek.append(tahmin)

    
    elif sonuc=="":
        print("TEBRIKLER KAZANDINIZ")
        break

    else:
        print("Hatali Islem : Lutfen istenilen sembollerden birini giriniz...")



