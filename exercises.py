from ast import Continue


while True:
    try:
    

        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))
        num3 = int(input('Enter third number: '))


        while num1 == num2 == num3:
            x = num1 * num2 * num3
            print(x)
            break
            
            
            
            
        else:
            print(num1 + num2 + num3)
            break

    except ValueError:
        print('Pleace enter an number!')
        continue






