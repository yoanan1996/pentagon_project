class Pentagon:
    """
    Clase para calcular el área de un pentágono.
    Fórmula: A = (1.5 * a * l) / 2
    donde 'a' es el apotema y 'l' es el lado.
    """

    def __init__(self, apotema: float, lado: float):
        """
        Constructor del Pentágono.
        :param apotema: Apotema del pentágono.
        :param lado: Longitud de un lado del pentágono.
        """
        self.apotema = apotema
        self.lado = lado

    def calcular_area(self) -> float:
        """
        Método para calcular el área del pentágono.
        :return: Área del pentágono.
        """
        return (1.5 * self.apotema * self.lado) / 2


if __name__ == "__main__":
    # Ejemplo de uso
    pentagon = Pentagon(5, 10)  # Apotema = 5, Lado = 10
    print(f"El área del pentágono es: {pentagon.calcular_area():.2f}")
