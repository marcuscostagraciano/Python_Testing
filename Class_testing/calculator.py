class Calculator: 

    def __init__(self,n1=0,n2=0):
        self.n1 = n1
        self.n2 = n2

    def sum(self):
        return self.n1 + self.n2


    def minus(self):
        return self.n1 - self.n2


    def times(self):
        return self.n1 * self.n2


    def division(self):
        if self.n2 == 0: return
        return round(self.n1 / self.n2, 2)


numbers = input("Type n1 and n2 (separated using space): ").split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])    
        

calc = Calculator(numbers[0], numbers[1])
print(f"Sum: {calc.sum()}")
print(f"Minus: {calc.minus()}")
print(f"Times: {calc.times()}")
print(f"Division: {calc.division()}")