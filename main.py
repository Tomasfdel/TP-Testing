class Tarjeta:
    
    def __init__ (self):
        self._Saldo = 0
        self._Registro= []
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
        if self.Viajes():
            if (self._Registro[-1])._Monto != self._CostoTransbordo:
                if (self._Registro[-1])._Colectivo._Linea != colectivo._Linea:
                    if (self._Registro[-1])._Horario[0:10] == horario[0:10]:
                        HoraVieja=int((self._Registro[-1])._Horario[11:13]) + 1
                        MinutoViejo=int((self._Registro[-1])._Horario[14:16])
                        SegundoViejo=int((self._Registro[-1])._Horario[17:19])
                      
                        HoraNueva=int(horario[11:13])
                        MinutoNuevo=int(horario[14:16])
                        SegundoNuevo=int(horario[17:19])
                        
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
                        
                        
                    HoraVieja=int((self._Registro[-1])._Horario[11:13])
                    if HoraVieja == 23 and self.TestearFecha((self._Registro[-1])._Horario,horario):
                        HoraVieja= 0
                        MinutoViejo=int((self._Registro[-1])._Horario[14:16])
                        SegundoViejo=int((self._Registro[-1])._Horario[17:19])
                      
                        HoraNueva=int(horario[11:13])
                        MinutoNuevo=int(horario[14:16])
                        SegundoNuevo=int(horario[17:19])
                        
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
            (self._Registro).append(Viaje(colectivo, horario, costo))
            return True
        else:
            return False
    
    
    def TestearFecha (self, HorarioViejo, horario):
        DiaViejo=int(HorarioViejo[0:2])
        MesViejo=int(HorarioViejo[3:5])
        AnoViejo=int(HorarioViejo[6:10])
                      
        DiaNuevo=int(horario[0:2])
        MesNuevo=int(horario[3:5])
        AnoNuevo=int(horario[6:10])
        
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

    def Viajes (self):
        return len(self._Registro)
        



class TarjetaMedioBoleto (Tarjeta) :
    
    def __init__ (self):
        self._Saldo = 0
        self._Registro= []
        self._CostoComun = 5.75
        self._CostoTransbordo = 1.90
        self._CostoMedioComun = 2.90
        self._CostoMedioTransbordo = 0.96
    
    def PagarBoleto (self, colectivo, horario):
        if self.Viajes():
            if (self._Registro[-1])._Monto != self._CostoTransbordo and (self._Registro[-1])._Monto != self._CostoMedioTransbordo:
                if (self._Registro[-1])._Colectivo._Linea != colectivo._Linea:
                    if (self._Registro[-1])._Horario[0:10] == horario[0:10]:
                        HoraVieja=int((self._Registro[-1])._Horario[11:13]) + 1
                        MinutoViejo=int((self._Registro[-1])._Horario[14:16])
                        SegundoViejo=int((self._Registro[-1])._Horario[17:19])
                      
                        HoraNueva=int(horario[11:13])
                        MinutoNuevo=int(horario[14:16])
                        SegundoNuevo=int(horario[17:19])
                        
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
                        
                    HoraVieja=int((self._Registro[-1])._Horario[11:13])
                    if HoraVieja == 23 and self.TestearFecha((self._Registro[-1])._Horario,horario):
                        HoraVieja= 0
                        MinutoViejo=int((self._Registro[-1])._Horario[14:16])
                        SegundoViejo=int((self._Registro[-1])._Horario[17:19])
                      
                        HoraNueva=int(horario[11:13])
                        MinutoNuevo=int(horario[14:16])
                        SegundoNuevo=int(horario[17:19])
                        
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
        if int(horario[11:13]) >= 0 and int(horario[11:13]) < 6:
            if costo == self._CostoComun:
                costo = self._CostoMedioComun
            else:
                costo = self._CostoMedioTransbordo
            
        
        if self._Saldo > costo:
            self._Saldo = self._Saldo - costo
            self._Registro.append(Viaje(colectivo, horario, costo))
            return True
        else:
            return False





class Colectivo:
    def __init__ (self, empresa, linea, interno):
            self._Empresa = empresa
            self._Linea = linea
            self._Interno = interno


class Viaje:
    def __init__ (self, colectivo, horario, monto):
        self._Colectivo = colectivo
        self._Horario = horario
        self._Monto = monto
