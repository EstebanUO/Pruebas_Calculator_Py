from calculator import Calculator

class Prueba():
    with open ('numeros.txt', 'r') as f:
        leer = f.readlines()
    print(leer)

    # leer = "-36 / 61 -0.5901639344262295"
    numeros = leer()
    print(numeros[3])

  #variables
    num1 = numeros[0]
    num2 = numeros[2]
    expresion = numeros[1]
    result = numeros[3]

    def pruebas(expresion, num1, num2, result):
        if  expresion == "/":
            division = Calculator(num1, num2)
            resultado = Calculator.div(division)
            print(resultado)
        
            if result == resultado:
                return f"{num1} {expresion} {num2} = {result} =====> Prueba superada!!"
            else:
                return f"{num1} {expresion} {num2} = {result} =====> No supero la prueba :("

        elif expresion == "+":
            suma = Calculator(num1, num2)
            resultado = Calculator.suma(suma)
            if result != resultado:
                return f"{num1} {expresion} {num2} = {result} -----> No supero la prueba :( \n"
            else:
                return (f"{num1} {expresion} {num2} = {result} -----> Prueba superada!! \n")

        elif expresion == "-":
            resta = Calculator(num1, num2)
            resultado = Calculator.resta(resta)
            if result != resultado:
                return f"{num1} {expresion} {num2} = {result} -----> No supero la prueba :( \n"
            else:
                return (f"{num1} {expresion} {num2} = {result} -----> Prueba superada!! \n")

        elif expresion == "*":
            multiplicacion = Calculator(num1, num2)
            resultado = Calculator.multi(multiplicacion)
            if result != resultado:
                return f"{num1} {expresion} {num2} = {result} -----> No supero la prueba :( \n"
            else:
                return (f"{num1} {expresion} {num2} = {result} -----> Prueba superada!! \n")

        elif  expresion == "^":
            potencia = Calculator(num1, num2)
            resultado = Calculator.pot(potencia)
            if result != resultado:
                return f"{num1} {expresion} {num2} = {result} -----> No supero la prueba :( \n"
            else:
                return (f"{num1} {expresion} {num2} = {result} -----> Prueba superada!! \n")

        else:
            print( "Caracter no existente")

    print(pruebas(expresion, num1, num2, result))