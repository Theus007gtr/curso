#solicitar ao usuario que dijita um numero
numero = float (input("digite um numero:"))
#verificar se o numero e positivo, negativo ou zero
if numero > 0:
    print("o numero e positivo")
elif numero < 0:
    print("o numero e negativo")
else:
    print("o numero e zero")