class Calculator:
    def add(self,first_number:float, second_number:float) -> float:
        return first_number + second_number

    def subtract(self,first_number:float, second_number:float) -> float:
        return first_number - second_number

    def multiply(self,first_number:float, second_number:float) -> float:
        return first_number * second_number

    def divide(self,first_number:float, second_number:float) -> float:
        if second_number == 0:
            raise ValueError("Second number cannot be zero")
        return first_number / second_number