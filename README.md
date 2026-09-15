# Entregable POO en Python — Herencia, MRO, Encapsulamiento y Abstracción

Repositorio con los ejercicios de Programación Orientada a Objetos (POO) en Python, desarrollados como entregable de clase. Cubre herencia simple, herencia múltiple, MRO (Method Resolution Order), encapsulamiento con `@property` y abstracción con `ABC`/`@abstractmethod`.

## 📂 Contenido del repositorio

| Archivo | Descripción |
|---|---|
| `ENTREGABLE.py` | Entregable principal: Clase 3 (herencia múltiple y MRO) y Clase 5-6 (personaje con vida, mobs, encapsulamiento y abstracción). |
| `actividad_abstractmethod.py` | Actividad adicional sobre `@abstractmethod`, aplicada a un sistema de cálculo de salario de empleados. |

## 🧩 `ENTREGABLE.py`

### Clase 3 - Punto 1: Herencia múltiple
Clases `Abuela`, `Abuelo` y `Nieto` (que hereda de ambas), mostrando cómo Python resuelve el MRO cuando una clase hija hereda de dos clases padre distintas.

### Clase 3 - Punto 2: Cadena de herencia lineal
Clases `A` → `B` → `C` → `D` → `E` → `F` → `G`, cada una heredando de la anterior, para ver un MRO simple y lineal.

### Clase 3 - Punto 3: Herencia múltiple (herencia en diamante)
Clases `A2` a `G2` con una estructura de **herencia en diamante** (varias ramas que comparten un ancestro común y luego se vuelven a juntar), mostrando cómo el algoritmo **C3 linearization** de Python calcula el MRO para evitar ambigüedades.

### Clase 5 - Ejercicio 1: Personaje con vida
Clase `Personaje` con sistema de corazones (vida), que puede recibir ataques y morir cuando llega a 0 corazones.

### Clase 5 - Ejercicio 2: Mobs que atacan al personaje
Clase base `Mob` y sus subclases (`Creeper`, `Zombie`, `Esqueleto`, `Enderman`), cada una con su propio daño, sonido y forma de ataque (polimorfismo), atacando a un `Personaje`.

### Clase 6 - Punto 1: Getters, Setters y `@property`
Clase `PersonajeConProperty`: encapsula el atributo `corazones` mediante un getter y un setter (`@property` / `@corazones.setter`) que valida que nunca sea negativo ni supere el máximo. El atributo `vivo` pasa a ser una **propiedad calculada** a partir de los corazones, en vez de una bandera manual.

### Clase 6 - Punto 2: Abstracción
Clase abstracta `Figura` (hereda de `ABC`) con el método obligatorio `calcular_area()` marcado con `@abstractmethod`. Las clases `Cuadrado` y `Circulo` heredan de `Figura` e implementan su propia versión de `calcular_area()`. `Figura` no se puede instanciar directamente.

## 🧩 `actividad_abstractmethod.py`

Actividad complementaria sobre `@abstractmethod`, aplicada a un sistema de nómina:

- **`Empleado`** (clase abstracta, `ABC`): define los métodos obligatorios `calcular_bono()` y `calcular_descuento()`, y un método concreto `calcular_salario_final()` que los usa.
- **`EmpleadoTiempoCompleto`**: bono según años de antigüedad, descuento fijo del 8%.
- **`EmpleadoPorHoras`**: bono por horas extra (más de 160 horas), sin descuento.
- **`Gerente`** (hereda de `EmpleadoTiempoCompleto`): mismo cálculo que un empleado de tiempo completo, más un bono extra según el tamaño de su equipo.

Al final se calcula el total de la nómina sumando el salario final de todos los empleados.

## ▶️ Cómo ejecutar

Requiere Python 3 (no usa librerías externas, solo el módulo estándar `abc`).

```bash
python3 ENTREGABLE.py
python3 actividad_abstractmethod.py
```

## 📚 Temas de POO cubiertos

- Herencia simple y múltiple
- MRO (Method Resolution Order) y herencia en diamante
- Polimorfismo
- Encapsulamiento (`@property`, getters y setters)
- Abstracción (`ABC`, `@abstractmethod`)