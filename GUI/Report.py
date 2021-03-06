# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI\Report.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Report(object):
    def setupUi(self, Report):
        Report.setObjectName("Report")
        Report.resize(1093, 757)
        self.gridLayout_2 = QtWidgets.QGridLayout(Report)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(Report)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.buttonLoadTrainingData = QtWidgets.QPushButton(Report)
        self.buttonLoadTrainingData.setObjectName("buttonLoadTrainingData")
        self.horizontalLayout_2.addWidget(self.buttonLoadTrainingData)
        self.buttonClearTrainingData = QtWidgets.QPushButton(Report)
        self.buttonClearTrainingData.setObjectName("buttonClearTrainingData")
        self.horizontalLayout_2.addWidget(self.buttonClearTrainingData)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.lineEditTrainingData = QtWidgets.QLineEdit(Report)
        self.lineEditTrainingData.setReadOnly(True)
        self.lineEditTrainingData.setObjectName("lineEditTrainingData")
        self.verticalLayout_3.addWidget(self.lineEditTrainingData)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(Report)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.buttonLoadTestingData = QtWidgets.QPushButton(Report)
        self.buttonLoadTestingData.setObjectName("buttonLoadTestingData")
        self.horizontalLayout_3.addWidget(self.buttonLoadTestingData)
        self.buttonClearTestingData = QtWidgets.QPushButton(Report)
        self.buttonClearTestingData.setObjectName("buttonClearTestingData")
        self.horizontalLayout_3.addWidget(self.buttonClearTestingData)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.lineEditTestingData = QtWidgets.QLineEdit(Report)
        self.lineEditTestingData.setReadOnly(True)
        self.lineEditTestingData.setObjectName("lineEditTestingData")
        self.verticalLayout_4.addWidget(self.lineEditTestingData)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_3 = QtWidgets.QLabel(Report)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.textEditDataDescription = QtWidgets.QTextEdit(Report)
        self.textEditDataDescription.setObjectName("textEditDataDescription")
        self.verticalLayout_6.addWidget(self.textEditDataDescription)
        self.verticalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_8.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(Report)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonLoadResult = QtWidgets.QPushButton(Report)
        self.buttonLoadResult.setObjectName("buttonLoadResult")
        self.horizontalLayout.addWidget(self.buttonLoadResult)
        self.buttonClearResult = QtWidgets.QPushButton(Report)
        self.buttonClearResult.setObjectName("buttonClearResult")
        self.horizontalLayout.addWidget(self.buttonClearResult)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.lineEditResultPath = QtWidgets.QLineEdit(Report)
        self.lineEditResultPath.setReadOnly(True)
        self.lineEditResultPath.setObjectName("lineEditResultPath")
        self.verticalLayout_2.addWidget(self.lineEditResultPath)
        self.textEditDescription = QtWidgets.QTextEdit(Report)
        self.textEditDescription.setObjectName("textEditDescription")
        self.verticalLayout_2.addWidget(self.textEditDescription)
        self.verticalLayout_8.addLayout(self.verticalLayout_2)
        self.buttonGenerate = QtWidgets.QPushButton(Report)
        self.buttonGenerate.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.buttonGenerate.setFont(font)
        self.buttonGenerate.setObjectName("buttonGenerate")
        self.verticalLayout_8.addWidget(self.buttonGenerate)
        self.horizontalLayout_5.addLayout(self.verticalLayout_8)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.canvasROC = MatplotlibWidget(Report)
        self.canvasROC.setMinimumSize(QtCore.QSize(400, 400))
        self.canvasROC.setObjectName("canvasROC")
        self.verticalLayout_7.addWidget(self.canvasROC)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.checkROCTrain = QtWidgets.QCheckBox(Report)
        self.checkROCTrain.setObjectName("checkROCTrain")
        self.horizontalLayout_4.addWidget(self.checkROCTrain)
        self.checkROCValidation = QtWidgets.QCheckBox(Report)
        self.checkROCValidation.setObjectName("checkROCValidation")
        self.horizontalLayout_4.addWidget(self.checkROCValidation)
        self.checkROCTest = QtWidgets.QCheckBox(Report)
        self.checkROCTest.setObjectName("checkROCTest")
        self.horizontalLayout_4.addWidget(self.checkROCTest)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(Report)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)
        self.comboFeatureSelector = QtWidgets.QComboBox(Report)
        self.comboFeatureSelector.setObjectName("comboFeatureSelector")
        self.gridLayout.addWidget(self.comboFeatureSelector, 2, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(Report)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 4, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(Report)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)
        self.comboDimensionReduction = QtWidgets.QComboBox(Report)
        self.comboDimensionReduction.setObjectName("comboDimensionReduction")
        self.gridLayout.addWidget(self.comboDimensionReduction, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(Report)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.comboNormalizer = QtWidgets.QComboBox(Report)
        self.comboNormalizer.setObjectName("comboNormalizer")
        self.gridLayout.addWidget(self.comboNormalizer, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(Report)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.comboClassifier = QtWidgets.QComboBox(Report)
        self.comboClassifier.setObjectName("comboClassifier")
        self.gridLayout.addWidget(self.comboClassifier, 3, 1, 1, 1)
        self.spinBoxFeatureNumber = QtWidgets.QSpinBox(Report)
        self.spinBoxFeatureNumber.setObjectName("spinBoxFeatureNumber")
        self.gridLayout.addWidget(self.spinBoxFeatureNumber, 4, 1, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout)
        self.verticalLayout_7.setStretch(0, 15)
        self.verticalLayout_7.setStretch(1, 1)
        self.verticalLayout_7.setStretch(2, 5)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 2)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)

        self.retranslateUi(Report)
        QtCore.QMetaObject.connectSlotsByName(Report)

    def retranslateUi(self, Report):
        _translate = QtCore.QCoreApplication.translate
        Report.setWindowTitle(_translate("Report", "Report"))
        self.label.setText(_translate("Report", "Training data"))
        self.buttonLoadTrainingData.setText(_translate("Report", "Load"))
        self.buttonClearTrainingData.setText(_translate("Report", "Clear"))
        self.label_2.setText(_translate("Report", "Testing data"))
        self.buttonLoadTestingData.setText(_translate("Report", "Load"))
        self.buttonClearTestingData.setText(_translate("Report", "Clear"))
        self.label_3.setText(_translate("Report", "Data Description"))
        self.label_4.setText(_translate("Report", "Pipeline Result"))
        self.buttonLoadResult.setText(_translate("Report", "Load"))
        self.buttonClearResult.setText(_translate("Report", "Clear"))
        self.buttonGenerate.setText(_translate("Report", "Generate Report"))
        self.checkROCTrain.setText(_translate("Report", "Train"))
        self.checkROCValidation.setText(_translate("Report", "Validation"))
        self.checkROCTest.setText(_translate("Report", "Test"))
        self.label_8.setText(_translate("Report", "Feature Selector"))
        self.label_10.setText(_translate("Report", "Feature Number"))
        self.label_9.setText(_translate("Report", "Classifier"))
        self.label_7.setText(_translate("Report", "Dimension Reducer"))
        self.label_6.setText(_translate("Report", "Normalizer"))

from MatplotlibWidget import MatplotlibWidget
