import math, time

class Faehre(object):
    " Klasse fuer Mondfaehre "
    def __init__(self):
        self.MondBeschleunigung=1.635
        self.Hoehe=4000.0
        self.Geschw=0.0
        self.Beschleunigung = self.MondBeschleunigung
        self.Tank = 5000
        self.SchubFaktor = 0.04
        
    def calcHoehe(self, Beschleunigung, altGeschw,  sekunden,  altHoehe):
        return -0.5*Beschleunigung*sekunden*sekunden  + altHoehe + altGeschw*sekunden

    def calcGeschwindigkeit(self, Beschleunigung, sekunden,  altGeschw):
        return -Beschleunigung*sekunden + altGeschw


    def bremse(self,  Schub):
        if (Schub<0.0): Schub=0.0
        if (Schub>100.0): Schub=100.0
        self.Beschleunigung = self.MondBeschleunigung - Schub * self.SchubFaktor
        if (Schub <= self.Tank) :
            self.Tank -= Schub
        else:
            Schub = self.Tank
            self.Tank = 0
        self.Hoehe  = self.calcHoehe(self.Beschleunigung, self.Geschw, 1.0, self.Hoehe)
        self.Geschw = self.calcGeschwindigkeit(self.Beschleunigung, 1.0, self.Geschw)

    def istTankVoll(self): 
        return self.Tank>0

    
    def zeigeStatus(self, Sekunden):
        print "Zeit: %d  Hoehe: %5.1f  Geschwindigkeit: %5.1f  Treibstoff:  %5.1f " % ( Sekunden, self.Hoehe, -self.Geschw, self.Tank )


def ZahlenEingabe( defvalue, text = ""):
    " Funktion fuer Zahleneingabe. Erlaubt Eingabe von 'Return', dann wird default bzw alter Wert benutzt "
    line = raw_input( text )

    try:
        val = int(line)
    except:
        val = defvalue

    return val


def Bewertung(Geschw):
    " Bewertung der Landung "
    Geschw = math.fabs(Geschw)
    if (Geschw<5.0) :
        print "Sehr gelungene Landung!"
    elif (Geschw<10.0) :
        print "Sauber gelandet!"
    elif (Geschw<20.0) :
        print "Verletzt gelandet!"
    else:
        print "Ein Krater wird Ihren Namen tragen!"

if __name__ == "__main__" :
    tFaehre = Faehre()
    Sekunden = 0
    Schub=0.0
    while ( tFaehre.Hoehe > 0):

        Sekunden += 1
        tFaehre.bremse(Schub)
        tFaehre.zeigeStatus(Sekunden)

        if ( tFaehre.Hoehe <= 0.0) :
            Bewertung(tFaehre.Geschw )

        elif (tFaehre.istTankVoll()) :
            prompt = "Wieviel Schub (0-100, %d ):" % ( Schub ) 
            Schub = ZahlenEingabe(Schub, prompt)

        else : # Tank leer, dann faellt das Ding ...
            Schub = 0.0
            time.sleep(1.) 
