def piramide():
    n=input("dime el numero de filas")
    for i in range (0,n):
        for i in range(0,i+1,1):
            print"*",
        print ""

piramide()
