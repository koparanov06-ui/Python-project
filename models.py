class Calculator: 
    
    def __init__(self, initial_value=0):
        self.result = initial_value
        self.history = []
    
    def add(self, number):
       
        self.history.append(f"Added {number} to {self.result}")
        self.result += number
        return self.result
    
    def subtract(self, number):
        
        self.history.append(f"Subtracted {number} from {self.result}")
        self.result -= number
        return self.result
    
    def multiply(self, number):
       
        self.history.append(f"Multiplied {self.result} by {number}")
        self.result *= number
        return self.result
    
    def divide(self, number):
       
        if number == 0:
            raise ValueError("Cannot divide by zero!")
        self.history.append(f"Divided {self.result} by {number}")
        self.result /= number
        return self.result
    
    def get_result(self):
        
        return self.result
    
    def reset(self):
        
        self.result = 0
        self.history = []
    
    def get_history(self):
       
        return self.history
