def collatz(number):
        if number % 2 == 0:
            return int(number / 2)
        else:
            return int(3 * number + 1)

try:
    number = int(input('整数を入力してください: '))
    if number == 1:
        print('数値はすでに1です。')
    else:
        while number != 1:
            number = collatz(number)
            print(number)

except ValueError:
    print('整数を入力する必要があります。')
