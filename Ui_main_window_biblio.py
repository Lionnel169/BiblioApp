# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window_biblio.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindowBiblio(object):
    def setupUi(self, MainWindowBiblio):
        MainWindowBiblio.setObjectName("MainWindowBiblio")
        MainWindowBiblio.resize(730, 723)
        self.centralwidget = QtWidgets.QWidget(MainWindowBiblio)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.treeViewBook = QtWidgets.QTreeView(self.centralwidget)
        self.treeViewBook.setObjectName("treeViewBook")
        self.gridLayout_2.addWidget(self.treeViewBook, 0, 0, 1, 7)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEditTitle = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditTitle.setObjectName("lineEditTitle")
        self.gridLayout.addWidget(self.lineEditTitle, 0, 1, 1, 3)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEditAuthor = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditAuthor.setObjectName("lineEditAuthor")
        self.gridLayout.addWidget(self.lineEditAuthor, 1, 1, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.comboBoxKind = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxKind.setObjectName("comboBoxKind")
        self.comboBoxKind.addItem("")
        self.comboBoxKind.setItemText(0, "")
        self.comboBoxKind.addItem("")
        self.comboBoxKind.addItem("")
        self.comboBoxKind.addItem("")
        self.comboBoxKind.addItem("")
        self.comboBoxKind.addItem("")
        self.comboBoxKind.addItem("")
        self.comboBoxKind.addItem("")
        self.comboBoxKind.addItem("")
        self.comboBoxKind.addItem("")
        self.gridLayout.addWidget(self.comboBoxKind, 2, 1, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(381, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEditEditor = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditEditor.setObjectName("lineEditEditor")
        self.gridLayout.addWidget(self.lineEditEditor, 3, 1, 1, 3)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.dateEditYear = QtWidgets.QDateEdit(self.groupBox)
        self.dateEditYear.setObjectName("dateEditYear")
        self.gridLayout.addWidget(self.dateEditYear, 4, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(424, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 2, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.plainTextEditResumed = QtWidgets.QPlainTextEdit(self.groupBox)
        self.plainTextEditResumed.setObjectName("plainTextEditResumed")
        self.gridLayout.addWidget(self.plainTextEditResumed, 5, 1, 1, 3)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.doubleSpinBoxPrice = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBoxPrice.setMaximum(9999.99)
        self.doubleSpinBoxPrice.setObjectName("doubleSpinBoxPrice")
        self.gridLayout.addWidget(self.doubleSpinBoxPrice, 6, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(381, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 6, 2, 1, 2)
        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 6)
        spacerItem3 = QtWidgets.QSpacerItem(110, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 2, 0, 1, 1)
        self.pushButtonNew = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonNew.setObjectName("pushButtonNew")
        self.gridLayout_2.addWidget(self.pushButtonNew, 2, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(110, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 2, 2, 1, 1)
        self.pushButtonSave = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.gridLayout_2.addWidget(self.pushButtonSave, 2, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(109, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 2, 4, 1, 1)
        self.pushButtonDelete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.gridLayout_2.addWidget(self.pushButtonDelete, 2, 5, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(110, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 2, 6, 1, 1)
        MainWindowBiblio.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindowBiblio)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 730, 21))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        MainWindowBiblio.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindowBiblio)
        self.statusbar.setObjectName("statusbar")
        MainWindowBiblio.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindowBiblio)
        self.actionOpen.setObjectName("actionOpen")
        self.action_Save = QtWidgets.QAction(MainWindowBiblio)
        self.action_Save.setObjectName("action_Save")
        self.action_Exit = QtWidgets.QAction(MainWindowBiblio)
        self.action_Exit.setObjectName("action_Exit")
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.actionOpen)
        self.menu_file.addAction(self.action_Save)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_Exit)
        self.menubar.addAction(self.menu_file.menuAction())

        self.retranslateUi(MainWindowBiblio)
        QtCore.QMetaObject.connectSlotsByName(MainWindowBiblio)

    def retranslateUi(self, MainWindowBiblio):
        _translate = QtCore.QCoreApplication.translate
        MainWindowBiblio.setWindowTitle(_translate("MainWindowBiblio", "BiblioApp"))
        self.groupBox.setTitle(_translate("MainWindowBiblio", "Details"))
        self.label.setText(_translate("MainWindowBiblio", "Title"))
        self.label_3.setText(_translate("MainWindowBiblio", "Author"))
        self.label_2.setText(_translate("MainWindowBiblio", "Kind of book"))
        self.comboBoxKind.setItemText(1, _translate("MainWindowBiblio", "Biography"))
        self.comboBoxKind.setItemText(2, _translate("MainWindowBiblio", "Fantastic"))
        self.comboBoxKind.setItemText(3, _translate("MainWindowBiblio", "Historic"))
        self.comboBoxKind.setItemText(4, _translate("MainWindowBiblio", "Novel"))
        self.comboBoxKind.setItemText(5, _translate("MainWindowBiblio", "Polar"))
        self.comboBoxKind.setItemText(6, _translate("MainWindowBiblio", "Science Fiction"))
        self.comboBoxKind.setItemText(7, _translate("MainWindowBiblio", "Detective Story"))
        self.comboBoxKind.setItemText(8, _translate("MainWindowBiblio", "Thriller"))
        self.comboBoxKind.setItemText(9, _translate("MainWindowBiblio", "Other"))
        self.label_4.setText(_translate("MainWindowBiblio", "Editor"))
        self.label_5.setText(_translate("MainWindowBiblio", "Publication year"))
        self.dateEditYear.setDisplayFormat(_translate("MainWindowBiblio", "yyyy"))
        self.label_6.setText(_translate("MainWindowBiblio", "Resumed"))
        self.label_7.setText(_translate("MainWindowBiblio", "Price"))
        self.doubleSpinBoxPrice.setSuffix(_translate("MainWindowBiblio", " €"))
        self.pushButtonNew.setText(_translate("MainWindowBiblio", "New"))
        self.pushButtonSave.setText(_translate("MainWindowBiblio", "Save"))
        self.pushButtonDelete.setText(_translate("MainWindowBiblio", "Delete"))
        self.menu_file.setTitle(_translate("MainWindowBiblio", "&File"))
        self.actionOpen.setText(_translate("MainWindowBiblio", "&Open"))
        self.actionOpen.setShortcut(_translate("MainWindowBiblio", "Ctrl+O"))
        self.action_Save.setText(_translate("MainWindowBiblio", "&Save"))
        self.action_Save.setShortcut(_translate("MainWindowBiblio", "Ctrl+S"))
        self.action_Exit.setText(_translate("MainWindowBiblio", "&Exit"))
