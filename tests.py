from main import *

#Verifica que las recargas a la tarjeta funcionen incluyendo los casos que dan credito extra.
def test_Recarga(): 
	tarj1=Tarjeta()
	assert tarj1._Saldo == 0
	tarj1.Recarga(196)
	assert tarj1._Saldo == 230
	tarj1.Recarga(368)
	assert tarj1._Saldo == 690
	tarj1.Recarga(10)
	assert tarj1._Saldo == 700

#Verifica que no se realice transbordo si se toma dos veces el mismo colectivo en el lapso de una hora.
def test_DosViajesIguales():
	tarj2=Tarjeta()
	tarj2.Recarga(20)
	bondi21=Colectivo("Mixta", 101, 3)
	tarj2.PagarBoleto(bondi21,"03/06/1997 05:30:00")
	assert tarj2._Saldo == 14.25
	tarj2.PagarBoleto(bondi22,"03/06/1997 05:30:10")
	assert tarj2._Saldo == 8.50
	
#Verifica el funcionamiento del transbordo.	
def test_Transbordo():
	tarj3=Tarjeta()
	tarj3.Recarga(20)
	bondi31=Colectivo("Mixta", 101, 3)
	bondi32=Colectivo("Mixta", 102, 2)
	tarj3.PagarBoleto(bondi31,"03/06/1997 05:30:00")
	assert tarj3._Saldo == 14.25
	tarj3.PagarBoleto(bondi32,"03/06/1997 06:10:00")
	assert tarj3._Saldo == 12.35
	
#Verifica que no sea posible tomarse un colectivo sin saldo suficiente en la tarjeta.
def test_SinSaldo():
	tarj4=Tarjeta()
	tarj4.Recarga(10)
	bondi41=Colectivo("Semtur", 132, 3)
	tarj4.PagarBoleto(bondi41,"10/06/2015 23:30:00")
	assert tarj2._Saldo == 4.25
	assert tarj2.PagarBoleto(bondi41,"10/06/2015 23:40:00") == False
	assert tarj2._Saldo == 4.25

#Verifica que se pueda tomar un colectivo de distinta linea al anterior pero no de la misma en caso de tener saldo suficiente
# para un viaje transbordo pero no para uno comun.
def test_TransbordoSiFunciona():
	tarj5=Tarjeta()
	tarj5.Recarga(10)
	bondi51=Colectivo("Mixta",101, 3)
	bondi52=Colectivo("Mixta",106, 3)
	tarj5.PagarBoleto(bondi51,"23/05/2010 17:45:00")
	assert tarj5._Saldo == 4.25
	assert tarj5.PagarBoleto(bondi51,"23/05/2010 18:40:00") == False
	tarj5.PagarBoleto(bondi52,"23/05/2010 18:41:00")
	assert tarj5._Saldo == 2.35
	
#Verifica el funcionamiento de la funcion ViajesRealizados.
def test_ViajesRealizados():
	tarj6=Tarjeta()
	tarj6.Recarga(15)
	bondi61=Colectivo("Mixta",101, 3)
	bondi62=Colectivo("Mixta",106, 3)
	tarj6.PagarBoleto(bondi61,"09/12/2014 10:45:00")
	tarj6.PagarBoleto(bondi62,"09/12/2014 11:15:00")
	Lista=tarj6.ViajesRealizados()
	assert Lista[0]._Colectivo == bondi61
	assert Lista[0]._Horario == "09/12/2014 10:45:00"
	assert Lista[0]._Monto == 5.75
	assert Lista[1]._Colectivo == bondi62
	assert Lista[1]._Horario == "09/12/2014 11:15:00"
	assert Lista[1]._Monto == 1.90
	
#Verifica el funcionamiento del transbordo en el caso en el que durante el lapso de la hora cambia el año.
def test_TransbordoFechasDistintas():
	tarj7=Tarjeta()
	tarj7.Recarga(13)
	bondi71=Colectivo("Mixta",101, 3)
	bondi72=Colectivo("Mixta",102, 3)
	tarj7.PagarBoleto(bondi71,"31/12/2010 23:45:00")
	assert tarj7._Saldo == 7.25
	tarj7.PagarBoleto(bondi72,"01/01/2011 00:15:00")
	assert tarj7._Saldo == 5.35
	
#Verifica que solo se realice un transbordo si se realizan mas viajes en una hora.
def test_TresViajesSeguidos():
	tarj8=Tarjeta()
	tarj8.Recarga(20)
	bondi81=Colectivo("Mixta",101, 3)
	bondi82=Colectivo("Mixta",102, 3)
	bondi83=Colectivo("Mixta",103, 3)
	tarj8.PagarBoleto(bondi81,"05/09/2015 12:45:00")
	assert tarj8._Saldo == 14.25
	tarj8.PagarBoleto(bondi82,"05/09/2015 13:15:00")
	assert tarj8._Saldo == 12.35
	tarj8.PagarBoleto(bondi83,"05/09/2015 13:35:00")
	assert tarj8._Saldo == 6.60

#Verifica que el medio boleto funcione en el horario correspondiente.
def test_MedioBoletoHorasDistintas():
	tarj9=TarjetaMedioBoleto()
	tarj9.Recarga(20)
	bondi91=Colectivo("Mixta",101, 3)
	tarj9.PagarBoleto(bondi91,"05/09/2015 15:00:00")
	assert tarj9._Saldo == 17.10
	tarj9.PagarBoleto(bondi91,"06/09/2015 03:00:00")
	assert tarj9._Saldo == 11.35

#Verifica el funcionamiento del medio boleto en los viajes de tipo transbordo.
def test_MedioBoletoTransbordo():
	tarj10=TarjetaMedioBoleto()
	tarj10.Recarga(20)
	bondi101=Colectivo("Mixta",101, 3)
	bondi102=Colectivo("Mixta",102, 3)
	tarj10.PagarBoleto(bondi101,"05/09/2015 15:00:00")
	assert tarj10._Saldo == 17.10
	tarj10.PagarBoleto(bondi102,"05/09/2015 15:15:00")
	assert tarj10._Saldo == 16.14



