# ENTREGABLE - HERENCIA MÚLTIPLE-MRO-ENCAPSULAMIENTO-ABSTRACCIÓN



# ==============================================================================
# CLASE 3 - PUNTO 1: HERENCIA MÚLTIPLE
# ==============================================================================
print("\n==================== CLASE 3 - PUNTO 1: HERENCIA MÚLTIPLE ====================\n")


class Abuela:
    def __init__(self, recetas, paciencia, sabiduria):
        self.recetas = recetas
        self.paciencia = paciencia
        self.sabiduria = sabiduria

    def hablar(self):
        return "Hola, Yo vengo de parte de la familia de mi abuela"

    def __str__(self):
        return f"Recetas: {self.recetas} \nPaciencia: {self.paciencia} \nSabiduria: {self.sabiduria}"


class Abuelo:
    def __init__(self, oficio, humor, experiencia):
        self.oficio = oficio
        self.humor = humor
        self.experiencia = experiencia

    def hablar(self):
        return "Hola, Yo vengo de parte de la familia de mi abuelo"

    def __str__(self):
        return f"Oficio: {self.oficio} \nHumor: {self.humor} \nExperiencia: {self.experiencia}"


class Nieto(Abuela, Abuelo):
    def __init__(self, recetas, paciencia, sabiduria, oficio, humor, experiencia):
        super().__init__(recetas, paciencia, sabiduria)
        Abuelo.__init__(self, oficio, humor, experiencia)

    def hablar(self):
        return f"Hola, Soy una persona con oficio: {self.oficio}, con humor: {self.humor} y con sabiduria: {self.sabiduria}"


Samuel = Nieto("Sancocho", "Mucha", "Alta", "Carpintero", "Bromista", "Media")
print(Samuel.hablar())

# Se muestra el MRO de Nieto, para ver el orden en que Python busca los métodos
# cuando hay herencia múltiple (Abuela y Abuelo).
print(Nieto.__mro__)

# ==============================================================================
# CLASE 3 - PUNTO 2: CADENA DE HERENCIA LINEAL
# ==============================================================================
print("\n================== CLASE 3 - PUNTO 2: CADENA DE HERENCIA LINEAL ==================\n")


class A:
    def hablar(self):
        return "Hola soy la clase A"


class B(A):
    def hablar(self):
        return "Hola soy la clase B"


class C(B):
    def hablar(self):
        return "Hola soy la clase C"


class D(C):
    def hablar(self):
        return "Hola soy la clase D"


class E(D):
    def hablar(self):
        return "Hola soy la clase E"


class F(E):
    def hablar(self):
        return "Hola soy la clase F"


class G(F):
    def hablar(self):
        return "Hola soy la clase G"


print(G.__mro__)  # Cadena lineal: G -> F -> E -> D -> C -> B -> A -> object

# ==============================================================================
# CLASE 3 - PUNTO 3: HERENCIA MÚLTIPLE (MRO MÁS COMPLEJO)
# ==============================================================================
print("\n============= CLASE 3 - PUNTO 3: HERENCIA MÚLTIPLE (MRO COMPLEJO) =============\n")


class A2:
    def hablar(self):
        return "Hola soy la clase A2"


class B2(A2):
    def hablar(self):
        return "Hola soy la clase B2"


class C2(B2):
    def hablar(self):
        return "Hola soy la clase C2"


class D2(C2):
    def hablar(self):
        return "Hola soy la clase D2"


class E2(D2, C2):
    def hablar(self):
        return "Hola soy la clase E2"


class F2(D2, C2):
    def hablar(self):
        return "Hola soy la clase F2"


class G2(F2, E2):
    def hablar(self):
        return "Hola soy la clase G2"


print(G2.__mro__)  # Muestra el orden de resolución de métodos (Method Resolution Order)


# ==============================================================================
# CLASE 5 - EJERCICIO 1: PERSONAJE CON VIDA (CORAZONES)
# ==============================================================================
print("\n================ CLASE 5 - EJERCICIO 1: PERSONAJE CON VIDA ================\n")

