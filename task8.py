num = 153
if num > 99 and num < 1000:
    print(num, 'это трехзначное число')
if num > 0 and num % 2 == 0:
    print(num, ' это число больше нуля и четное')
if num % 31 ==0:
    print(num, 'это число делится без остатка на 31')
if num > 100 and num % 17 ==0 or num > 150 and num == 13**2:
    print(f'это число {num}')