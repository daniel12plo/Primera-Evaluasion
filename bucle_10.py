def bucle_10():
    #Suma de numeros pares e impares
    nfinal= input("NUMERO = ")
    numero_pares=0
    numero_impares=0
    for numero in range(1,nfinal+1):
        #para cada numero me pregunto si es par o impar
        if(numero%2==0):
            print str(numero)," es par"
            numero_pares=numero_pares+1
        else:
            print str(numero)," es impar"
            numero_impares=numero_impares+1
    print "He contado ",numero_pares, " números pares"
    print "He contado ",numero_impares, " números impares"


bucle_10()
    
