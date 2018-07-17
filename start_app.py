# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

# start_app.py

import sys
from PyQt5.QtWidgets import QApplication
from main_window_biblio import MainWindowBiblio 

app = QApplication(sys.argv) 
mainWindowBiblio = MainWindowBiblio() 
mainWindowBiblio.show() 

rc = app.exec_() 
sys.exit(rc)