# This file holds code to program the player of the game

# Para definir un objeto en Python usamos la palabra resertvada Class
# Las clases se definen con mayuscula
# las clases tienen 2 caracteristicas principales: atributos (variables)

class Player:

    def __init__(self, name):
        self.name = name
        self.vida = 1
        
        self.armadura = 0
        self.escudo = 0
        self.voluntad = 0

        self.inventario = {

        }

        self.nivel = 0
        self.experiencia = 0

    def speak(self):
        print(f"Hola, me llamo {self.name}")
        
    def check_vida(self):
        print(f"la vida actual es{self.vida}")
    
    def check_armadura(self):
        print(f"la armadura actual es {self.armadura}")   

    def check_escudo(self):
        print(f"la escudo actual es {self.escudo}")   

    def check_voluntad(self):
        print(f"la voluntad actual es {self.voluntad}")   

    def check_nivel(self):
        print(f"El nivel actual es {self.nivel}") 

    def check_xp(self):
        print(f"La experiencia actual es {self.experiencia}")   

    def check_inventario(self):
        if self.inventario == {}
        print(f"El inventario está vacío :(*)    
                             


# Ahora creamos a un jugador, designando una variable
# player_1 = Player("Pablo")
# player_2 = Player("Ana")
# player_3 = Player("Víctor")

# Los () son para llamar a funciones
# Para acceder a los atributos del objeto lo hago sin ()

# player_1.speak()
# player_2.speak()
# player_3.speak()

print("Bienvenido a la Alfa de SpacerSurvive")


# Los metdos deben llevar self porque actuan sobre el objeto 
# Metodos magicos

#Por convencion a los atributos no se accede, solo se accede

name = input("Introduzca su nombre de jugador: ")
