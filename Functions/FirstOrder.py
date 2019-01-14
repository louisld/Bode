import math

"""
Fonction du premier ordre de paramètre K, tau et reversed.
"""
class FirstOrder:

    def __init__(self, K, tau, reversed = False):
        self.K = K
        self.tau = tau
        self.reversed = reversed

    #Renvoie le gain en fonction de w
    def getGain(self, w):
        value = 20*math.log10(self.K)-10*math.log10(1+(w*self.tau)*(w*self.tau))
        if self.reversed:
            return -value
        else:
            return value

    #Renvoie la phase en fonction de w
    def getPhase(self,w):
        value = -math.atan(self.tau*w)/math.pi*180
        if self.reversed:
            return -value
        else:
            return value
