class Tarjeta:
    
    def __init__ (self):
        self._Saldo = 0
        self._Registro= []
        self._Viaje = Viaje()
        self._CostoComun = 5.75
        self._CostoTransbordo = 1.90
        
    def Recarga (self, monto):
        if monto == 196:
            self._Saldo = self._Saldo + 230
        else:
            if monto == 368:
                self._Saldo = self._Saldo + 460
            else:
                self._Saldo = self._Saldo + monto


    def PagarBoleto (self, colectivo, horario):
        if self.ExistenViajes:
            UltimoViaje = self._Registro[-1]
            if UltimoViaje._Monto != self._CostoTransbordo:
                if UltimoViaje._Linea != colectivo._Linea:
                    FechaVieja = UltimoViaje._Horario[0:9]
                    FechaActual = horario[0:9]
                    if FechaVieja == FechaActual:
                        #ACA VA LA COSA DE LAS HORAS
                        return self.PagarConCosto(colectivo, horario, self._CostoTransbordo)
        
        return self.PagarConCosto(colectivo, horario, self._CostoComun)
        
        
                
    def PagarConCosto (self, colectivo, horario, costo):
        if self._Saldo > costo:
            self._Saldo = self._Saldo - costo
            self._Viaje.setValores (colectivo, horario, costo)
            self._Registro.append(self._Viaje)
            print("Pasaste\n")
            return True
        else:
            print("No Pasaste\n")
            return False
    

    def Saldo (self):
        return self._Saldo

    def ViajesRealizados (self):
        return self._Registro

    def ExistenViajes (self):
        if len(self._Registro) > 0:
            return True
        else:
            return False
        



class TarjetaMedioBoleto (Tarjeta) :
    def PagarBoleto (self, colectivo, horario):
        print ("Still under development")
        return True
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
