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
        jsonStim.resize(772, 656)
        self.centralwidget = QtGui.QWidget(jsonStim)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.trialRatio_grid = QtGui.QGridLayout()
        self.trialRatio_grid.setHorizontalSpacing(6)
        self.trialRatio_grid.setObjectName(_fromUtf8("trialRatio_grid"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.trialRatio_grid.addWidget(self.label, 1, 1, 1, 1)
        self.trainSMinus_Box = QtGui.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trainSMinus_Box.sizePolicy().hasHeightForWidth())
        self.trainSMinus_Box.setSizePolicy(sizePolicy)
        self.trainSMinus_Box.setMinimumSize(QtCore.QSize(0, 25))
        self.trainSMinus_Box.setMaximumSize(QtCore.QSize(50, 30))
        self.trainSMinus_Box.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.trainSMinus_Box.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.trainSMinus_Box.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.trainSMinus_Box.setObjectName(_fromUtf8("trainSMinus_Box"))
        self.trialRatio_grid.addWidget(self.trainSMinus_Box, 3, 8, 1, 1)
        self.probeSPlus_Box = QtGui.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probeSPlus_Box.sizePolicy().hasHeightForWidth())
        self.probeSPlus_Box.setSizePolicy(sizePolicy)
        self.probeSPlus_Box.setMinimumSize(QtCore.QSize(0, 25))
        self.probeSPlus_Box.setMaximumSize(QtCore.QSize(50, 30))
        self.probeSPlus_Box.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.probeSPlus_Box.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.probeSPlus_Box.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.probeSPlus_Box.setObjectName(_fromUtf8("probeSPlus_Box"))
        self.trialRatio_grid.addWidget(self.probeSPlus_Box, 4, 9, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.trialRatio_grid.addItem(spacerItem, 4, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(50, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.trialRatio_grid.addItem(spacerItem1, 4, 10, 1, 1)
        self.probeTempoRange_Label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probeTempoRange_Label.sizePolicy().hasHeightForWidth())
        self.probeTempoRange_Label.setSizePolicy(sizePolicy)
        self.probeTempoRange_Label.setMaximumSize(QtCore.QSize(120, 100))
        self.probeTempoRange_Label.setWordWrap(True)
        self.probeTempoRange_Label.setObjectName(_fromUtf8("probeTempoRange_Label"))
        self.trialRatio_grid.addWidget(self.probeTempoRange_Label, 4, 1, 1, 1)
        self.trialRatio_Label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trialRatio_Label.sizePolicy().hasHeightForWidth())
        self.trialRatio_Label.setSizePolicy(sizePolicy)
        self.trialRatio_Label.setMaximumSize(QtCore.QSize(100, 200))
        self.trialRatio_Label.setWordWrap(True)
        self.trialRatio_Label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.trialRatio_Label.setObjectName(_fromUtf8("trialRatio_Label"))
        self.trialRatio_grid.addWidget(self.trialRatio_Label, 3, 5, 2, 1)
        self.probeSMinus_Box = QtGui.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probeSMinus_Box.sizePolicy().hasHeightForWidth())
        self.probeSMinus_Box.setSizePolicy(sizePolicy)
        self.probeSMinus_Box.setMinimumSize(QtCore.QSize(0, 25))
        self.probeSMinus_Box.setMaximumSize(QtCore.QSize(50, 30))
        self.probeSMinus_Box.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.probeSMinus_Box.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.probeSMinus_Box.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.probeSMinus_Box.setObjectName(_fromUtf8("probeSMinus_Box"))
        self.trialRatio_grid.addWidget(self.probeSMinus_Box, 4, 8, 1, 1)
        self.trainingRatio_Label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trainingRatio_Label.sizePolicy().hasHeightForWidth())
        self.trainingRatio_Label.setSizePolicy(sizePolicy)
        self.trainingRatio_Label.setMaximumSize(QtCore.QSize(70, 25))
        self.trainingRatio_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.trainingRatio_Label.setObjectName(_fromUtf8("trainingRatio_Label"))
        self.trialRatio_grid.addWidget(self.trainingRatio_Label, 3, 6, 1, 1)
        self.sPlusSelector_Label = QtGui.QLabel(self.centralwidget)
        self.sPlusSelector_Label.setObjectName(_fromUtf8("sPlusSelector_Label"))
        self.trialRatio_grid.addWidget(self.sPlusSelector_Label, 3, 1, 1, 1)
        self.trialTypeApply_Button = QtGui.QPushButton(self.centralwidget)
        self.trialTypeApply_Button.setObjectName(_fromUtf8("trialTypeApply_Button"))
        self.trialRatio_grid.addWidget(self.trialTypeApply_Button, 5, 1, 1, 3)
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.trialRatio_grid.addWidget(self.line_3, 0, 4, 6, 1)
        self.probeTempoRange_Box = QtGui.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probeTempoRange_Box.sizePolicy().hasHeightForWidth())
        self.probeTempoRange_Box.setSizePolicy(sizePolicy)
        self.probeTempoRange_Box.setMinimumSize(QtCore.QSize(100, 30))
        self.probeTempoRange_Box.setMaximumSize(QtCore.QSize(500, 30))
        self.probeTempoRange_Box.setObjectName(_fromUtf8("probeTempoRange_Box"))
        self.trialRatio_grid.addWidget(self.probeTempoRange_Box, 4, 2, 1, 2)
        self.trainSPlus_Box = QtGui.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trainSPlus_Box.sizePolicy().hasHeightForWidth())
        self.trainSPlus_Box.setSizePolicy(sizePolicy)
        self.trainSPlus_Box.setMinimumSize(QtCore.QSize(0, 25))
        self.trainSPlus_Box.setMaximumSize(QtCore.QSize(50, 30))
        self.trainSPlus_Box.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.trainSPlus_Box.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.trainSPlus_Box.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.trainSPlus_Box.setObjectName(_fromUtf8("trainSPlus_Box"))
        self.trialRatio_grid.addWidget(self.trainSPlus_Box, 3, 9, 1, 1)
        self.sPlusSelector_Box = QtGui.QComboBox(self.centralwidget)
        self.sPlusSelector_Box.setMinimumSize(QtCore.QSize(90, 0))
        self.sPlusSelector_Box.setMaximumSize(QtCore.QSize(150, 30))
        self.sPlusSelector_Box.setObjectName(_fromUtf8("sPlusSelector_Box"))
        self.sPlusSelector_Box.addItem(_fromUtf8(""))
        self.sPlusSelector_Box.addItem(_fromUtf8(""))
        self.trialRatio_grid.addWidget(self.sPlusSelector_Box, 3, 2, 1, 1)
        self.probeRatio_Label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probeRatio_Label.sizePolicy().hasHeightForWidth())
        self.probeRatio_Label.setSizePolicy(sizePolicy)
        self.probeRatio_Label.setMaximumSize(QtCore.QSize(70, 25))
        self.probeRatio_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.probeRatio_Label.setObjectName(_fromUtf8("probeRatio_Label"))
        self.trialRatio_grid.addWidget(self.probeRatio_Label, 4, 6, 1, 1)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.trialRatio_grid.addWidget(self.line, 3, 7, 3, 1)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setMinimumSize(QtCore.QSize(0, 1))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.trialRatio_grid.addWidget(self.line_2, 2, 6, 1, 4)
        self.line_5 = QtGui.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.trialRatio_grid.addWidget(self.line_5, 2, 0, 1, 4)
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.trialRatio_grid.addWidget(self.comboBox, 1, 2, 1, 2)
        self.refresh_Button = QtGui.QPushButton(self.centralwidget)
        self.refresh_Button.setObjectName(_fromUtf8("refresh_Button"))
        self.trialRatio_grid.addWidget(self.refresh_Button, 0, 3, 1, 1)
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.trialRatio_grid.addWidget(self.line_4, 1, 7, 1, 1)
        self.sMinusRatio_Label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sMinusRatio_Label.sizePolicy().hasHeightForWidth())
        self.sMinusRatio_Label.setSizePolicy(sizePolicy)
        self.sMinusRatio_Label.setMaximumSize(QtCore.QSize(70, 25))
        self.sMinusRatio_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.sMinusRatio_Label.setObjectName(_fromUtf8("sMinusRatio_Label"))
        self.trialRatio_grid.addWidget(self.sMinusRatio_Label, 1, 8, 1, 1)
        self.sPlusRatio_Label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sPlusRatio_Label.sizePolicy().hasHeightForWidth())
        self.sPlusRatio_Label.setSizePolicy(sizePolicy)
        self.sPlusRatio_Label.setMaximumSize(QtCore.QSize(70, 25))
        self.sPlusRatio_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.sPlusRatio_Label.setObjectName(_fromUtf8("sPlusRatio_Label"))
        self.trialRatio_grid.addWidget(self.sPlusRatio_Label, 1, 9, 1, 1)
        self.gridLayout_3.addLayout(self.trialRatio_grid, 5, 0, 1, 2)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.stimDir_Button = QtGui.QToolButton(self.centralwidget)
        self.stimDir_Button.setMinimumSize(QtCore.QSize(30, 30))
        self.stimDir_Button.setObjectName(_fromUtf8("stimDir_Button"))
        self.gridLayout.addWidget(self.stimDir_Button, 0, 2, 1, 1)
        self.paramFile_Label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.paramFile_Label.sizePolicy().hasHeightForWidth())
        self.paramFile_Label.setSizePolicy(sizePolicy)
        self.paramFile_Label.setMinimumSize(QtCore.QSize(101, 0))
        self.paramFile_Label.setMaximumSize(QtCore.QSize(104, 30))
        self.paramFile_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.paramFile_Label.setObjectName(_fromUtf8("paramFile_Label"))
        self.gridLayout.addWidget(self.paramFile_Label, 1, 0, 1, 1)
        self.stimDir_Box = QtGui.QTextEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stimDir_Box.sizePolicy().hasHeightForWidth())
        self.stimDir_Box.setSizePolicy(sizePolicy)
        self.stimDir_Box.setMinimumSize(QtCore.QSize(400, 60))
        self.stimDir_Box.setMaximumSize(QtCore.QSize(410, 60))
        self.stimDir_Box.setObjectName(_fromUtf8("stimDir_Box"))
        self.gridLayout.addWidget(self.stimDir_Box, 0, 1, 1, 1)
        self.stimDir_Label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stimDir_Label.sizePolicy().hasHeightForWidth())
        self.stimDir_Label.setSizePolicy(sizePolicy)
        self.stimDir_Label.setMinimumSize(QtCore.QSize(101, 0))
        self.stimDir_Label.setMaximumSize(QtCore.QSize(104, 30))
        self.stimDir_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.stimDir_Label.setObjectName(_fromUtf8("stimDir_Label"))
        self.gridLayout.addWidget(self.stimDir_Label, 0, 0, 1, 1)
        self.paramFile_Box = QtGui.QTextEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.paramFile_Box.sizePolicy().hasHeightForWidth())
        self.paramFile_Box.setSizePolicy(sizePolicy)
        self.paramFile_Box.setMinimumSize(QtCore.QSize(400, 60))
        self.paramFile_Box.setMaximumSize(QtCore.QSize(410, 60))
        self.paramFile_Box.setObjectName(_fromUtf8("paramFile_Box"))
        self.gridLayout.addWidget(self.paramFile_Box, 1, 1, 1, 1)
        self.paramFile_Button = QtGui.QToolButton(self.centralwidget)
        self.paramFile_Button.setMinimumSize(QtCore.QSize(30, 30))
        self.paramFile_Button.setMaximumSize(QtCore.QSize(30, 30))
        self.paramFile_Button.setObjectName(_fromUtf8("paramFile_Button"))
        self.gridLayout.addWidget(self.paramFile_Button, 1, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 6, 0, 1, 2)
        self.controlHorizLayout = QtGui.QHBoxLayout()
        self.controlHorizLayout.setObjectName(_fromUtf8("controlHorizLayout"))
        self.cancelButton = QtGui.QPushButton(self.centralwidget)
        self.cancelButton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.controlHorizLayout.addWidget(self.cancelButton)
        self.saveButton = QtGui.QPushButton(self.centralwidget)
        self.saveButton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.controlHorizLayout.addWidget(self.saveButton)
        self.saveAs_Button = QtGui.QPushButton(self.centralwidget)
        self.saveAs_Button.setMaximumSize(QtCore.QSize(16777215, 30))
        self.saveAs_Button.setObjectName(_fromUtf8("saveAs_Button"))
        self.controlHorizLayout.addWidget(self.saveAs_Button)
        self.gridLayout_3.addLayout(self.controlHorizLayout, 7, 0, 1, 2)
        self.treeWidget = QtGui.QTreeWidget(self.centralwidget)
        self.treeWidget.setTabKeyNavigation(True)
        self.treeWidget.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.treeWidget.setAllColumnsShowFocus(True)
        self.treeWidget.setHeaderHidden(False)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.treeWidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.treeWidget.header().setCascadingSectionResizes(True)
        self.treeWidget.header().setSortIndicatorShown(True)
        self.treeWidget.header().setStretchLastSection(True)
        self.gridLayout_3.addWidget(self.treeWidget, 0, 0, 1, 2)
        self.treeWidget.raise_()
        jsonStim.setCentralWidget(self.centralwidget)
        self.trainingRatio_Label.setBuddy(self.trainSMinus_Box)
        self.sPlusSelector_Label.setBuddy(self.sPlusSelector_Box)
        self.probeRatio_Label.setBuddy(self.probeSMinus_Box)
        self.paramFile_Label.setBuddy(self.paramFile_Box)
        self.stimDir_Label.setBuddy(self.stimDir_Box)

        self.retranslateUi(jsonStim)
        QtCore.QMetaObject.connectSlotsByName(jsonStim)
        jsonStim.setTabOrder(self.stimDir_Button, self.cancelButton)
        jsonStim.setTabOrder(self.cancelButton, self.saveButton)

    def retranslateUi(self, jsonStim):
        jsonStim.setWindowTitle(_translate("jsonStim", "Stimuli Selection", None))
        self.label.setText(_translate("jsonStim", "Group by:", None))
        self.probeTempoRange_Label.setText(_translate("jsonStim", "Probe Tempo Range", None))
        self.trialRatio_Label.setText(_translate("jsonStim", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Trial Ratios</span></p></body></html>", None))
        self.trainingRatio_Label.setText(_translate("jsonStim", "Training", None))
        self.sPlusSelector_Label.setText(_translate("jsonStim", "S+", None))
        self.trialTypeApply_Button.setText(_translate("jsonStim", "Apply Changes", None))
        self.probeTempoRange_Box.setToolTip(_translate("jsonStim", "<html><head/><body><p>Comma-separated ranges (e.g., 120-130, 90-100)</p></body></html>", None))
        self.sPlusSelector_Box.setItemText(0, _translate("jsonStim", "Regular", None))
        self.sPlusSelector_Box.setItemText(1, _translate("jsonStim", "Irregular", None))
        self.probeRatio_Label.setText(_translate("jsonStim", "Probe", None))
        self.comboBox.setItemText(0, _translate("jsonStim", "Base Tempo", None))
        self.comboBox.setItemText(1, _translate("jsonStim", "Trial Type", None))
        self.comboBox.setItemText(2, _translate("jsonStim", "Bird", None))
        self.refresh_Button.setText(_translate("jsonStim", "Refresh", None))
        self.sMinusRatio_Label.setText(_translate("jsonStim", "S-", None))
        self.sPlusRatio_Label.setText(_translate("jsonStim", "S+", None))
        self.stimDir_Button.setText(_translate("jsonStim", "...", None))
        self.paramFile_Label.setText(_translate("jsonStim", "Parameter File", None))
        self.stimDir_Label.setText(_translate("jsonStim", "Stim Directory", None))
        self.paramFile_Button.setText(_translate("jsonStim", "...", None))
        self.cancelButton.setText(_translate("jsonStim", "Cancel", None))
        self.saveButton.setText(_translate("jsonStim", "Save", None))
        self.saveAs_Button.setText(_translate("jsonStim", "Save As", None))
        self.treeWidget.setSortingEnabled(True)
        self.treeWidget.headerItem().setText(0, _translate("jsonStim", "Bird", None))
        self.treeWidget.headerItem().setText(1, _translate("jsonStim", "Sound Type", None))
        self.treeWidget.headerItem().setText(2, _translate("jsonStim", "Base Tempo", None))
        self.treeWidget.headerItem().setText(3, _translate("jsonStim", "Tempo", None))
        self.treeWidget.headerItem().setText(4, _translate("jsonStim", "Pattern", None))
        self.treeWidget.headerItem().setText(5, _translate("jsonStim", "Trial Type", None))
        self.treeWidget.headerItem().setText(6, _translate("jsonStim", "Stimulus", None))