# Personaje con 10 corazones (vida) que puede recibir ataques y perder corazones.
class Personaje:
    def __init__(self, nombre, corazones=10):
        self.nombre = nombre
        self.corazones = corazones
        self.vivo = True

    def recibir_ataque(self, daño, atacante):
        if not self.vivo:
            print(f"{self.nombre} ya está muerto, {atacante} no puede hacerle más daño.")
            return

        self.corazones -= daño
        if self.corazones <= 0:
            self.corazones = 0
            self.vivo = False
            print(f"{atacante} atacó a {self.nombre} y le quitó {daño} corazones. {self.nombre} ha MUERTO.")
        else:
            print(f"{atacante} atacó a {self.nombre} y le quitó {daño} corazones. Le quedan {self.corazones} corazones.")

    def estado(self):
        if self.vivo:
            return f"{self.nombre} está vivo con {self.corazones} corazones."
        else:
            return f"{self.nombre} está muerto."


Steve = Personaje("Steve")
Steve.recibir_ataque(3, "Caída")
print(Steve.estado())


# ==============================================================================
# CLASE 5 - EJERCICIO 2: MOBS QUE ATACAN AL PERSONAJE
# ==============================================================================
print("\n============== CLASE 5 - EJERCICIO 2: MOBS QUE ATACAN AL PERSONAJE ==============\n")


class Mob:
    def __init__(self, nombre, daño, sonido, drop, forma_ataque):
        self.nombre = nombre
        self.daño = daño
        self.sonido = sonido
        self.drop = drop
        self.forma_ataque = forma_ataque

    def hacer_sonido(self):
        return f"*{self.nombre} hace: {self.sonido}*"

    def atacar(self, personaje):
        print(self.hacer_sonido())
        print(f"{self.nombre} ataca con: {self.forma_ataque}.")
        personaje.recibir_ataque(self.daño, self.nombre)

    def soltar_drop(self):
        print(f"{self.nombre} suelta al morir: {self.drop}")


class Creeper(Mob):
    def __init__(self):
        # El Creeper explota, hace mucho daño y no hace ruido de "golpe" sino un siseo
        super().__init__("Creeper", 6, "sssss...", "pólvora", "explosión")


class Zombie(Mob):
    def __init__(self):
        super().__init__("Zombie", 2, "gruñido", "carne podrida", "golpe cuerpo a cuerpo")


class Esqueleto(Mob):
    def __init__(self):
        super().__init__("Esqueleto", 3, "hueso al chocar", "flechas y huesos", "disparo de flecha")


class Enderman(Mob):
    def __init__(self):
        super().__init__("Enderman", 4, "sonido gutural al teletransportarse", "perla de Ender", "teletransporte y golpe")


# Se crea un nuevo personaje con sus 10 corazones completos 
Alex = Personaje("Alex")
print(Alex.estado())

mobs = [Zombie(), Esqueleto(), Creeper(), Enderman()]

for mob in mobs:
    mob.atacar(Alex)

print(Alex.estado())

# Si el personaje sobrevive a la ronda de ataques, se le suma un Creeper extra
# para mostrar tanto el caso de "sigue vivo" como el caso de "muere".
if Alex.vivo:
    Creeper().atacar(Alex)
    print(Alex.estado())

# Demostración de que cada mob, aunque hereda de la misma clase Mob,
# tiene su propio drop (esto también es polimorfismo: mismo método
# soltar_drop(), resultado distinto según el mob).
print("\nDrops de cada mob si fueran derrotados:")
for mob in mobs:
    mob.soltar_drop()


# ==============================================================================
# CLASE 6 - PUNTO 1: GETTERS, SETTERS Y DECORADOR @property
# ==============================================================================
print("\n============= CLASE 6 - PUNTO 1: GETTERS, SETTERS Y @property =============\n")

# Se crea una NUEVA clase (PersonajeConProperty) en vez de reescribir Personaje,
# para no generar ambigüedad con la clase Personaje ya usada en la Clase 5.

