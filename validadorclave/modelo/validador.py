from abc import ABC, abstractmethod

class ReglaValidacion(ABC):

    def __init__(self, _longitud_esperada: int):
        self._longitud_esperada: int = _longitud_esperada

    def _validar_longitud(self, clave: str) -> bool:
        return len(clave) > self._longitud_esperada

    def _contiene_mayuscula(self, clave: str) -> bool:
       for c in clave:
            if c.isupper():
                return True
            else:
                return False


    def _contiene_minuscula(self, clave: str) -> bool:
        for c in clave:
            if c.islower():
                return True
            else:
                return False

    def _contiene_numero(self, clave: str) -> bool:
        for c in clave:
            if c.isdigit():
                return True
            else:
                return False

    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        pass


class ReglaValidacionGanimedes(ReglaValidacion):

    def contiene_caracter_especial(self, clave: str) -> bool:
        caracteres_especiales = "@_#$%"
        for c in clave:
            if c in caracteres_especiales:
                return True
            else:
                return False


    def es_valida(self, clave: str) -> bool:
        if (self._validar_longitud(clave) and
            self._contiene_mayuscula(clave) and
            self._contiene_minuscula(clave) and
            self._contiene_numero(clave) and
            self.contiene_caracter_especial(clave)):
            return True
        return False


class ReglaValidacionCalisto(ReglaValidacion):

    def contiene_calisto(self):
        pass

    def es_valida(self, clave: str) -> bool:
        pass

class Validador:
     def es_valida(self):
         pass