# coding: utf-8

import matplotlib.pyplot as plot
import numpy as np

"""
Classe affichant un graphique matplotlib.
Contient deux subplots.
"""
class Graph:

    def update(self, tGain, tPhase, tGainAsympt, tPhaseAsympt, tx):
        fig,(axGain,axPhase)=plot.subplots(2, 1, sharex=True)

        axGain.semilogx(tx, tGainAsympt, linestyle="dashed", color="green")
        axGain.semilogx(tx, tGain)
        #Définitions des graduations pour le diagramme de Gain
        axGain.grid(b=True,which='major', linewidth=1, axis='x')
        axGain.grid(b=True,which='minor', linewidth=0.5, axis='x')
        axGain.grid(b=True,which='major', linewidth=0.5, axis='y')
        axGain.legend("Gain")
        axGain.set_ylabel("dB")

        axPhase.semilogx(tx, tPhaseAsympt, linestyle="dashed", color="green")
        axPhase.semilogx(tx,tPhase)
        #Définitions des graduations pour le diagramme de Phase
        axPhase.grid(b=True,which='major', linewidth=1, axis='x')
        axPhase.grid(b=True,which='minor', linewidth=0.5, axis='x')
        axPhase.grid(b=True,which='major', linewidth=0.5, axis='y')
        axPhase.legend("Phase")
        axPhase.set_ylabel("°")

        plot.xlabel("ω")

        plot.show()

    def draw(self):
        plot.draw()
