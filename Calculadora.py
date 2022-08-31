import time

print('~'*40)
print('''

╭━━━╮╱╱╭╮╱╱╱╱╱╱╭╮╱╱╱╱╱╭╮
┃╭━╮┃╱╱┃┃╱╱╱╱╱╱┃┃╱╱╱╱╱┃┃
┃┃╱╰╋━━┫┃╭━━┳╮╭┫┃╭━━┳━╯┣━━┳━┳━━╮
┃┃╱╭┫╭╮┃┃┃╭━┫┃┃┃┃┃╭╮┃╭╮┃╭╮┃╭┫╭╮┃
┃╰━╯┃╭╮┃╰┫╰━┫╰╯┃╰┫╭╮┃╰╯┃╰╯┃┃┃╭╮┃
╰━━━┻╯╰┻━┻━━┻━━┻━┻╯╰┻━━┻━━┻╯╰╯╰╯
''')
print('Feito por Aero')
print('~'*40)

def soma():
    calc = float(input('Número 1: '))
    calc2 = float(input('Número 1: '))
    total = calc + calc2
    print(total)

def subtração():
    calc = float(input('Número 1: '))
    calc2 = float(input('Número 1: '))
    total = calc - calc2
    print(total)

def divisão():
    calc = float(input('Número 1: '))
    calc2 = float(input('Número 1: '))
    total = calc // calc2
    print(total)

def multiplicação():
    calc = float(input('Número 1: '))
    calc2 = float(input('Número 1: '))
    total = calc * calc2
    print(total)

print('Qual opção vc deseja')
print('~'*40)
time.sleep(1)
print('Opção 1: Soma')
time.sleep(1)
print('Opção 2: Subtração')
time.sleep(1)
print('Opção 3: Divisão')
time.sleep(1)
print('Opção 4: Multiplicação')
time.sleep(1)
print('~'*40)
opção = int(input('Opção: '))

if opção == 1:
    soma()
elif opção == 2:
    subtração()
elif opção == 3:
    divisão()
elif opção == 4:
    multiplicação()
