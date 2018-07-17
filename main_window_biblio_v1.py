# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 06:27:54 2018

@author: ldupo
"""
# main_window_biblio.py
# Connection signal-slot with decorator

# ============================================================================
# Imports 
# ============================================================================
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtCore import pyqtSlot, QDate

from Ui_main_window_biblio import Ui_MainWindowBiblio

from modele_biblio import Livre, ModeleTableBiblio                            

# ============================================================================
# Classes  
# ============================================================================
class MainWindowBiblio(QMainWindow, Ui_MainWindowBiblio): 
    
    def __init__(self,parent=None): 
        super(MainWindowBiblio,self).__init__(parent) 
        self.setupUi(self)
        # Code test à supprimer
        livresTest = [ Livre("Une étude en rouge", "Conan Doyle", "Hachette", "Detective Story",
                 1888, "...", 13.),
           Livre("Le Horla", "Guy de Maupassant", "Gallimard", "Fantastic",
                 1887, "...", 11.),
           Livre("Napoléon", "André Castelot", "Perrin", "Biography",
                 2008, "...", 24.)]
        
        self.modeleTableBiblio = ModeleTableBiblio(livresTest)
        self.treeViewBook.setModel(self.modeleTableBiblio)
        self.treeViewBook.selectionModel().selectionChanged.connect(self.on_treeViewBook_selectionChanged)
    
    def on_treeViewBook_selectionChanged(self,selected,deselected): 
        indexesSelection = selected.indexes()
        if len(indexesSelection) > 0:
            self.indexSelection = indexesSelection[0]
            self.indiceLivreSelectionne = self.indexSelection.row()
            self.afficheLivre(self.modeleTableBiblio.livres[
            self.indiceLivreSelectionne])
    
    def afficheLivre(self,livre): 
        self.lineEditTitle.setText(livre.titre)
        self.lineEditAuthor.setText(livre.auteur)
        self.comboBoxKind.setCurrentText(livre.genre)
        self.lineEditEditor.setText(livre.editeur)
        self.dateEditYear.setDate(QDate(livre.annee,1,1))
        self.plainTextEditResumed.setPlainText(livre.resume)
        self.doubleSpinBoxPrice.setValue(livre.prix)
    
    # Method "Open file"
    @pyqtSlot()
    def on_actionOpen_triggered(self):
        # TODO: Temporary trace to replace by reading of file 
        (nameFileBiblio,filtre) = QFileDialog.getOpenFileName(self,\
                                  "Open file directory",
                                  filter="Directory (*.bib);; All (*.*)")
        
        if nameFileBiblio:
            QMessageBox.information(self,"Trace","File to open: \n\%s"%nameFileBiblio)
        
    # Method "Quit"
    @pyqtSlot()
    def on_action_Exit_triggered(self):
        self.close()
    
    def closeEvent(self,event):
        messageConfirmation = "Are you sure to quit BiblioApp ?"
        reply = QMessageBox.question(self,"Confirmation",messageConfirmation,\
                                     QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

            