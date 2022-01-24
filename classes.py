# class 

# syntax

class Computador:
    #construtor com dados que serao usados 
    def __init__(self,marca:str,memoria="8gb"):
        #marca, memoria , placa de video
        self.marca = marca
        self.memoria = memoria
        self.placa = "Nvidia"
        print(self.ligar())

    def ligar(self):
        return  "ligando compiuri"

    def desligar(self):
        print("desligando")

    infos = lambda self: print(f"marca:{self.marca}, memoria:{self.memoria}, placa:{self.placa}")


#comp  = Computador("asus","12gb")
#comp.infos()
#comp.marca = "Samsung"
#comp.infos()


class Heranca(Computador):
    def __init__(self):
        super().__init__(marca="aaaaaa")

    def elemento(self):
        print("bateria " + self.marca + f" but memory the {self.memoria} " + self.placa)

hr = Heranca()

#hr.infos()
hr.elemento()

"""se passa outro construtor para minha class Heranca sera chamado de polimorfismo
que e atribuição de outros valores ao meu objeto , para mim usar um init novo e 
tbm usar o init com os valores ca minha outra class eu passo a seguinte 
informção :

super().__init__(v=10,i=5) v and i sao atributos aleatorios que eu coloquei

ex: class Heranca(Computador):
    def __init__(self):
        super().__init__(marca,memoria="8gn")"""