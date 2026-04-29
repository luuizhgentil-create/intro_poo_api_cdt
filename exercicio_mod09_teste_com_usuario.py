class Celular:
    def__init__(self, marca, modelo)

    def  verificar_status(self):
        try:
            entrada=input(f"Bateria do {self.modelo}:")
            nivel=float(entrada)
            if nivel<0 or nivel>100:
                print("Valor inválido! Digite de 0 a 100.")
                elif nível <15:
                    print(f"Bateria em {nivel}%! Carregue já.")
            elif nivel>85:
        print(f"Bateria em {nivel}%. Carga exelente!")
    else:
        print(f"Bateria em nivel {nivel}%. Status normal.")
    except ValueError:
        print("Erro: Digite apenas números!")

cel=Celular("Samsung", "S24")
cel.verificar_status()
