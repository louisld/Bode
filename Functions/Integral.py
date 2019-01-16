import math

"""
Fonction intégrale de paramètre K et reversed.
"""
class Integral:

    def __init__(self, K, reversed = False):
        self.K = K
        self.reversed = reversed

    #Renvoie le gain en fonction de w
    def getGain(self, w):
        value = 20*math.log10(self.K)-20*math.log10(w)
        if self.reversed:
            return -value
        else:
            return value

    #Renvoie la phase en fonction de w
    def getPhase(self,w):
        return -90

    #Renvoie la value de l'asymptote du gain en fonction de w
    def getGainAsymptote(self, w):
        value = 20*math.log10(self.K)-20*math.log10(w)
        if self.reversed:
            return -value
        else:
            return value

    def getPhaseAsymptote(self, w):
        return -90
