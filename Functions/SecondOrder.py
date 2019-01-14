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
