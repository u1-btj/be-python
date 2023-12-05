def decorator(func):

    def compare(*num):
        if num[0] > num[1]:
            return func(num[1], num[0])
        else:
            return func(*num)

    def take_args(*num):
        if func.__name__ == 'div_between_number':
            if num[0] <= 0 or num[1] <= 0:
                print('Cannot divided by zero! Result must be greater than 1.')
            else:
                compare(*num)

        elif func.__name__ == 'substract_between_number':
            if max(*num) - min(*num) <= 0:
                print('Cannot do substraction! Result must be positive.')
            else:
                compare(*num)

    return take_args

@decorator
def substract_between_number(num1, num2):
    selisih = num2 - num1 # selalu positif
    print(f"{num2} - {num1} = {selisih}")

@decorator
def div_between_number(num1, num2):
    pembagian = num2 / num1 # selalu > 1
    print(f"{num2} / {num1} = {pembagian}")

div_between_number(5,4)
substract_between_number(5,4)

div_between_number(10,88)
substract_between_number(10,88)

div_between_number(87,50)
substract_between_number(87,50)

div_between_number(1,0)
substract_between_number(-1,0)