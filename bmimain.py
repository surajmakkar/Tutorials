class BMI:
    def calculate(self,weight,height):
        self.weight=weight
        self.height=height
        bmi=(self.weight/pow(height,2))
        return bmi
#this is called data encapsulation.