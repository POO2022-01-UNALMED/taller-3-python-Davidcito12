class TV:
    _numTV = 0

    def __init__(self, Marca, Estado):
        self._marca = Marca
        self._estado = Estado
        self._canal = 1
        self._volumen = 1
        self._precio = 500
        self._control = None
        TV._numTV += 1

    @classmethod
    def setNumTv(cls,Nuevo):
        cls._numTV = Nuevo

    def getMarca(self):
        return self._marca

    def getEstado(self):
        return self._estado

    def getCanal(self):
        return self._canal

    def getControl(self):
        return self._control

    def getVolumen(self):
        return self._volumen

    def getPrecio(self):
        return self._precio

    def setCanal(self, NuevoCanal):
        if NuevoCanal > 0 and NuevoCanal < 121 and self._estado == True:
            self._canal = NuevoCanal

    def setVolumen(self, NuevoVolumen):
        if NuevoVolumen >= 0 and NuevoVolumen <= 7 and self._estado == True:
            self._volumen = NuevoVolumen

    def setMarca(self, NuevaMarca):
        self._marca = NuevaMarca

    def setPrecio(self, NuevoPrecio):
        self._precio = NuevoPrecio

    def setControl(self, NuevoControl):
        self._control = NuevoControl

    def turnOn(self):
        self._estado = True

    def turnOff(self):
        self._estado = False

    def volumenUp(self):
        if self._volumen < 7 and self._estado == True:
            self._volumen += 1

    def volumenDown(self):
        if self._volumen > 0 and self._estado == True:
            self._volumen -= 1

    def canalUp(self):
        if self._canal < 120 and self._estado == True:
            self._canal += 1

    def canalDown(self):
        if self._canal > 1 and self._estado == True:
            self._canal -= 1
