class Calculator():

    def __init__ (self, num1, num2):
        self.num1 = float(num1)
        self.num2 = float(num2)

    def suma(self):
        suma = self.num1 + self.num2
        return(suma)

    def resta(self):
        resta = self.num1 - self.num2
        return(resta) 

    def multi(self):
        multi = self.num1 * self.num2
        return(multi) 

    def div(self):
        div = self.num1 / self.num2
        return(div) 
    
    def pot(self):
        pot = pow(self.num1, self.num2)
        return(pot) 