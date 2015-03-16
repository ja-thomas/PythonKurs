import random, threading, time

class Aufzug(object):
	lck = threading.Lock()

	def __init__(self, stockwerke, stockwerk):
		self.stockwerke = stockwerke
		self.stockwerk = stockwerk

	def wird_gerufen(self, person, person_stockwerk, ziel_stockwerk):
		self.lck.acquire()
		time.sleep(abs(self.stockwerk - person_stockwerk) / 2)
		print "%s ruft den Aufzug in den %i Stock" %(person, person_stockwerk)
		time.sleep(1)
		print "Aufzug in Stockwerk %i angekommen" %person_stockwerk
		time.sleep(1)
		print "%s steigt in den Aufzug" %person
		time.sleep(abs(person_stockwerk - ziel_stockwerk))
		print "%s ist in Stockwerk %i angekommen" %(person, ziel_stockwerk)
		self.stockwerk = ziel_stockwerk
		self.lck.release()
	pass	



class Person(threading.Thread):

	def __init__(self, name, stockwerk, Aufzug):
		threading.Thread.__init__(self, name = name)
		self.name = name
		self.stockwerk = stockwerk
		self.Aufzug = Aufzug

	def run(self):
		c = 1
		while(c < random.randint(1,5)):
			time.sleep(random.randint(1,10))
			ziel_stockwerk = random.randint(1, self.Aufzug.stockwerke)
			if ziel_stockwerk == self.stockwerk:
				pass
			else:
				self.Aufzug.wird_gerufen(person = self.name ,person_stockwerk = self.stockwerk, ziel_stockwerk = ziel_stockwerk)
				self.stockwerk = ziel_stockwerk
			c += 1		
		ziel_stockwerk = 0
		self.Aufzug.wird_gerufen(person = self.name ,person_stockwerk = self.stockwerk, ziel_stockwerk = ziel_stockwerk)
		print "%s geht nach Hause" %self.name
	pass


a = Aufzug(10, 1)

p1 = Person("Peter", 5, a)
p2 = Person("Sabine", 2, a)
p3 = Person("Hans", 5, a)

p1.start()
p2.start()
p3.start()