from abc import ABC, abstractmethod

class ReglaValidacion(ABC):

    def __init__(self, _longitud_esperada: int):
        self._longitud_esperada: int = _longitud_esperada

    def es_valida(self):
        pass

    def _validar_longitud(self):
        pass

    def _contiene_mayuscula(self):
        pass

    def _contiene_minuscula(self):
        pass

    def _contiene_numero(self):
        pass


class ReglaValidacionGanimedes:

    def contiene_caracter_especial(self):
        pass

    def es_valida(self):
        pass


class ReglaValidacionCalisto:

    def contiene_calisto(self):
        pass

    def es_valida(self):
        pass

class Validador:
     def es_valida(self):