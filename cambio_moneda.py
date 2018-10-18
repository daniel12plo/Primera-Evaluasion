def cambio_moneda():
    moneda=input("Cuanto quieres cambiar?")
    respuesta=raw_input("dolares o libras o camellos?")
    if (respuesta=="dolares"):
        print str (moneda*1.15) + " dolares"
    else:
        if(respuesta=="libras"):
            print str (moneda*0.88) + " libras"
    if (respuesta=="camellos"):
        print str (moneda*2.22) + " camellos"
        

cambio_moneda()           
