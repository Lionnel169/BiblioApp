# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 06:27:54 2018

@author: ldupo
"""
# main_window_biblio.py

from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
                            
class MainWindowBiblio(QMainWindow): 
    
    def __init__(self): 
        super(MainWindowBiblio,self).__init__() 
        self.resize(300,150) 
        self.setWindowTitle("BiblioApp") 
        self.centralWidget = QWidget(self) 
        self.setCentralWidget(self.centralWidget)
        self.label = QLabel("Titre",self.centralWidget) 
        self.lineEditTitre = QLineEdit(self.centralWidget)
        self.lineEditTitre.move(80,0) 
        self.pushButtonOK = QPushButton("OK",self.centralWidget)
        self.pushButtonOK.move(20,40)
        self.pushButtonOK.clicked.connect(self.onPushButtonOKClicked)
        
        
    def onPushButtonOKClicked(self):
        QMessageBox.information(self,"Info","Titre : "+self.lineEditTitre.text())
