# by Manuel Marchand
# EECE-2140 Assignment #05

class BasicMathFunctions:
    # define init method with variables with default variable so class can be called with only 1 arguement
    def __init__(self, a, b = None):
        self.a = a
        self.b = b

    def greet_user(self):
        print("Greetings, " + str(self.a) + " " + str(self.b))

    def add(self):
        return int(self.a) + int(self.b)

    def perform_operation(self, operation):
        # check if arguements have been passed
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
        # counts from 2 to the input and multiplies all those numbers
        for i in range(2, self.a+1):
            output *= i
        return output

    def counting(self):
        # uses the built-in range function to count
        return list(range(int(self.a), int(self.b)+1))

    def calculate_hypotenuse(self):
        # uses the square function defined in the class earlier
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
            # the input string contains either a mix of letters and numbers or letters
            # manually check if it's a bool
            if str(self.a) == "True" or str(self.a) == "False":
                return "bool"
            else:
                # else it has to be a string
                return "str"


def check_string(prompt):
    while True:
        user_input = input(prompt)
        try:
            # try converting to a float
            return float(user_input)
        except:
            # if error thrown the entry was invalid, prompt user to enter again
            print("Invalid entry")
def main():
    # define operations the user can execute
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
    # prompt user for first and last name
    first_name = str(input("Please enter your first name: "))
    last_name = str(input("Please enter your last name: "))
    # use greet user method
    BasicMathFunctions(first_name, last_name).greet_user()
    # main ui loop
    while True:
        # print out all the user's options with the number in front
        for i in range(len(options)):
            print(str(i+1) + ": " + options[i])
        selection = int(check_string("Please enter the number of the method to execute: "))
        # ensure the selection is one of the options and not outside of range
        if selection not in list(range(1, len(options)+1)):
            print("Enter number between 1 and " + str(len(options)))
        else:
            if selection == 9:
                # special case, doesn't need to be checked
                op1 = input("Enter type to check: ")
            elif selection == 10:
                # user wants to quit program
                quit()
            else:
                # ensure user input is valid
                op1 = float(check_string("Please enter an operand: "))
                # these selections require a second operand
                if selection != 3 and selection != 4 and selection != 9:
                    # ensure the second operation the user inputted is valid
                    op2 = float(check_string("Please enter the second operand: "))
            output = None
            # define all program behaviors with a switch case
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
            # display result to user
            print("The result of your " + str(options[selection-1]) + " is: " + str(output))


main()