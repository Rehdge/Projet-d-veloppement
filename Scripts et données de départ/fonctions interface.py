# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 20:32:21 2017

@author: ajlsi
"""


 
import tkinter as TK
import tkinter.filedialog as FD
import tkinter.messagebox as MB
import Pmw 
import subprocess

 
from tkinter import ttk
 

 
class FileEntry (ttk.Frame):
 
    def __init__ (self, master=None, **kw):
 
        # initialisation de la classe
 
        ttk.Frame.__init__(self, master)
 
        # initialisation des widgets
 
        self.init_widget(**kw)
 
    # fin de fonction
 
 
    def init_widget (self, **kw):
 
        # fonction permettant d'initialiser les objets servant à récupérer les chemin des trois fichiers
 
        self.label = ttk.Label(
 
            self,
 
            text=kw.get(
 
                "label",
 
                "Veuillez sélectionner un fichier, SVP:"
            )
        )
 
        self.file_path = TK.StringVar()
 
        self.entry = ttk.Entry(
 
            self,
 
            textvariable=self.file_path
        )
        
        # Initialisation du bouton "Parcourir"
 
        self.button = ttk.Button(
 
            self,
 
            text="Parcourir",
 
            command=self.slot_browse,
 
            underline=0,
        )
 
        # initialisation de la disposition des différents objets 
 
        self.label.pack(side=TK.TOP, expand=0, fill=TK.X)
 
        self.entry.pack(side=TK.LEFT, expand=1, fill=TK.X)
 
        self.button.pack(side=TK.LEFT, expand=0, fill=TK.NONE, padx=5)
 
    # fin de fonction
 
 
    def slot_browse (self, tk_event=None, *args, **kw):
 
        # chargement du chemin du fichier
 
        _fpath = FD.askopenfilename(filetypes = [('CSV', '*.csv'),('SHP','*.shp')])
 
        # permet de définir le contenu de l'entrée avec la variable de contrôle file_path
 
        self.file_path.set(_fpath)
 
    # fin de fonction
 
 
    def get_path (self):
 
        return self.file_path.get()
 
    # fin de fonction
 
# fin de la classe FileEntry
 
def valid():
    
    #fonction valider : elle donne un accès au menu déroulant contenant les collèges via un bouton "Valider"
    
    # Dans un pemier temps, on récupère le chemin du fichier contenant les nom des collèges
    
    filename = fileentry_college.get_path()
    fichier = open(filename, "r")
    lignes = fichier.readlines()
    fichier.close()

    print(lignes)
    
    # Dans un deuxième temps on crée la liste qui sera contenue dans le menu déroulant
    
    liste=[]
   
    i=0
    for ligne in lignes:
        if i>0:
            listobj = ligne.split(',')
            liste.insert(i,listobj[0])
        i+=1
        
    # Création du menu déroulant    
        
    combo = Pmw.ComboBox(labelpos = 'nw',
        label_text = 'Choisissez le collège :',
        scrolledlist_items = liste,
        listheight = 150)
    combo.pack(padx=5, pady=10)
    

    
def launch():
    
    # Fonction permettant de relier le script, via le bouton "Lancer", à celui de "resultat_shp.py" qui permet le calcul de plus court chemin
    # Malheureusement le lancement du script "reslutat_shp.py" dans QGIS ne fonctionne pas faute de réussir à ouvrir QGIS depuis le script 
     subprocess.call(["C:\Program Files\QGIS Essen\bin\qgis-ltr-grass7.bat", "C:/Users/ajlsi/Desktop/Scripts/resultat_shp.py", "start python fonctions interface.py"])
   
    
    
root = TK.Tk()
Pmw.initialise(root)

# Définition du titre et sous titre de l'interface

 
root.title("Calcul trajet")
 
labelframe = ttk.LabelFrame(
 
    root,
 
    text="Interface",
 
    padding="5px",
)

# Definition des boutons : le premier bouton "Valider" est nommé de la sorte puis rataché à la fonction "valid"
# Le deuxième bouton est d'abord nommé "Lancer" puis rattaché à la fonction "launch" 
 
btn_validation = ttk.Button(
 
    root,
 
    text="Valider",
 
    command=valid,
 
    underline=0,
)

btn_lancer = ttk.Button(
        
        root,
        
        text= "Lancer",
        
        command=launch,
        
        underline=0,
)
 
# Sous éléments de la classe FileEntry 
 
fileentry_eleve = FileEntry(labelframe, label="Fichier adresses élèves :")
 
fileentry_college = FileEntry(labelframe, label="Fichier adresses collège :")
 
fileentry_voirie = FileEntry(labelframe, label="Fichier voirie :")
 
# Initialisation de la disposition du chemin des fichiers dans la classe FileEntry
 
fileentry_eleve.pack(expand=0, fill=TK.X)
 
fileentry_college.pack(expand=0, fill=TK.X)
 
fileentry_voirie.pack(expand=0, fill=TK.X)
 
# labelframe layout inits
 
labelframe.pack(side=TK.TOP, expand=1, fill=TK.BOTH, padx=5, pady=5)
 
# petit extra
 
ttk.Sizegrip(root).pack(
 
    side=TK.RIGHT, expand=0, fill=TK.Y, padx=5, pady=5,
)
 
# bouton valider pour obtenir le menu déroulant et le bouton lancer pour démarrer le calcul de trajet depuis l'interface
 
btn_validation.pack(side=TK.RIGHT, padx=0, pady=5)

btn_lancer.pack(side=TK.RIGHT, padx=0, pady=7)
 
# pour récupérer un chemin de fichier

 
filepath_eleve = fileentry_eleve.get_path()
 
filepath_college = fileentry_college.get_path()
 
filepath_voirie = fileentry_voirie.get_path()
 
# lancement de l'interface
 
root.mainloop()