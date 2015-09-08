from main import *

#Revisa si se carga saldo EXTRA y que si se sube dos veces al mismo colectivo no cobre transbordo.
def test1(): 
	tarj1=Tarjeta()
	tarj1.Recarga(196)
	assert tarj1._Saldo == 230
	tarj1.Recarga(368)
	assert tarj1._Saldo == 690
	tarj1.Recarga(10)
	assert tarj1._Saldo == 700
	cole1 = Colectivo("Semtur", 153, 1)
	tarj1.PagarBoleto(cole1,"07/09/2015 17:58:01")
	tarj1.PagarBoleto(cole1,"07/09/2015 18:30:00")
	assert tarj1._Saldo == 688.50
   

#Revisa el transbordo en una Tarjeta Medio Boleto, con una hora fuera de su horario de costo reducido.
def test2():
	tarj2=TarjetaMedioBoleto()
	tarj2.Recarga(20)
	bondi21=Colectivo("Mixta", 101, 3)
	bondi22=Colectivo("Mixta", 102, 2)
	tarj2.PagarBoleto(bondi21,"03/06/1997 05:30:00")
	assert tarj2._Saldo == 14.25
	tarj2.PagarBoleto(bondi22,"03/06/1997 06:10:00")
	assert tarj2._Saldo == 13.29
	

#Revisa un transbordo con días de fechas, mes y año distinto. Luego se fija si no se puede subir a otro
#colectivo porque ya transbordó antes y no tiene saldo suficiente.
def test3():
	tarj3=Tarjeta()
	tarj3.Recarga(13)
	bondi31=Colectivo("Mixta",101, 3)
	bondi32=Colectivo("Mixta",102, 3)
	bondi33=Colectivo("Mixta",103, 3)
	tarj3.PagarBoleto(bondi31,"31/12/2010 23:45:00")
	tarj3.PagarBoleto(bondi32,"01/01/2011 00:15:00")
	assert tarj3._Saldo == 5.35
	assert tarj3.PagarBoleto(bondi33,"01/01/2011 00:30:00") == False
	

#Revisa que si después de subir a un primer colectivo, te subas a otro igual sin tener saldo suficiente,
#te deje subir a otro de una línea distinta porque el saldo sí alcanza para un transbordo.
def test4():
	tarj4=Tarjeta()
	tarj4.Recarga(10)
	bondi41=Colectivo("Mixta",101, 3)
	bondi42=Colectivo("Mixta",106, 3)
	tarj4.PagarBoleto(bondi41,"23/05/2010 17:45:00")
	assert tarj4.PagarBoleto(bondi41,"23/05/2010 18:40:00") == False
	tarj4.PagarBoleto(bondi42,"23/05/2010 18:41:00")
	assert tarj4._Saldo == 2.35
	


#Revisa si la función ViajesRealizados devuelve el Registro de viajes correctamente.
def test5():
	tarj5=Tarjeta()
	tarj5.Recarga(15)
	bondi51=Colectivo("Mixta",101, 3)
	bondi52=Colectivo("Mixta",106, 3)
	tarj5.PagarBoleto(bondi51,"09/12/2014 10:45:00")
	tarj5.PagarBoleto(bondi52,"09/12/2014 11:15:00")
	Lista=tarj5.ViajesRealizados()
	assert Lista[0]._Colectivo == bondi51
	assert Lista[0]._Horario == "09/12/2014 10:45:00"
	assert Lista[0]._Monto == 5.75
	assert Lista[1]._Colectivo == bondi52
	assert Lista[1]._Horario == "09/12/2014 12:15:00"
	assert Lista[1]._Monto == 1.90
