def hesablama():
    ilkEded = float(input('Ədədi daxil edin: '))
    riyaziEmel = input('Riyazi əməli daxil edin: +,-,*,/,%\n')
    ikinciEded = float(input('Ədədi ədədi daxil edin: '))

    def vur():
        return ilkEded * ikinciEded

    def bol():
        return ilkEded / ikinciEded

    def topla():
        return ilkEded + ikinciEded

    def cix():
        return ilkEded - ikinciEded
    
    def faiz():
        return (ilkEded * ikinciEded) / 100
        
    if riyaziEmel == '*':
        print(vur())
        vurma = vur()

        while vurma >= 0 or vurma < 0:
            elaveRiyaziEmel = input('+,-,*,/,%\n')
            elaveEded = float(input(''))
            if elaveRiyaziEmel == '*':
                vurma *= elaveEded
                print(vurma)
            elif elaveRiyaziEmel == '/':
                try:
                    vurma /= elaveEded
                    print(vurma)
                except ZeroDivisionError:
                    print('0-a bölmə yoxdur!')
            elif elaveRiyaziEmel == '+':
                vurma += elaveEded
                print(vurma)
            elif elaveRiyaziEmel == '-':
                vurma -= elaveEded
                print(vurma) 
            else:
                vurma *= elaveEded / 100
                print(vurma)

    elif riyaziEmel == '/':
        try:
            print(bol())
            bolme = bol()

            while bolme >= 0 or bolme < 0:
                elaveRiyaziEmel = input('+,-,*,/,%\n')
                elaveEded = float(input(''))
                if elaveRiyaziEmel == '*':
                    bolme *= elaveEded
                    print(bolme)
                elif elaveRiyaziEmel == '/':
                    try:
                        bolme /= elaveEded
                        print(bolme)
                    except ZeroDivisionError:
                        print('0-a bölmə yoxdur!')
                elif elaveRiyaziEmel == '+':
                    bolme += elaveEded
                    print(bolme)
                elif elaveRiyaziEmel == '-':
                    bolme -= elaveEded
                    print(bolme)
                else:
                    bolme *= elaveEded / 100
                    print(bolme)
        except ZeroDivisionError:
            print('0-a bölmə yoxdur, bir daha sınayın')
            hesablama()

    elif riyaziEmel == '+':
        print(topla())
        toplama = topla()

        while toplama >= 0 or toplama < 0:
            elaveRiyaziEmel = input('+,-,*,/,%\n')
            elaveEded = float(input(''))
            if elaveRiyaziEmel == '*':
                toplama *= elaveEded
                print(toplama)
            elif elaveRiyaziEmel == '/':
                try:
                    toplama /= elaveEded
                    print(toplama)
                except ZeroDivisionError:
                    print('0-a bölmə yoxdur!')
            elif elaveRiyaziEmel == '+':
                toplama += elaveEded
                print(toplama)
            elif elaveRiyaziEmel == '-':
                toplama -= elaveEded
                print(toplama)
            else:
                toplama *= elaveEded / 100
                print(toplama) 
                
    elif riyaziEmel == '-':
        print(cix())
        cixma = cix()

        while cixma >= 0 or cixma < 0:
            elaveRiyaziEmel = input('+,-,*,/,%\n')
            elaveEded = float(input(''))
            if elaveRiyaziEmel == '*':
                cixma *= elaveEded
                print(cixma)
            elif elaveRiyaziEmel == '/':
                try:
                    cixma /= elaveEded
                    print(cixma)
                except ZeroDivisionError:
                    print('0-a bölmə yoxdur!')
            elif elaveRiyaziEmel == '+':
                cixma += elaveEded
                print(cixma)
            elif elaveRiyaziEmel == '-':
                cixma -= elaveEded
                print(cixma) 
            else:
                cixma *= elaveEded / 100
                print(cixma)

    else:
        print(faiz())
        faizDeyer = faiz()

        while faizDeyer >= 0 or faizDeyer < 0:
            elaveRiyaziEmel = input('+,-,*,/,%\n')
            elaveEded = float(input(''))
            if elaveRiyaziEmel == '*':
                faizDeyer *= elaveEded
                print(faizDeyer)
            elif elaveRiyaziEmel == '/':
                try:
                    faizDeyer /= elaveEded
                    print(faizDeyer)
                except ZeroDivisionError:
                    print('0-a bölmə yoxdur!')
            elif elaveRiyaziEmel == '+':
                faizDeyer += elaveEded
                print(faizDeyer)
            elif elaveRiyaziEmel == '-':
                faizDeyer -= elaveEded
                print(faizDeyer) 
            else:
                faizDeyer *= elaveEded / 100
                print(faizDeyer)

hesablama()