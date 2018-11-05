def bucle_11_suma():
    print "Hasta que número quieres sumar: "
    nfinal=input("numero = ")
    suma_pares=0
    suma_impares=0
    for numero in range (1,nfinal+1):
        if(numero%2==0):
            print str(numero)," es Par"
            suma_pares=suma_pares+numero
        else:
            print str(numero)," es Impar"
            suma_impares=suma_impares+numero
    print "La suma de los números pares vale",suma_pares
    print "La suma de los números impares vale",suma_impares

bucle_11_suma()
