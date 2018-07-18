# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 06:27:54 2018

@author: ldupo
"""
# main_window_biblio.py
# Connection signzl-slot with decorator

from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, \
                            QPushButton, QMessageBox, QHBoxLayout, QVBoxLayout \
                            
from PyQt5.QtCore import QMetaObject, pyqtSlot
                            
class MainWindowBiblio(QMainWindow): 
    
    def __init__(self): 
        super(MainWindowBiblio,self).__init__() 
        self.resize(300,150) 
        self.setWindowTitle("BiblioApp") 
        
        self.centralWidget = QWidget(self) 
        self.setCentralWidget(self.centralWidget)
        
        self.label = QLabel("Titre",self.centralWidget) 
        
        self.lineEditTitre = QLineEdit(self.centralWidget)
        
        self.pushButtonOK = QPushButton("OK",self.centralWidget)
        
        self.hBoxLayout = QHBoxLayout()
        self.hBoxLayout.addWidget(self.label)
        self.hBoxLayout.addWidget(self.lineEditTitre)
        
        self.vBoxLayout = QVBoxLayout(self.centralWidget)
        self.vBoxLayout.addLayout(self.hBoxLayout)
        self.vBoxLayout.addStretch()
        
        self.hBoxLayout2 = QHBoxLayout()
        self.hBoxLayout2.addStretch()
        self.hBoxLayout2.addWidget(self.pushButtonOK)
        self.hBoxLayout2.addStretch()
        self.vBoxLayout.addLayout(self.hBoxLayout2)
        
        # connection signal-slot
        self.pushButtonOK.setObjectName("pushButtonOK")
        QMetaObject.connectSlotsByName(self)
        
    # Method format => on_objectName_signalName
    # ObjectName = pushButtonOK
    # signalName = clicked 
    #                  on_pushButtonOK_clicked 
    # @pyqtSlot() can use some arguments 
    # @pyqtSlot(int,name='on_spinBoxChoix_valueChanged')
    #   def on_spinBoxChoix_valueChanged_int(self,i):
    #   print ("nombre entier : %d" % i)
    @pyqtSlot()    
    def on_pushButtonOK_clicked(self):
        QMessageBox.information(self,"Info","Titre : "+self.lineEditTitre.text())
