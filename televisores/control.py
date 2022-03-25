class Control:
    def __init__(self):
        self._tv = None

    def enlazar(self,Televisor):
        self._tv = Televisor

    def turnOn(self):
        self._tv.turnOn()

    def turnOff(self):
        self._tv.turnOff()

    def canalUp(self):
        self._tv.canalUp()

    def canalDown(self):
        self._tv.canalDown()

    def volumenUp(self):
        self._tv.volumenUp()

    def volumenDown(self):
        self._tv.volumenDown()

    def setCanal(self,NuevoCanal):
        self._tv.setCanal(NuevoCanal)

    def getTv(self):
        return self._tv

    def setTv(self,NuevoTele):
        self._tv = NuevoTele
        self._tv.setControl(self)

