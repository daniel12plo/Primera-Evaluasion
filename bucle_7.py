def bucle_7():
    print "*******************************"
    print "* EL CONSTRUCTOR DE PIRAMIDES *"
    print "*******************************"
    print "Indica de que altura deseas la piramide."
    altura=input("altura = ")
    for fil in range(1,altura+1):
        for col in range(1,fil+1):
            print "*",
        print " "
bucle_7()
