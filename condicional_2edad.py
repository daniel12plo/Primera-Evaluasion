def condicional_2():
    edad=input("cual es tu edad?")
    if(edad>=18):
        print "Sala alcoholica"
    else:
        if(edad>=15):
            print "Sala adolescentes"
        else:
            print "Sala infaltil"

condicional_2()
