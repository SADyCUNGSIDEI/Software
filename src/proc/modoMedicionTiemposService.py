import commandSender
import threading
import placaService

def setPines(pin1, pin2):
	commandSender.setPinesMedTiempo(pin1, pin2)
	placaService.__estados["seteado"] = True

def medir(callback):
	placaService.__estados["midiendo"] = True

	def toThread():
		res = commandSender.readLine() #TODO: cuantos bytes traemos?

		microSegundos = 0

		for c in res:
			microSegundos = microSegundos*10
			microSegundos = microSegundos + int(c)

		callback(microSegundos)

	t = threading.Thread(target = toThread)
	t.start()

