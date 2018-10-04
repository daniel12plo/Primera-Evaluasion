def condicional_2():
    respuesta=input("que hora es? ")
    if(respuesta >24 ):
        print "Numero no valido"
    elif(respuesta >= 20 ):
        print "Buenas noches"
    elif(respuesta >= 12 ):
        print "Buenas tardes"
    elif(respuesta < 12 ):
        print "Buenos dias"
  

condicional_2()
