#"01/34/6789 12:45:78"
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
                    if UltimoViaje._Horario[0:9] == horario[0:9]:
                        
                        HoraVieja=int(UltimoViaje._Horario[11:12]) + 1
                        MinutoViejo=int(UltimoViaje._Horario[14:15])
                        SegundoViejo=int(UltimoViaje._Horario[17:18])
                      
                        HoraNueva=int(horario[11:12])
                        MinutoNuevo=int(horario[14:15])
                        SegundoNuevo=int(horario[17:18])
                        
                        if HoraNueva > HoraVieja:
                            return self.PagarConCosto(colectivo, horario, self._CostoComun)
                        if HoraNueva < HoraVieja:
                            return self.PagarConCosto(colectivo, horario, self._CostoTransbordo)        
                        
                        
                        if MinutoNuevo > MinutoViejo:
                            return self.PagarConCosto(colectivo, horario, self._CostoComun)
                        if MinutoNuevo < MinutoViejo:
                            return self.PagarConCosto(colectivo, horario, self._CostoTransbordo)                                
                        
                        
                        if SegundoNuevo > SegundoViejo:
                            return self.PagarConCosto(colectivo, horario, self._CostoComun)
                        if SegundoNuevo <= SegundoViejo:
                            return self.PagarConCosto(colectivo, horario, self._CostoTransbordo)                                
                        
                    
                    if int(UltimoViaje._Horario[9:10]) == 23 and TestearFecha(UltimoViaje._Horario,horario):
                        HoraVieja= 0
                        MinutoViejo=int(UltimoViaje._Horario[14:15])
                        SegundoViejo=int(UltimoViaje._Horario[17:18])
                      
                        HoraNueva=int(horario[11:12])
                        MinutoNuevo=int(horario[14:15])
                        SegundoNuevo=int(horario[17:18])
                        
                        if HoraNueva > HoraVieja:
                            return self.PagarConCosto(colectivo, horario, self._CostoComun)
                        
                        if MinutoNuevo > MinutoViejo:
                            return self.PagarConCosto(colectivo, horario, self._CostoComun)
                        if MinutoNuevo < MinutoViejo:
                            return self.PagarConCosto(colectivo, horario, self._CostoTransbordo)                                
                        
                        
                        if SegundoNuevo > SegundoViejo:
                            return self.PagarConCosto(colectivo, horario, self._CostoComun)
                        if SegundoNuevo <= SegundoViejo:
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
    
    
    def TestearFecha (self, HorarioViejo, horario):
        DiaViejo=int(HorarioViejo[0:1])
        MesViejo=int(HorarioViejo[3:4])
        AnoViejo=int(HorarioViejo[6:9])
                      
        DiaNuevo=int(horario[0:1])
        MesNuevo=int(horario[3:4])
        AnoNuevo=int(horario[6:9])
        
        if DiaViejo+1 == DiaNuevo and MesViejo == MesNuevo and AnoViejo == AnoNuevo:
            return True
    
        if DiaNuevo == 1 and MesViejo+1 == MesNuevo and AnoViejo == AnoNuevo:
            return True
    
        if DiaNuevo == 1 and MesNuevo == 1 and AnoViejo+1 == AnoNuevo:
            return True
            
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
    
    def __init__ (self):
        self._Saldo = 0
        self._Registro= []
        self._Viaje = Viaje()
        self._CostoComun = 5.75
        self._CostoTransbordo = 1.90
        self._CostoMedioComun = 2.90
        self._CostoMedioTransbordo = 0.96
    
    def PagarBoleto (self, colectivo, horario):
        if self.ExistenViajes:
            UltimoViaje = self._Registro[-1]
            if UltimoViaje._Monto != self._CostoTransbordo and UltimoViaje._Monto != self._CostoMedioTransbordoTransbordo:
                if UltimoViaje._Linea != colectivo._Linea:
                    if UltimoViaje._Horario[0:9] == horario[0:9]:
                        
                        HoraVieja=int(UltimoViaje._Horario[11:12]) + 1
                        MinutoViejo=int(UltimoViaje._Horario[14:15])
                        SegundoViejo=int(UltimoViaje._Horario[17:18])
                      
                        HoraNueva=int(horario[11:12])
                        MinutoNuevo=int(horario[14:15])
                        SegundoNuevo=int(horario[17:18])
                        
                        if HoraNueva > HoraVieja:
                            return self.PagarConCosto(colectivo, horario, self._CostoComun)
                        if HoraNueva < HoraVieja:
                            return self.PagarConCosto(colectivo, horario, self._CostoTransbordo)        
                        
                        
                        if MinutoNuevo > MinutoViejo:
                            return self.PagarConCosto(colectivo, horario, self._CostoComun)
                        if MinutoNuevo < MinutoViejo:
                            return self.PagarConCosto(colectivo, horario, self._CostoTransbordo)                                
                        
                        
                        if SegundoNuevo > SegundoViejo:
                            return self.PagarConCosto(colectivo, horario, self._CostoComun)
                        if SegundoNuevo <= SegundoViejo:
                            return self.PagarConCosto(colectivo, horario, self._CostoTransbordo)                                
                        
                    
                    if int(UltimoViaje._Horario[9:10]) == 23 and TestearFecha(UltimoViaje._Horario,horario):
                        HoraVieja= 0
                        MinutoViejo=int(UltimoViaje._Horario[14:15])
                        SegundoViejo=int(UltimoViaje._Horario[17:18])
                      
                        HoraNueva=int(horario[11:12])
                        MinutoNuevo=int(horario[14:15])
                        SegundoNuevo=int(horario[17:18])
                        
                        if HoraNueva > HoraVieja:
                            return self.PagarConCosto(colectivo, horario, self._CostoComun)
                        
                        if MinutoNuevo > MinutoViejo:
                            return self.PagarConCosto(colectivo, horario, self._CostoComun)
                        if MinutoNuevo < MinutoViejo:
                            return self.PagarConCosto(colectivo, horario, self._CostoTransbordo)                                
                        
                        
                        if SegundoNuevo > SegundoViejo:
                            return self.PagarConCosto(colectivo, horario, self._CostoComun)
                        if SegundoNuevo <= SegundoViejo:
                            return self.PagarConCosto(colectivo, horario, self._CostoTransbordo)  
            
        
        return self.PagarConCosto(colectivo, horario, self._CostoComun)

    
    def PagarConCosto (self, colectivo, horario, costo):
        if int(horario[11:12]) >= 0 and int(horario[11:12]) < 6:
            if costo == self._CostoComun:
                costo = self._CostoMedioComun
            else:
                costo = self._CostoMedioTransbordo
            
        
        if self._Saldo > costo:
            self._Saldo = self._Saldo - costo
            self._Viaje.setValores (colectivo, horario, costo)
            self._Registro.append(self._Viaje)
            print("Pasaste\n")
            return True
        else:
            print("No Pasaste\n")
            return False





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
