# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'json_layout2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_jsonStim(object):
    def setupUi(self, jsonStim):
        jsonStim.setObjectName(_fromUtf8("jsonStim"))
        jsonStim.resize(650, 600)
        self.centralwidget = QtGui.QWidget(jsonStim)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(6, 9, 6, 9)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.paramHorizLayout = QtGui.QHBoxLayout()
        self.paramHorizLayout.setObjectName(_fromUtf8("paramHorizLayout"))
        self.paramFile_Label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.paramFile_Label.sizePolicy().hasHeightForWidth())
        self.paramFile_Label.setSizePolicy(sizePolicy)
        self.paramFile_Label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.paramFile_Label.setObjectName(_fromUtf8("paramFile_Label"))
        self.paramHorizLayout.addWidget(self.paramFile_Label)
        self.paramFile_Box = QtGui.QTextEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.paramFile_Box.sizePolicy().hasHeightForWidth())
        self.paramFile_Box.setSizePolicy(sizePolicy)
        self.paramFile_Box.setMaximumSize(QtCore.QSize(16777215, 30))
        self.paramFile_Box.setObjectName(_fromUtf8("paramFile_Box"))
        self.paramHorizLayout.addWidget(self.paramFile_Box)
        self.paramFile_Button = QtGui.QToolButton(self.centralwidget)
        self.paramFile_Button.setMinimumSize(QtCore.QSize(30, 30))
        self.paramFile_Button.setMaximumSize(QtCore.QSize(30, 30))
        self.paramFile_Button.setObjectName(_fromUtf8("paramFile_Button"))
        self.paramHorizLayout.addWidget(self.paramFile_Button)
        self.gridLayout_2.addLayout(self.paramHorizLayout, 2, 0, 1, 3)
        self.controlHorizLayout = QtGui.QHBoxLayout()
        self.controlHorizLayout.setObjectName(_fromUtf8("controlHorizLayout"))
        self.cancelButton = QtGui.QPushButton(self.centralwidget)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.controlHorizLayout.addWidget(self.cancelButton)
        self.saveButton = QtGui.QPushButton(self.centralwidget)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.controlHorizLayout.addWidget(self.saveButton)
        self.gridLayout_2.addLayout(self.controlHorizLayout, 4, 0, 1, 3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.stimDir_Label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stimDir_Label.sizePolicy().hasHeightForWidth())
        self.stimDir_Label.setSizePolicy(sizePolicy)
        self.stimDir_Label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.stimDir_Label.setObjectName(_fromUtf8("stimDir_Label"))
        self.horizontalLayout.addWidget(self.stimDir_Label)
        self.stimDir_Box = QtGui.QTextEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stimDir_Box.sizePolicy().hasHeightForWidth())
        self.stimDir_Box.setSizePolicy(sizePolicy)
        self.stimDir_Box.setMaximumSize(QtCore.QSize(16777215, 30))
        self.stimDir_Box.setObjectName(_fromUtf8("stimDir_Box"))
        self.horizontalLayout.addWidget(self.stimDir_Box)
        self.stimDir_Button = QtGui.QToolButton(self.centralwidget)
        self.stimDir_Button.setMinimumSize(QtCore.QSize(30, 30))
        self.stimDir_Button.setObjectName(_fromUtf8("stimDir_Button"))
        self.horizontalLayout.addWidget(self.stimDir_Button)
        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 0, 1, 3)
        self.stimTable = QtGui.QTableWidget(self.centralwidget)
        self.stimTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.stimTable.setDragDropOverwriteMode(False)
        self.stimTable.setAlternatingRowColors(True)
        self.stimTable.setIconSize(QtCore.QSize(10, 10))
        self.stimTable.setTextElideMode(QtCore.Qt.ElideRight)
        self.stimTable.setShowGrid(True)
        self.stimTable.setWordWrap(False)


        self.enableCheck = QtGui.QTableWidgetItem()
        self.enableCheck.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        self.enableCheck.setCheckState(QtCore.Qt.Unchecked)
        self.stimTable.setItem(0, 0, self.enableCheck)

        self.stimLine = QtGui.Lin
        self.stimTable.setRowCount(50)
        self.stimTable.setColumnCount(4)
        self.stimTable.setColumnWidth(0, 30)
        self.stimTable.setColumnWidth(1, 300)
        self.stimTable.setColumnWidth(2, 200)
        self.stimTable.setColumnWidth(3, 30)
        self.stimTable.setColumnWidth(4, 30)
        self.stimTable.setObjectName(_fromUtf8("stimTable"))
        item = QtGui.QTableWidgetItem()
        self.stimTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.stimTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.stimTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.stimTable.setHorizontalHeaderItem(3, item)
        self.stimTable.horizontalHeader().setCascadingSectionResizes(True)
        self.stimTable.horizontalHeader().setDefaultSectionSize(208)
        self.stimTable.horizontalHeader().setMinimumSectionSize(30)
        self.stimTable.horizontalHeader().setStretchLastSection(False)
        self.stimTable.verticalHeader().setVisible(False)
        self.gridLayout_2.addWidget(self.stimTable, 0, 0, 1, 3)
        self.trialRatio_grid = QtGui.QGridLayout()
        self.trialRatio_grid.setObjectName(_fromUtf8("trialRatio_grid"))
        self.probeSMinus_Box = QtGui.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probeSMinus_Box.sizePolicy().hasHeightForWidth())
        self.probeSMinus_Box.setSizePolicy(sizePolicy)
        self.probeSMinus_Box.setMaximumSize(QtCore.QSize(50, 30))
        self.probeSMinus_Box.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.probeSMinus_Box.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.probeSMinus_Box.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.probeSMinus_Box.setObjectName(_fromUtf8("probeSMinus_Box"))
        self.trialRatio_grid.addWidget(self.probeSMinus_Box, 3, 2, 1, 1)
        self.trainSPlus_Box = QtGui.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trainSPlus_Box.sizePolicy().hasHeightForWidth())
        self.trainSPlus_Box.setSizePolicy(sizePolicy)
        self.trainSPlus_Box.setMaximumSize(QtCore.QSize(50, 30))
        self.trainSPlus_Box.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.trainSPlus_Box.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.trainSPlus_Box.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.trainSPlus_Box.setObjectName(_fromUtf8("trainSPlus_Box"))
        self.trialRatio_grid.addWidget(self.trainSPlus_Box, 2, 3, 1, 1)
        self.trainSMinus_Box = QtGui.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trainSMinus_Box.sizePolicy().hasHeightForWidth())
        self.trainSMinus_Box.setSizePolicy(sizePolicy)
        self.trainSMinus_Box.setMaximumSize(QtCore.QSize(50, 30))
        self.trainSMinus_Box.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.trainSMinus_Box.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.trainSMinus_Box.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.trainSMinus_Box.setObjectName(_fromUtf8("trainSMinus_Box"))
        self.trialRatio_grid.addWidget(self.trainSMinus_Box, 2, 2, 1, 1)
        self.probeSPlus_Box = QtGui.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probeSPlus_Box.sizePolicy().hasHeightForWidth())
        self.probeSPlus_Box.setSizePolicy(sizePolicy)
        self.probeSPlus_Box.setMaximumSize(QtCore.QSize(50, 30))
        self.probeSPlus_Box.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.probeSPlus_Box.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.probeSPlus_Box.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.probeSPlus_Box.setObjectName(_fromUtf8("probeSPlus_Box"))
        self.trialRatio_grid.addWidget(self.probeSPlus_Box, 3, 3, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.probeRatio_Label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probeRatio_Label.sizePolicy().hasHeightForWidth())
        self.probeRatio_Label.setSizePolicy(sizePolicy)
        self.probeRatio_Label.setMaximumSize(QtCore.QSize(70, 25))
        self.probeRatio_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.probeRatio_Label.setObjectName(_fromUtf8("probeRatio_Label"))
        self.trialRatio_grid.addWidget(self.probeRatio_Label, 3, 1, 1, 1)
        self.trainingRatio_Label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trainingRatio_Label.sizePolicy().hasHeightForWidth())
        self.trainingRatio_Label.setSizePolicy(sizePolicy)
        self.trainingRatio_Label.setMaximumSize(QtCore.QSize(70, 25))
        self.trainingRatio_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.trainingRatio_Label.setObjectName(_fromUtf8("trainingRatio_Label"))
        self.trialRatio_grid.addWidget(self.trainingRatio_Label, 2, 1, 1, 1)
        self.sPlusRatio_Label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sPlusRatio_Label.sizePolicy().hasHeightForWidth())
        self.sPlusRatio_Label.setSizePolicy(sizePolicy)
        self.sPlusRatio_Label.setMaximumSize(QtCore.QSize(70, 25))
        self.sPlusRatio_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.sPlusRatio_Label.setObjectName(_fromUtf8("sPlusRatio_Label"))
        self.trialRatio_grid.addWidget(self.sPlusRatio_Label, 1, 3, 1, 1)
        self.sMinusRatio_Label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sMinusRatio_Label.sizePolicy().hasHeightForWidth())
        self.sMinusRatio_Label.setSizePolicy(sizePolicy)
        self.sMinusRatio_Label.setMaximumSize(QtCore.QSize(70, 25))
        self.sMinusRatio_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.sMinusRatio_Label.setObjectName(_fromUtf8("sMinusRatio_Label"))
        self.trialRatio_grid.addWidget(self.sMinusRatio_Label, 1, 2, 1, 1)
        self.trialRatio_Label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trialRatio_Label.sizePolicy().hasHeightForWidth())
        self.trialRatio_Label.setSizePolicy(sizePolicy)
        self.trialRatio_Label.setMaximumSize(QtCore.QSize(90, 25))
        self.trialRatio_Label.setObjectName(_fromUtf8("trialRatio_Label"))
        self.trialRatio_grid.addWidget(self.trialRatio_Label, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.trialRatio_grid.addItem(spacerItem, 2, 4, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.trialRatio_grid.addItem(spacerItem1, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.trialRatio_grid, 1, 0, 1, 3)
        jsonStim.setCentralWidget(self.centralwidget)
        self.paramFile_Label.setBuddy(self.paramFile_Box)
        self.stimDir_Label.setBuddy(self.paramFile_Box)

        self.retranslateUi(jsonStim)
        QtCore.QMetaObject.connectSlotsByName(jsonStim)
        jsonStim.setTabOrder(self.stimTable, self.paramFile_Box)
        jsonStim.setTabOrder(self.paramFile_Box, self.paramFile_Button)
        jsonStim.setTabOrder(self.paramFile_Button, self.stimDir_Button)
        jsonStim.setTabOrder(self.stimDir_Button, self.cancelButton)
        jsonStim.setTabOrder(self.cancelButton, self.saveButton)

    def retranslateUi(self, jsonStim):
        jsonStim.setWindowTitle(_translate("jsonStim", "Stimuli Selection", None))
        self.paramFile_Label.setText(_translate("jsonStim", "Parameter File", None))
        self.paramFile_Button.setText(_translate("jsonStim", "...", None))
        self.cancelButton.setText(_translate("jsonStim", "Cancel", None))
        self.saveButton.setText(_translate("jsonStim", "Save", None))
        self.stimDir_Label.setText(_translate("jsonStim", "Stim Directory", None))
        self.stimDir_Button.setText(_translate("jsonStim", "...", None))
        self.stimTable.setSortingEnabled(True)
        item = self.stimTable.horizontalHeaderItem(0)
        item.setText(_translate("jsonStim", "Class", None))
        item = self.stimTable.horizontalHeaderItem(1)
        item.setText(_translate("jsonStim", "Stimulus", None))
        self.probeRatio_Label.setText(_translate("jsonStim", "Probe", None))
        self.trainingRatio_Label.setText(_translate("jsonStim", "Training", None))
        self.sPlusRatio_Label.setText(_translate("jsonStim", "S+", None))
        self.sMinusRatio_Label.setText(_translate("jsonStim", "S-", None))
        self.trialRatio_Label.setText(_translate("jsonStim", "Trial Ratios", None))
