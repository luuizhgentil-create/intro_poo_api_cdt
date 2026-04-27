class Celular:
    def__init__(self, marca, modelo)

    def  verificar_status(self):
        try:
            entrada=input(f"Bateria do {self.modelo}:")
            nivel=float(entrada)
            if nivel<0 or nivel>100:
                print("Valor inválido! Digite de 0 a 100.")
                elif nível