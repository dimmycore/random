import random
num = random.randint(1, 100)
while True:
    print('угадайте число от 1 до 100')
    guess = int(input('ваше число:'))
    if guess == num:
        print('правильно')
        break
    elif guess < num:
        print('загаданное число больше')
    elif guess > num:
        print('загаданное число меньше')
        
       
