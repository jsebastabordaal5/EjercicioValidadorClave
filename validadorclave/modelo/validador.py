from abc import ABC, abstractmethod

class ReglaValidacion(ABC):

    def __init__(self, _longitud_esperada: int):
        self._longitud_esperada: int = _longitud_esperada


    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        pass

    def _validar_longitud(self, clave: str) -> bool:
        if len(clave) > self._longitud_esperada:
            return True
        else:
            return False


    def _contiene_mayuscula(self, clave: str) -> bool:
        if any(caracter.isupper() for caracter in clave):
            return True
        else:
            return False


    def _contiene_minuscula(self, clave: str) -> bool:
        if any(caracter.islower() for caracter in clave):
            return True
        else:
            return False

    def _contiene_numero(self, clave: str) -> bool:
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