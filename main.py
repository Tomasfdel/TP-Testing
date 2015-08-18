class Tarjeta:
    
    def __init__ (self):
        self._Saldo = 0
        self._Registro= []
        self._Viaje = Viaje()

    
    def Recarga (self, monto):
        if monto = 196:
            self._Saldo = self._Saldo + 230
        else:
            if monto = 368:
                self._Saldo = self._Saldo + 460
            else:
                self._Saldo = self._Saldo + monto


    def Saldo (self):
        return self._Saldo


    def ViajesRealizados (self):
        return self._Registro

    
    def PagarBoleto (self, colectivo, horario):
        
        


class TarjetaMedioBoleto (Tarjeta) :
        
    def PagarBoleto (self, colectivo, horario):
        #SI EL HORARIO ESTA FUERA DEL RANGO, PAGA COMUN
        #ELSE PAGA DESCONTADO




class Colectivo:
    def __init__ (self, empresa, linea, interno):
        self._Empresa = empresa
        self._Linea = linea
        self._Interno = interno



class Viaje:
    def __init__ (self):
        self.setValores(0,0,0)
        
    def setValores (self, colectivo, horario, monto):
        self._Colectivo = colectivo
        self._Horario = horario
        self._Monto = monto
