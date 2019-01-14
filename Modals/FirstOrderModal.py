# coding: utf-8

import tkinter as tk
import tkinter.simpledialog as tksd

"""
Modale pour créer une fonction du premier ordre.
"""
class FirstOrderModal(tksd.Dialog):

    def body(self, master):
        logoFirstOrder = tk.PhotoImage(file="Assets/FirstOrder.pgm")
        logoLabelFirstOrder = tk.Label(master, image=logoFirstOrder)
        logoLabelFirstOrder.photo = logoFirstOrder
        logoLabelFirstOrder.grid(row=0, column=1, padx=8, pady=8)
        tk.Label(master, text="K: ").grid(row=1)
        tk.Label(master, text="τ: ").grid(row=2)

        self.e1 = tk.Entry(master, bg="white")
        self.e2 = tk.Entry(master, bg="white")

        self.e1.grid(row=1, column=1)
        self.e2.grid(row=2, column=1)

        self.inversed = tk.IntVar()
        self.cb = tk.Checkbutton(master, text="Inversé ?", variable=self.inversed)
        self.cb.grid(row=3, columnspan=2, sticky=tk.W)
        return self.e1

    def apply(self):
        K = int(self.e1.get())
        tau = int(self.e2.get())
        inversed = self.inversed.get()
        self.result = K, tau, inversed
