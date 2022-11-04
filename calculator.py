class Calculator():

    # def __init__ (self, num1, num2):
    #     self.num1 = float(num1)
    #     self.num2 = float(num2)

    def suma(num1, num2):
        suma = float(num1) + float(num2)
        return(suma)

    def resta(num1, num2):
        resta = float(num1) - float(num2)
        return(resta) 

    def multi(num1, num2):
        multi = float(num1) * float(num2)
        return(multi) 

    def div(num1, num2):
        if num2 == 0:
            return "No se puede dividir entre cero"
        div = float(num1) / float(num2)
        return(div)
    
    def pot(num1, num2):
        pot = pow(num1, num2)
        return(pot) 