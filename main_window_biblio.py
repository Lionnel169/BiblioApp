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
from PyQt5.QtCore import pyqtSlot, QDate, QItemSelectionModel

from Ui_main_window_biblio import Ui_MainWindowBiblio

from modele_biblio import Livre, ModeleTableBiblio                            

# ============================================================================
# Classes  
# ============================================================================
class MainWindowBiblio(QMainWindow, Ui_MainWindowBiblio): 
    
    def __init__(self,parent=None): 
        super(MainWindowBiblio,self).__init__(parent) 
        self.setupUi(self)
        self.nomFichierBiblio = None
        self.modeleTableBiblio = ModeleTableBiblio([])        
        self.treeViewBook.setModel(self.modeleTableBiblio)
        self.treeViewBook.selectionModel().selectionChanged.connect(self.on_treeViewBook_selectionChanged)
    
        self.modificationAEnregistrer(False) 
        self.dateEditYear.setMinimumDate(QDate(101,1,1)) 
        self.dateEditYear.setSpecialValueText(" ")
        self.doubleSpinBoxPrice.setMinimum(-0.01)
        self.doubleSpinBoxPrice.setSpecialValueText(" ")
        self.effaceLivre()
        self.pushButtonDelete.setEnabled(False)

        self.pushButtonSauvegarder.setEnabled(False) 

        for lineEdit in (self.lineEditTitre, 
                         self.lineEditAuteur,
                         self.lineEditEditeur): 
            lineEdit.textEdited.connect(self.declareSaisieEnCours)
        self.comboBoxGenre.currentIndexChanged.connect(self.declareSaisieEnCours)
        self.dateEditAnnee.dateChanged.connect(self.declareSaisieEnCours)
        self.plainTextEditResume.textChanged.connect(self.declareSaisieEnCours)
        self.doubleSpinBoxPrix.valueChanged.connect(self.declareSaisieEnCours)

    def declareSaisieEnCours(self): 
        self.pushButtonNouveau.setEnabled(False)
        saisieValide = len(self.lineEditTitre.text().strip()) > 0
        self.pushButtonSauvegarder.setEnabled(saisieValide)
        
    def modificationAEnregistrer(self,fichierNonEnregistre): 
        self.fichierNonEnregistre = fichierNonEnregistre
        titre = "BiblioApp"
        if self.nomFichierBiblio is not None:
            titre += " - " + self.nomFichierBiblio
        if self.fichierNonEnregistre:
            titre += " *"
        self.setWindowTitle(titre)
        self.action_Save.setEnabled(fichierNonEnregistre)
        self.pushButtonNouveau.setEnabled(True) 
        self.pushButtonSauvegarder.setEnabled(False)
                                              
    def on_treeViewBook_selectionChanged(self,selected,deselected): 
        indexesSelection = selected.indexes()
        if self.pushButtonSauvegarder.isEnabled(): 
            reponse = QMessageBox.question(self,'Confirmation',
                                           'Abandonner la saisie en cours ?',
                                           QMessageBox.Yes,QMessageBox.No)
            if reponse == QMessageBox.No:
                selectionModel = self.treeViewLivres.selectionModel()     
                selectionModel.selectionChanged.disconnect( 
                                    self.on_treeViewLivres_selectionChanged) 
                selectionModel.select(selected,QItemSelectionModel.Deselect)
                selectionModel.select(deselected,QItemSelectionModel.Select)
                selectionModel.selectionChanged.connect(
                                    self.on_treeViewLivres_selectionChanged)
                return
        
        if len(indexesSelection) == 0:
            self.effaceLivre()
            self.pushButtonDelete.setEnabled(False)
        else:
            self.indexSelection = indexesSelection[0]
            self.indiceLivreSelectionne = self.indexSelection.row()
            self.afficheLivre(self.modeleTableBiblio.livres[self.indiceLivreSelectionne])
            self.ushButtonDelete.setEnabled(True)
            self.pushButtonNouveau.setEnabled(True)
        
        self.pushButtonSauvegarder.setEnabled(False)
        
    def effaceLivre(self):
        for lineEdit in (self.lineEditTitle,
                         self.lineEditAuthor,
                         self.lineEditEditor):
            lineEdit.setText("")
        self.comboBoxKind.setCurrentIndex(0)
        self.plainTextEditResumed.setPlainText("")
        self.dateEditYear.setDate(self.dateEditYear.minimumDate()) 
        self.doubleSpinBoxPrice.setValue(self.doubleSpinBoxPrice.minimum())
    
    def afficheLivre(self,livre): 
        self.lineEditTitle.setText(livre.titre)
        self.lineEditAuthor.setText(livre.auteur)
        self.comboBoxKind.setCurrentText(livre.genre)
        self.lineEditEditor.setText(livre.editeur)
        self.dateEditYear.setDate(QDate(livre.annee,1,1))
        self.plainTextEditResumed.setPlainText(livre.resume)
        self.doubleSpinBoxPrice.setValue(livre.prix)
    
    def closeEvent(self,event):
        if not self.fichierNonEnregistre:
            event.accept()
        else:
            messageConfirmation = "Are you sure to quit BiblioApp ?"
            reply = QMessageBox.question(self,"Confirmation",messageConfirmation,\
                                     QMessageBox.Yes, QMessageBox.No)
            if reply == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()

    # Method "Open file"
    @pyqtSlot()
    def on_actionOuvrir_triggered(self):
        if self.fichierNonEnregistre: 
            messageConfirmation = "Modifications en cours.\n\n"        \
                                  "Êtes-vous sûr de vouloir continuer" \
                                  " sans enregistrer le fichier ?"
            reponse = QMessageBox.question(self,"Confirmation",
                           messageConfirmation,QMessageBox.Yes,QMessageBox.No)
            if reponse == QMessageBox.No:
                return
        (nomFichierBiblio,filtre) = QFileDialog.getOpenFileName(
                                   self,"Ouvrir fichier bibliothèque",
                                   filter="Bibliothèque (*.bib);; Tout (*.*)")
        if nomFichierBiblio:
            self.modeleTableBiblio = ModeleTableBiblio.creeDepuisFichier( 
                                                             nomFichierBiblio) 
            self.treeViewLivres.setModel(self.modeleTableBiblio)
            self.treeViewLivres.selectionModel().selectionChanged.connect(
                                      self.on_treeViewLivres_selectionChanged)
            self.nomFichierBiblio = nomFichierBiblio
            self.modificationAEnregistrer(False)
    
    # Save 
    @pyqtSlot()
    def on_action_Save_triggered(self):
        if self.nomFichierBiblio is None: 
            (nomFichierBiblio,filtre) = QFileDialog.getSaveFileName(self,"Enregistrer fichier",filter="Bibliothèque (*.bib);; Tout (*.*)")
            if nomFichierBiblio:
                self.nomFichierBiblio = nomFichierBiblio
        if self.nomFichierBiblio is not None: 
            self.modeleTableBiblio.enregistreDansFichier(self.nomFichierBiblio)
            self.modificationAEnregistrer(False)
   
    # New 
    @pyqtSlot()
    def on_pushButtonNouveau_clicked(self): 
        self.treeViewLivres.selectionModel().clearSelection()
        self.effaceLivre()
        self.pushButtonSauvegarder.setEnabled(False)
        
    @pyqtSlot()
    def on_pushButtonSauvegarder_clicked(self): 
        livre = Livre( titre = self.lineEditTitle.text(),
                       auteur = self.lineEditAuthor.text(),
                       editeur = self.lineEditEditor.text(),
                       genre = self.comboBoxKind.currentText(),
                       annee = self.dateEditYear.date().year(),
                       resume = self.plainTextEditResumed.toPlainText(),
                       prix = self.doubleSpinBoxPrice.value() )
        selectionModel = self.treeViewLivres.selectionModel()
        indexesSelectionnes = selectionModel.selectedRows()
        if len(indexesSelectionnes) == 0: 
            self.modeleTableBiblio.ajouteLivre(livre) 
            self.on_pushButtonNouveau_clicked()
        else: 
            indiceLivreSelectionne = indexesSelectionnes[0].row() 
            self.modeleTableBiblio.remplaceLivre(indiceLivreSelectionne,
                                                 livre)
        self.modificationAEnregistrer(True)
    
    @pyqtSlot()
    def on_pushButtonDelete_clicked(self): 
        selectionModel = self.treeViewLivres.selectionModel()
        indexesSelectionnes = selectionModel.selectedRows()
        if len(indexesSelectionnes) > 0:
            indiceLivreSelectionne = indexesSelectionnes[0].row()
            self.modeleTableBiblio.supprimeLivre(indiceLivreSelectionne)
            self.modificationAEnregistrer(True)
    
    # Method "Quit"
    @pyqtSlot()
    def on_action_Exit_triggered(self):
        self.close()
    
   
            