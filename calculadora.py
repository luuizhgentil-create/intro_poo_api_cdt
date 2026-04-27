
print("---Desafio 1: Divisão---")

try:
    numerador=int(input("Digita o Numerador:"))
    denominador=int(input("Digita o denominador:"))
    resultado=numerador/denominador
except ValueError:
    print("Erro: Digita apenas números interos!")
except ZeroDivisionError:
    print("Erro: Não podes dividir por zero.")
except Exception as erro:
    prinnt(f"Erro inesperado: {erro}")
else:
    print(f"Sucesso! Resultado: {resultado}")
finally:
    print("---Fim da Divisão---")



