print("!Semaje chief...Tell me what you want us to calculate!")
num1 = eval(input('Please enter your first number: '))
operator = input("Enter your operator(+,-,*,/): ")
num2 = eval(input('Please enter your second number: '))
if operator == '+':
    print('Your answer is:' ,num1 + num2)
if operator == '-':
    print('Your answer is:' ,num1 - num2)
if operator == '*':
    print('Your answer is:' ,num1 * num2)
if operator == '/':
    print('Your answer is:' ,num1 / num2 if num2 != 0 else 'Error: Division by zero')
