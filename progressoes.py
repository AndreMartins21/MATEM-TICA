class Progressao:
    def __init__(self, *num:list):
        self.lista = list(num)
        self.tam = len(self.lista)
        self.razao = 0
        self.main()
    
    def gera_pa(self) -> str:
        lista = self.lista[:]
        for i in range(10):
            lista.append(lista[-1] + self.razao)  
        return "\n".join([f"{i+1}°: {v}" for i, v in enumerate(lista)])
    
    def gera_pg(self) -> str:
        lista = self.lista[:]
        for i in range(10):
            lista.append(float(lista[-1] * self.razao))
        lista = [round(x, 3) for x in lista] # Arredondar os valores
        lista = list(map(str, lista)) # Convertendo pra string
        return "\n".join([f"{i+1}°: {v}" for i, v in enumerate(lista)])

    def is_pa(self) -> str:
        lista = self.lista
        razao = []
        for i in range(1, self.tam):
            anterior, atual = lista[i-1], lista[i]
            razao.append(atual - anterior)
            
        uniq = set(razao)
        if len(uniq) == 1: 
            self.razao = razao[0]
            return True
        return False

    def is_pg(self) -> str:
        lista = self.lista
        razao = []
        for i in range(1, self.tam):
            anterior, atual = lista[i-1], lista[i]
            try:
                razao.append(round(atual / anterior, 2))
            except ZeroDivisionError:
                print("Divisão por zero...")
                return False
            
        self.lista = list(map(float, self.lista)) # Setar todos valores como float
        uniq = set(razao)
        if len(uniq) == 1: 
            self.razao = razao[0]
            return True
        return False

    def main(self):
        if self.is_pa() and self.is_pg():
            print("Devido à pouca quantidade de valores informados, conclui-se que a sequência informada pode ser tanto PA quanto PG")
        elif self.is_pa():
            print(f"<> É uma PA de razão {self.razao}\n")
            print(self.gera_pa())
        elif self.is_pg():
            print(f"<> É uma PG de razão {self.razao}\n")
            print(self.gera_pg())
        else:
            print("Esses números não formam uma sequência de PA ou PG!")

P1 = Progressao(1.5, 3, 4.5)
