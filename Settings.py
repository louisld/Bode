# conding: utf-8

import tkinter as tk
import numpy as np
from Modals.FirstOrderModal import FirstOrderModal
from Modals.SecondOrderModal import SecondOrderModal
from Functions.FirstOrder import FirstOrder
from Functions.SecondOrder import SecondOrder
from Graph import Graph

"""
Fenêtre principal permettant d'ajouter des fonctions et d'afficher le graphe.
"""
class Settings:

    def __init__(self):

        #Initialisation des fenêtres
        self.window = tk.Tk()
        self.graph = Graph()

        #Valeurs par défaut
        self.gainValue = {
            "gainWmin": -4,
            "gainWmax": 4,
            "gaindBmin": -50,
            "gaindBmax": 50
        }

        self.phaseValue = {
            "phaseWmin": -4,
            "phaseWmax": 4,
            "phasedBmin": -50,
            "phasedBmax": 50
        }
        self.valeurGainWmin = tk.StringVar()
        self.valeurGainWmax = tk.StringVar()
        self.valeurGaindBmin = tk.StringVar()
        self.valeurGaindBmax = tk.StringVar()
        self.valeurPhaseWmin = tk.StringVar()
        self.valeurPhaseWmax = tk.StringVar()
        self.valeurPhasedBmin = tk.StringVar()
        self.valeurPhasedBmax = tk.StringVar()

        self.listeOptions = ("1er ordre", "2nd ordre")
        self.fonctionSelector = tk.StringVar()

        #Tableau contenant les fonctions à afficher
        self.tFunctions = []

        self.ligneFunction = 4

    """
    Met à jour les paramêtres.
    Calcul les valeurs pour le graphe.
    Affiche le graphe.
    """
    def updateSettings(self):
        self.gainValue["GainWmin"] = self.valeurGainWmin.get()
        self.gainValue["GainWmax"] = self.valeurGainWmax.get()
        self.gainValue["GaindBmin"] = self.valeurGaindBmin.get()
        self.gainValue["GaindBmax"] = self.valeurGaindBmax.get()
        self.phaseValue["PhaseWmin"] = self.valeurPhaseWmin.get()
        self.phaseValue["PhaseWmax"] = self.valeurPhaseWmax.get()
        self.phaseValue["PhasedBmin"] = self.valeurPhasedBmin.get()
        self.phaseValue["PhasedBmax"] = self.valeurPhasedBmax.get()

        #Création d'un nouveau graphe
        del self.graph
        self.graph = Graph()

        #Tableaux contenant les valeurs des corubes
        tPhase = []
        tGain = []
        tGainAsympt = []
        tPhaseAsympt = []
        tx = []
        #Création des abcisses sur une échelle logarithmique
        tx = np.logspace(int(self.gainValue["GainWmin"]), int(self.gainValue["GainWmax"]), num=400)
        #On calcule l'abcisse pour chaque ordonnée
        for i in tx:
            gain = 0
            phase = 0
            gainAsympt = 0
            phaseAsympt = 0
            #On fait la somme des ordonnées pour chaque fonction
            for function in self.tFunctions:
                gain += function.getGain(i)
                phase += function.getPhase(i)
                gainAsympt += function.getGainAsymptote(i)
                phaseAsympt += function.getPhaseAsymptote(i)
            tGain.append(gain)
            tPhase.append(phase)
            tGainAsympt.append(gainAsympt)
            tPhaseAsympt.append(phaseAsympt)


        self.graph.update(tGain, tPhase, tGainAsympt, tPhaseAsympt, tx)
        self.graph.draw()


    """
    Dessine la fenêtre.
    """
    def drawSettingsWindow(self):
        self.window.title("Réglage des diagrammes de Bode")

        #Valeurs pour l'affichage
        padx=8
        pady=8
        entryWidth=5

        #Réglages pour le diagramme de gain
        frameGain = tk.LabelFrame(self.window, text="Réglage du diagramme de gain", padx=padx, pady=pady)
        frameGain.grid(row=1, column=1)

        labelGainWmin = tk.Label(frameGain, text="Wmin : ", padx=padx, pady=pady).grid(row=1, column=1)
        entryGainWmin = tk.Entry(frameGain, bg='white', width=entryWidth, textvariable=self.valeurGainWmin).grid(row=1, column=2)
        self.valeurGainWmin.set(self.gainValue["gainWmin"])
        labelGainWmax = tk.Label(frameGain, text="Wmax : ", padx=padx, pady=pady).grid(row=2, column=1)
        entryGainWmax = tk.Entry(frameGain, bg='white', width=entryWidth, textvariable=self.valeurGainWmax).grid(row=2, column=2)
        self.valeurGainWmax.set(self.gainValue["gainWmax"])
        labelGaindBmin = tk.Label(frameGain, text="dBmin : ", padx=padx, pady=pady).grid(row=1, column=3)
        entryGaindBmin = tk.Entry(frameGain, bg='white', width=entryWidth, textvariable=self.valeurGaindBmin, state='disabled').grid(row=1, column=4)
        self.valeurGaindBmin.set(self.gainValue["gaindBmin"])
        labelGaindBmax = tk.Label(frameGain, text="dBmax : ", padx=padx, pady=pady).grid(row=2, column=3)
        entryGaindBmax = tk.Entry(frameGain, bg='white', width=entryWidth, textvariable=self.valeurGaindBmax, state='disabled').grid(row=2, column=4)
        self.valeurGaindBmax.set(self.gainValue["gaindBmax"])

        #Réglages pour le diagramme de phase
        framePhase = tk.LabelFrame(self.window, text="Réglage du diagramme de phase", padx=padx, pady=pady)
        framePhase.grid(row=1, column=2)

        labelPhaseWmin = tk.Label(framePhase, text="Wmin : ", padx=padx, pady=pady).grid(row=1, column=1)
        entryPhaseWmin = tk.Entry(framePhase, bg='white', width=entryWidth, textvariable=self.valeurPhaseWmin, state='disabled').grid(row=1, column=2)
        self.valeurPhaseWmin.set(self.phaseValue["phaseWmin"])
        labelPhaseWmax = tk.Label(framePhase, text="Wmax : ", padx=padx, pady=pady).grid(row=2, column=1)
        entryPhaseWmax = tk.Entry(framePhase, bg='white', width=entryWidth, textvariable=self.valeurPhaseWmax, state='disabled').grid(row=2, column=2)
        self.valeurPhaseWmax.set(self.phaseValue["phaseWmax"])
        labelPhasedBmin = tk.Label(framePhase, text="dBmin : ", padx=padx, pady=pady).grid(row=1, column=3)
        entryPhasedBmin = tk.Entry(framePhase, bg='white', width=entryWidth, textvariable=self.valeurPhasedBmin, state='disabled').grid(row=1, column=4)
        self.valeurPhasedBmin.set(self.phaseValue["phasedBmin"])
        labelPhasedBmax = tk.Label(framePhase, text="dBmax : ", padx=padx, pady=pady).grid(row=2, column=3)
        entryPhasedBmax = tk.Entry(framePhase, bg='white', width=entryWidth, textvariable=self.valeurPhasedBmax, state='disabled').grid(row=2, column=4)
        self.valeurPhasedBmax.set(self.phaseValue["phasedBmax"])

        valider = tk.Button(self.window, padx=padx, pady=pady, text="Nouveau graphe", command=self.updateSettings).grid(row=2, column=1, columnspan=2)
        ajouter = tk.Button(self.window, padx=padx, pady=pady, text="Ajouter une fonction", command=self.addFunction).grid(row=3, column=1)

        self.fonctionSelector.set(self.listeOptions[0])
        om = tk.OptionMenu(self.window, self.fonctionSelector, *self.listeOptions).grid(row=3, column=2)

        self.window.protocol("WM_DELETE_WINDOW", self.end)
        self.window.mainloop()

    """
    Ajoute une fonction à la liste des fonctions.
    L'ajout se fait via une modale.
    """
    def addFunction(self):
        padx=8
        pady=8

        if self.fonctionSelector.get() == self.listeOptions[0]: # Premier ordre
            firstOrderModal = FirstOrderModal(self.window)
            firstOrder = FirstOrder(*firstOrderModal.result)
            self.tFunctions.append(firstOrder)

            K, tau, inversed = firstOrderModal.result
            frameFirstOrder = tk.LabelFrame(self.window, text="1er ordre", padx=padx, pady=pady)
            labelFirstOrder = tk.Label(frameFirstOrder, text=" K=" + str(K) + "   τ=" + str(tau) + "   inversée=" + str(inversed), padx=padx, pady=pady).grid(row=1, column=1)
            logoFirstOrder = tk.PhotoImage(file="Assets/FirstOrder.pgm")
            logoLabelFirstOrder = tk.Label(frameFirstOrder, image=logoFirstOrder)
            logoLabelFirstOrder.photo = logoFirstOrder
            logoLabelFirstOrder.grid(row=1, column=2)
            frameFirstOrder.grid(row=self.ligneFunction, column=1, columnspan=2)
            self.ligneFunction += 1
        if self.fonctionSelector.get() == self.listeOptions[1]: #Second ordre
            secondOrderModal = SecondOrderModal(self.window)
            secondOrder = SecondOrder(*secondOrderModal.result)
            self.tFunctions.append(secondOrder)

            K, z, w0, inversed = secondOrderModal.result
            frameSecondOrder = tk.LabelFrame(self.window, text="2nd ordre", padx=padx, pady=pady)
            labelSecondOrder = tk.Label(frameSecondOrder, text=" K=" + str(K) + "   z=" + str(z) + "   ω0="+ str(w0) + "   inversée=" + str(inversed), padx=padx, pady=pady).grid(row=1, column=1)
            logoSecondOrder = tk.PhotoImage(file="Assets/SecondOrder.pgm")
            logoLabelSecondOrder = tk.Label(frameSecondOrder, image=logoSecondOrder)
            logoLabelSecondOrder.photo = logoSecondOrder
            logoLabelSecondOrder.grid(row=1, column=2)
            frameSecondOrder.grid(row=self.ligneFunction, column=1, columnspan=2)

    """
    Destruction de la fenêtre
    """
    def end(self):
        del self.graph
        self.window.destroy()
