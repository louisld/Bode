# coding: utf-8

import tkinter as tk
import tkinter.simpledialog as tksd

"""
Modale pour créer une fonction du seconde ordre.
"""
class SecondOrderModal(tksd.Dialog):

    def body(self, master):
        logoSecondOrder = tk.PhotoImage(file="Assets/SecondOrder.pgm")
        logoLabelSecondOrder = tk.Label(master, image=logoSecondOrder)
        logoLabelSecondOrder.photo = logoSecondOrder
        logoLabelSecondOrder.grid(row=0, column=1, padx=8, pady=8)
        tk.Label(master, text="K: ").grid(row=1)
        tk.Label(master, text="z: ").grid(row=2)
        tk.Label(master, text="ω0: ").grid(row=3)

        self.e1 = tk.Entry(master, bg="white")
        self.e2 = tk.Entry(master, bg="white")
        self.e3 = tk.Entry(master, bg="white")

        self.e1.grid(row=1, column=1)
        self.e2.grid(row=2, column=1)
        self.e3.grid(row=3, column=1)

        self.inversed = tk.IntVar()
        self.cb = tk.Checkbutton(master, text="Inversé ?", variable=self.inversed)
        self.cb.grid(row=4, columnspan=2, sticky=tk.W)
        return self.e1

    def apply(self):
        K = int(self.e1.get())
        z = int(self.e2.get())
        w0 = int(self.e3.get())
        inversed = self.inversed.get()
        self.result = K, w0, z, inversed
