# by Manuel Marchand
class BasicMathFunctions:
    def __init__(self, a = None, b = None):
        self.a = a
        self.b = b

    def greet_user(self):
        print("Greetings, " + str(self.a) + " " + str(self.b))

    def add(self):
        return int(self.a) + int(self.b)

    def perform_operation(self, operation):
        if self.a is not None and self.b is not None:
            match operation:
                case "+":
                    return self.a + self.b
                case "-":
                    return self.a - self.b
                case "*":
                    return self.a * self.b
                case "/":
                    return self.a / self.b
                case _:
                    return "Please enter a valid operation, +, -, *, or /"

    def square(self):
        return self.a**2

    def factorial(self):
        output = 1
        for i in range(2, self.a+1):
            output *= i
        return output

    def counting(self):
        return list(range(int(self.a), int(self.b)+1))

    def calculate_hypotenuse(self):
        return (BasicMathFunctions(self.a).square() + BasicMathFunctions(self.b).square()) ** 0.5

    def rect_area(self):
        return self.a * self.b

    def power(self):
        return self.a ** self.b

    def type_of(self):
        try:
            # following code throws an exception if input string doesn't contain only numbers
            # if input contains only numbers it will properly return int or float depending on the input
            return str(type(eval(self.a))).replace("<class '", "").replace("'>", "")
        except:
            if str(self.a) == "True" or str(self.a) == "False":
                return "bool"
            else:
                return "str"


def check_string(prompt):
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except:
            print("Invalid entry")
def main():
    options = ["addition",
               "operation",
               "square",
               "factorization",
               "counting",
               "hypotenuse calculation",
               "rectangle area calculation",
               "exponentiation",
               "find type",
               "quit"]
    first_name = str(input("Please enter your first name: "))
    last_name = str(input("Please enter your last name: "))
    BasicMathFunctions(first_name, last_name).greet_user()
    while True:
        for i in range(len(options)):
            print(str(i+1) + ": " + options[i])
        selection = int(check_string("Please enter the number of the method to execute: "))
        if selection not in list(range(1, len(options)+1)):
            print("Enter number between 1 and " + str(len(options)))
        else:
            if selection == 9:
                op1 = input("Enter type to check: ")
            elif selection == 10:
                quit()
            else:
                op1 = float(check_string("Please enter an operand: "))
                if selection != 3 and selection != 4 and selection != 9:
                    op2 = float(check_string("Please enter the second operand: "))
            output = None
            match selection:
                case 1:
                    output = BasicMathFunctions(op1, op2).add()
                case 2:
                    while True:
                        op3 = input("Please enter an operator (+, -, *, or /): ")
                        if op3 == "*" or op3 == "+" or op3 == "-" or op3 == "/":
                            break
                        else:
                            print("Invalid entry")
                    output = BasicMathFunctions(op1, op2).perform_operation(op3)
                case 3:
                    output = BasicMathFunctions(op1).square()
                case 4:
                    output = BasicMathFunctions(op1).factorial()
                case 5:
                    output = BasicMathFunctions(op1, op2).counting()
                case 6:
                    output = BasicMathFunctions(op1, op2).calculate_hypotenuse()
                case 7:
                    output = BasicMathFunctions(op1, op2).rect_area()
                case 8:
                    output = BasicMathFunctions(op1, op2).power()
                case 9:
                    output = BasicMathFunctions(op1).type_of()
                case _:
                    output = None
            print("The result of your " + str(options[selection-1]) + " is: " + str(output))


main()