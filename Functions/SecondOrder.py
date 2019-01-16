import math

"""
Fonction du second ordre de paramètre K, z, w0 et reversed.
"""
class SecondOrder:

    def __init__(self, K, w0, z, reversed = False):
        self.K = K
        self.w0 = w0
        self.z = z
        self.reversed = reversed

    #Renvoie le gain en fonction de w
    def getGain(self, w):
        value = 20*math.log10(self.K)-10*math.log10(math.pow(2*self.z/self.w0*w,2)+math.pow(1-1/(math.pow(self.w0,2))*w*w,2))
        if self.reversed:
            return -value
        else:
            return value

    #Renvoie la phase en fonction de w
    def getPhase(self,w):
        value = -math.atan2(2*self.z/self.w0*w,1-1/(self.w0*self.w0)*w*w)/math.pi*180
        if self.reversed:
            return -value
        else:
            return value

    #Renvoie la value de l'asymptote du gain en fonction de w
    def getGainAsymptote(self, w):
        value = 0
        if(self.z <= 1):
            if(w <= self.w0):
                value = 20*math.log10(self.K)
            else:
                value = 20*math.log10(self.K)+40*math.log10(self.w0)-40*math.log10(w)
        else:
            a = 1
            b = 2*self.z*self.w0
            c = self.w0**2
            delta = (b**2)-(4*a*c)
            w1 = -(-b+math.sqrt(delta))/(2*a)
            w2 = -(-b-math.sqrt(delta))/(2*a)
            if(w < w1):
                value = 20*math.log10(self.K)
            elif(w < w2):
                value = 20*math.log10(self.K)+20*math.log10(w1)-20*math.log10(w)
            else:
                value = 20*math.log10(self.K)+20*math.log10(w1)+20*math.log10(w2)-40*math.log10(w)
        if self.reversed:
            return -value
        else:
            return value

    def getPhaseAsymptote(self, w):
        value = 0
        if(self.z <= 1):
            if(w < self.w0):
                value = 0
            else:
                value = -180
        else:
            a = 1
            b = 2*self.z/self.w0*math.pow(self.w0,2)
            c = math.pow(self.w0,2)
            delta = b**2-4*a*c
            w1 = -(-b+math.sqrt(delta))/(2*a)
            w2 = -(-b-math.sqrt(delta))/(2*a)
            if(w < w1):
                value = 0
            elif(w < w2):
                value = -90
            else:
                value = -180
        if self.reversed:
            return -value
        else:
            return value
