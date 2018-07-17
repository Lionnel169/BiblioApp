# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 10:03:47 2018

@author: ldupo
"""
# ============================================================================
# Imports 
# ============================================================================

from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex, QVariant

from collections import namedtuple

import json

# ============================================================================
# Attributs  
# ============================================================================
Livre = namedtuple('Livre', ('titre', 'auteur', 'editeur', 'genre',
                             'annee', 'resume', 'prix') )

# ============================================================================
# Classes  
# ============================================================================
class ModeleTableBiblio(QAbstractTableModel):
  
    def __init__(self,livres):
        super(ModeleTableBiblio,self).__init__()
        self.titresColonnes = ("Titre", "Auteur", "Éditeur")
        self.livres = livres

    # Titre des colonnes
    def headerData(self,section,orientation,role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.titresColonnes[section]
        return QVariant()
 
    # Nombre de colonnes
    def columnCount(self,parent):
        return len(self.titresColonnes)
   
    # Nombre de lignes
    def rowCount(self,parent):
        return len(self.livres)

    # L'attribut d'indice y du livre d'indice x 
    def data(self,index,role): 
        if role == Qt.DisplayRole and index.isValid():
            return (self.livres[index.row()][index.column()])
        return QVariant()

    def enregistreDansFichier(self,nomFichierBiblio): 
        with open(nomFichierBiblio,'w') as f:
            json.dump(self.livres,f)

    @staticmethod
    def creeDepuisFichier(nomFichierBiblio): 
        with open(nomFichierBiblio,'r') as f:
            attributsLivres = json.load(f)
        livres = [Livre(*attrLivre) for attrLivre in attributsLivres]
        return ModeleTableBiblio(livres)
    
    def ajouteLivre(self,livre): 
        indiceLivre = len(self.livres)
        self.beginInsertRows(QModelIndex(),indiceLivre,indiceLivre)
        self.livres.append(livre)
        self.endInsertRows()
  
    def supprimeLivre(self,indiceLivre): 
        self.beginRemoveRows(QModelIndex(),indiceLivre,indiceLivre)
        del self.livres[indiceLivre]
        self.endRemoveRows()     

    def remplaceLivre(self,indiceLivre,livre): 
        self.livres[indiceLivre] = livre
        self.dataChanged.emit(self.createIndex(indiceLivre,0),
                              self.createIndex(indiceLivre,2))
        