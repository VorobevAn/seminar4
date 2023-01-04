from random import randint as ran



def polican(min, max):
    saiz = int(input('Введите степень: '))
    equation = {}
    for key in range(saiz, -1, -1):
        value = ran(min, max)
        equation[key] = value
    return equation


def recording_polynomial(equation):
    new_equation = ''
    for (key, value) in equation.items():
        if value != 0:
            if value == 1:
                if key == 1:
                    new_equation += f'+ x '
                elif key == 0:
                    new_equation += f'+ 1 '
                else:
                    new_equation += f'+ x^{key} '
            elif value > 1:
                if key == 1:
                    new_equation += f'+ {value}*x '
                elif key == 0:
                    new_equation += f'+ {value} '
                else:
                    new_equation += f'+ {value}*x^{key} '
            elif value == -1:
                if key == 1:
                    new_equation += f'- x '
                elif key == 0:
                    new_equation += f'- 1 '
                else:
                    new_equation += f'- x^{key} '
            elif value < 1:
                if key == 1:
                    new_equation += f'- {value*-1}*x '
                elif key == 0:
                    new_equation += f'- {value*-1} '
                else:
                    new_equation += f'- {value*-1}*x^{key} '
    if new_equation[0] =='+':
        new_equation = new_equation[2:] +'= 0'
    elif new_equation[0] == '-':
       new_equation = new_equation.replace('- ','-') + '= 0'
    return new_equation


def addition(first, second):
    base = {}
    base.update(first)
    base.update(second)
    for key in base:
        if first.get(key) and second.get(key):
            base[key] = first.get(key) + second.get(key)
        elif first.get(key):
            base[key] = first.get(key)
        else:
            base[key] = second.get(key)
    return dict(sorted(base.items())[::-1])

first = polican(-100, 100)
with open('first.txt', 'w') as fail:
    fail.write(recording_polynomial(first))
 
second = polican(-100, 100)
with open('second.txt', 'w') as fail_2:
    fail_2.write(recording_polynomial(second))

with open('first.txt', 'r') as fail:
    print(fail.read())
with open('second.txt', 'r') as fail_2:
    print(fail_2.read()) 
    
    
result = addition(first, second)

with open('result.txt', 'w') as res:
    res.write(recording_polynomial(result))
with open('result.txt', 'r') as res:
    print(res.read())


