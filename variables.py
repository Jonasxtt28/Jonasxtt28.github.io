"""
(1) suma
(2) resta
(3) multi
(4) division 
"""
def calculadora(num1, num2 , op):
    if op == 1:
        print(f"el resultado de la suma de {num1} y {num2}:{num1 + num2}")
    elif op == 2:
        print(f"el resultado de la resta de {num1} y {num2}:{num1 - num2}")
    elif op == 3:
        print(f"el resultado de la multiplicacion de {num1} y {num2}:{num1 * num2}")
    elif op == 4:
        print(f"el resultado de la division de {num1} y {num2}:{num1 / num2}")
    else:
        print("te equivocaste luky")

calculadora(45,23,1) 
calculadora(45,23,2)
calculadora(45,23,3)
calculadora(45,23,4)
calculadora(20,20,1)
calculadora(20,30,1)
calculadora(620,850,1)
calculadora(252,14,4)