class PersonajeConProperty:
    def __init__(self, nombre, corazones=10, corazones_max=10):
        self.nombre = nombre
        self.corazones_max = corazones_max
        # Atributo "privado" (_corazones): todo acceso externo debe pasar
        # obligatoriamente por el getter/setter definidos abajo.
        self._corazones = corazones

    @property
    def corazones(self):
        """Getter: permite leer personaje.corazones como si fuera un atributo normal."""
        return self._corazones

    @corazones.setter
    def corazones(self, valor):
        """Setter: valida el valor cada vez que se hace personaje.corazones = algo."""
        if valor < 0:
            self._corazones = 0
        elif valor > self.corazones_max:
            self._corazones = self.corazones_max
        else:
            self._corazones = valor

    @property
    def vivo(self):
        """Propiedad calculada: vivo = True mientras corazones > 0."""
        return self._corazones > 0

    def recibir_ataque(self, daño, atacante):
        if not self.vivo:
            print(f"{self.nombre} ya está muerto, {atacante} no puede hacerle más daño.")
            return

        self.corazones -= daño  # pasa por el setter, que valida el rango
        if not self.vivo:
            print(f"{atacante} atacó a {self.nombre} y le quitó {daño} corazones. {self.nombre} ha MUERTO.")
        else:
            print(f"{atacante} atacó a {self.nombre} y le quitó {daño} corazones. Le quedan {self.corazones} corazones.")

    def estado(self):
        if self.vivo:
            return f"{self.nombre} está vivo con {self.corazones} corazones."
        else:
            return f"{self.nombre} está muerto."


Notch = PersonajeConProperty("Notch")
Notch.recibir_ataque(4, "Esqueleto")
print(Notch.estado())


Notch.corazones = 999  # se limita automáticamente al máximo (10)
print(f"Intento de poner 999 corazones -> queda en: {Notch.corazones}")

Notch.corazones = -50  # se limita automáticamente a 0 (y por lo tanto, muere)
print(f"Intento de poner -50 corazones -> queda en: {Notch.corazones}, ¿vivo? {Notch.vivo}")

# ==============================================================================
# CLASE 6 - PUNTO 2: ABSTRACCIÓN
# ==============================================================================
print("\n===================== CLASE 6 - PUNTO 2: ABSTRACCIÓN =====================\n")

# La abstracción sirve para definir una clase "molde" que dice QUÉ métodos
# debe tener cada clase hija, pero sin decir CÓMO se hacen. Esa clase molde
# no se puede usar directamente (no se puede crear un objeto de ella), solo
# sirve como base para las clases que sí van a heredar de ella.

# Para hacer esto en Python se usa el módulo "abc" (Abstract Base Class):
# - La clase abstracta hereda de ABC.
# - Los métodos que las clases hijas están OBLIGADAS a crear se marcan con
#   el decorador @abstractmethod.
from abc import ABC, abstractmethod


# Figura es una clase ABSTRACTA: representa la idea general de "una figura
# geométrica", pero no una figura en concreto (no existe "una figura" sin
# más, solo existen círculos, cuadrados, etc.)
class Figura(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    # Este método NO tiene implementación (no dice cómo se calcula el área),
    # solo obliga a que toda clase hija de Figura tenga su propio método
    # calcular_area(). Si una clase hija no lo implementa, Python da error.
    @abstractmethod
    def calcular_area(self):
        pass

    # Este sí es un método normal, con implementación. Las clases hijas lo
    # heredan tal cual, sin necesidad de reescribirlo.
    def describir(self):
        print(f"{self.nombre} tiene un área de {self.calcular_area()} unidades cuadradas.")


# Cuadrado SÍ se puede crear como objeto, porque hereda de Figura e
# implementa el método calcular_area() que era obligatorio.
class Cuadrado(Figura):
    def __init__(self, lado):
        super().__init__("Cuadrado")
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado


# Círculo también implementa su propia versión de calcular_area().
class Circulo(Figura):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.radio = radio

    def calcular_area(self):
        return round(3.1416 * (self.radio ** 2), 2)


# Se crean objetos de las clases hijas normalmente.
mi_cuadrado = Cuadrado(4)
mi_circulo = Circulo(3)

mi_cuadrado.describir()
mi_circulo.describir()

# Esta línea de abajo, si se descomenta, daría ERROR, porque Figura es
# abstracta y no se puede instanciar directamente:
# figura_generica = Figura(Genérica)   # TypeError: no se puede instanciar