# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dls_pmaccontrol/formAxisSettings.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_formAxisSettings(object):
    def setupUi(self, formAxisSettings):
        formAxisSettings.setObjectName("formAxisSettings")
        formAxisSettings.resize(508, 451)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(formAxisSettings.sizePolicy().hasHeightForWidth())
        formAxisSettings.setSizePolicy(sizePolicy)
        formAxisSettings.setMaximumSize(QtCore.QSize(1024, 768))
        self.gridLayout_3 = QtWidgets.QGridLayout(formAxisSettings)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.textLabel1 = QtWidgets.QLabel(formAxisSettings)
        self.textLabel1.setWordWrap(False)
        self.textLabel1.setObjectName("textLabel1")
        self.gridLayout_3.addWidget(self.textLabel1, 0, 0, 1, 3)
        self.tabAxisSetup = QtWidgets.QTabWidget(formAxisSettings)
        self.tabAxisSetup.setObjectName("tabAxisSetup")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox1 = QtWidgets.QGroupBox(self.tab)
        self.groupBox1.setObjectName("groupBox1")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox1)
        self.formLayout_2.setContentsMargins(11, 11, 11, 11)
        self.formLayout_2.setSpacing(6)
        self.formLayout_2.setObjectName("formLayout_2")
        self.textLabel2 = QtWidgets.QLabel(self.groupBox1)
        self.textLabel2.setWordWrap(False)
        self.textLabel2.setObjectName("textLabel2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.textLabel2)
        self.lneIx11 = QtWidgets.QLineEdit(self.groupBox1)
        self.lneIx11.setMinimumSize(QtCore.QSize(60, 0))
        self.lneIx11.setMaximumSize(QtCore.QSize(31222, 32767))
        self.lneIx11.setObjectName("lneIx11")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lneIx11)
        self.textLabel2_2 = QtWidgets.QLabel(self.groupBox1)
        self.textLabel2_2.setWordWrap(False)
        self.textLabel2_2.setObjectName("textLabel2_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.textLabel2_2)
        self.lneIx12 = QtWidgets.QLineEdit(self.groupBox1)
        self.lneIx12.setMinimumSize(QtCore.QSize(60, 0))
        self.lneIx12.setMaximumSize(QtCore.QSize(31222, 32767))
        self.lneIx12.setObjectName("lneIx12")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lneIx12)
        self.textLabel2_3 = QtWidgets.QLabel(self.groupBox1)
        self.textLabel2_3.setWordWrap(False)
        self.textLabel2_3.setObjectName("textLabel2_3")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.textLabel2_3)
        self.lneIx13 = QtWidgets.QLineEdit(self.groupBox1)
        self.lneIx13.setMinimumSize(QtCore.QSize(60, 0))
        self.lneIx13.setMaximumSize(QtCore.QSize(31222, 32767))
        self.lneIx13.setObjectName("lneIx13")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lneIx13)
        self.textLabel2_4 = QtWidgets.QLabel(self.groupBox1)
        self.textLabel2_4.setWordWrap(False)
        self.textLabel2_4.setObjectName("textLabel2_4")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.textLabel2_4)
        self.lneIx14 = QtWidgets.QLineEdit(self.groupBox1)
        self.lneIx14.setMinimumSize(QtCore.QSize(60, 0))
        self.lneIx14.setMaximumSize(QtCore.QSize(31222, 32767))
        self.lneIx14.setObjectName("lneIx14")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lneIx14)
        self.textLabel2_5 = QtWidgets.QLabel(self.groupBox1)
        self.textLabel2_5.setWordWrap(False)
        self.textLabel2_5.setObjectName("textLabel2_5")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.textLabel2_5)
        self.lneIx15 = QtWidgets.QLineEdit(self.groupBox1)
        self.lneIx15.setMinimumSize(QtCore.QSize(60, 0))
        self.lneIx15.setMaximumSize(QtCore.QSize(31222, 32767))
        self.lneIx15.setObjectName("lneIx15")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lneIx15)
        self.textLabel2_6 = QtWidgets.QLabel(self.groupBox1)
        self.textLabel2_6.setWordWrap(False)
        self.textLabel2_6.setObjectName("textLabel2_6")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.textLabel2_6)
        self.lneIx16 = QtWidgets.QLineEdit(self.groupBox1)
        self.lneIx16.setMinimumSize(QtCore.QSize(60, 0))
        self.lneIx16.setMaximumSize(QtCore.QSize(31222, 32767))
        self.lneIx16.setObjectName("lneIx16")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lneIx16)
        self.textLabel2_7 = QtWidgets.QLabel(self.groupBox1)
        self.textLabel2_7.setWordWrap(False)
        self.textLabel2_7.setObjectName("textLabel2_7")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.textLabel2_7)
        self.lneIx17 = QtWidgets.QLineEdit(self.groupBox1)
        self.lneIx17.setMinimumSize(QtCore.QSize(60, 0))
        self.lneIx17.setMaximumSize(QtCore.QSize(31222, 32767))
        self.lneIx17.setObjectName("lneIx17")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lneIx17)
        self.textLabel2_8 = QtWidgets.QLabel(self.groupBox1)
        self.textLabel2_8.setWordWrap(False)
        self.textLabel2_8.setObjectName("textLabel2_8")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.textLabel2_8)
        self.lneIx19 = QtWidgets.QLineEdit(self.groupBox1)
        self.lneIx19.setMinimumSize(QtCore.QSize(60, 0))
        self.lneIx19.setMaximumSize(QtCore.QSize(31222, 32767))
        self.lneIx19.setObjectName("lneIx19")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lneIx19)
        self.gridLayout_2.addWidget(self.groupBox1, 0, 0, 1, 1)
        self.groupBox2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox2.setObjectName("groupBox2")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox2)
        self.formLayout.setContentsMargins(11, 11, 11, 11)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.textLabel2_9 = QtWidgets.QLabel(self.groupBox2)
        self.textLabel2_9.setWordWrap(False)
        self.textLabel2_9.setObjectName("textLabel2_9")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.textLabel2_9)
        self.lneIx20 = QtWidgets.QLineEdit(self.groupBox2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lneIx20.sizePolicy().hasHeightForWidth())
        self.lneIx20.setSizePolicy(sizePolicy)
        self.lneIx20.setMinimumSize(QtCore.QSize(60, 0))
        self.lneIx20.setMaximumSize(QtCore.QSize(32222, 32767))
        self.lneIx20.setObjectName("lneIx20")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lneIx20)
        self.textLabel2_2_2 = QtWidgets.QLabel(self.groupBox2)
        self.textLabel2_2_2.setWordWrap(False)
        self.textLabel2_2_2.setObjectName("textLabel2_2_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.textLabel2_2_2)
        self.lneIx21 = QtWidgets.QLineEdit(self.groupBox2)
        self.lneIx21.setMinimumSize(QtCore.QSize(60, 0))
        self.lneIx21.setMaximumSize(QtCore.QSize(32222, 32767))
        self.lneIx21.setObjectName("lneIx21")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lneIx21)
        self.textLabel2_3_2 = QtWidgets.QLabel(self.groupBox2)
        self.textLabel2_3_2.setWordWrap(False)
        self.textLabel2_3_2.setObjectName("textLabel2_3_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.textLabel2_3_2)
        self.lneIx22 = QtWidgets.QLineEdit(self.groupBox2)
        self.lneIx22.setMinimumSize(QtCore.QSize(60, 0))
        self.lneIx22.setMaximumSize(QtCore.QSize(32222, 32767))
        self.lneIx22.setObjectName("lneIx22")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lneIx22)
        self.textLabel2_4_2 = QtWidgets.QLabel(self.groupBox2)
        self.textLabel2_4_2.setWordWrap(False)
        self.textLabel2_4_2.setObjectName("textLabel2_4_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.textLabel2_4_2)
        self.lneIx23 = QtWidgets.QLineEdit(self.groupBox2)
        self.lneIx23.setMinimumSize(QtCore.QSize(60, 0))
        self.lneIx23.setMaximumSize(QtCore.QSize(32222, 32767))
        self.lneIx23.setObjectName("lneIx23")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lneIx23)
        self.textLabel2_5_2 = QtWidgets.QLabel(self.groupBox2)
        self.textLabel2_5_2.setWordWrap(False)
        self.textLabel2_5_2.setObjectName("textLabel2_5_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.textLabel2_5_2)
        self.lneIx24 = QtWidgets.QLineEdit(self.groupBox2)
        self.lneIx24.setMinimumSize(QtCore.QSize(60, 0))
        self.lneIx24.setMaximumSize(QtCore.QSize(32222, 32767))
        self.lneIx24.setObjectName("lneIx24")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lneIx24)
        self.textLabel2_6_2 = QtWidgets.QLabel(self.groupBox2)
        self.textLabel2_6_2.setWordWrap(False)
        self.textLabel2_6_2.setObjectName("textLabel2_6_2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.textLabel2_6_2)
        self.lneIx25 = QtWidgets.QLineEdit(self.groupBox2)
        self.lneIx25.setMinimumSize(QtCore.QSize(60, 0))
        self.lneIx25.setMaximumSize(QtCore.QSize(32222, 32767))
        self.lneIx25.setObjectName("lneIx25")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lneIx25)
        self.textLabel2_7_2 = QtWidgets.QLabel(self.groupBox2)
        self.textLabel2_7_2.setWordWrap(False)
        self.textLabel2_7_2.setObjectName("textLabel2_7_2")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.textLabel2_7_2)
        self.lneIx26 = QtWidgets.QLineEdit(self.groupBox2)
        self.lneIx26.setMinimumSize(QtCore.QSize(0, 0))
        self.lneIx26.setMaximumSize(QtCore.QSize(32222, 32767))
        self.lneIx26.setObjectName("lneIx26")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lneIx26)
        self.gridLayout_2.addWidget(self.groupBox2, 0, 1, 1, 1)
        self.tabAxisSetup.addTab(self.tab, "")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.gridLayout = QtWidgets.QGridLayout(self.tab1)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox1_2 = QtWidgets.QGroupBox(self.tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox1_2.sizePolicy().hasHeightForWidth())
        self.groupBox1_2.setSizePolicy(sizePolicy)
        self.groupBox1_2.setObjectName("groupBox1_2")
        self.formLayout_3 = QtWidgets.QFormLayout(self.groupBox1_2)
        self.formLayout_3.setContentsMargins(11, 11, 11, 11)
        self.formLayout_3.setSpacing(6)
        self.formLayout_3.setObjectName("formLayout_3")
        self.textLabel2_10 = QtWidgets.QLabel(self.groupBox1_2)
        self.textLabel2_10.setWordWrap(False)
        self.textLabel2_10.setObjectName("textLabel2_10")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.textLabel2_10)
        self.lneIx30 = QtWidgets.QLineEdit(self.groupBox1_2)
        self.lneIx30.setMinimumSize(QtCore.QSize(60, 0))
        self.lneIx30.setMaximumSize(QtCore.QSize(32233, 32767))
        self.lneIx30.setObjectName("lneIx30")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lneIx30)
        self.textLabel2_2_3 = QtWidgets.QLabel(self.groupBox1_2)
        self.textLabel2_2_3.setWordWrap(False)
        self.textLabel2_2_3.setObjectName("textLabel2_2_3")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.textLabel2_2_3)
        self.lneIx31 = QtWidgets.QLineEdit(self.groupBox1_2)
        self.lneIx31.setMinimumSize(QtCore.QSize(60, 0))
        self.lneIx31.setMaximumSize(QtCore.QSize(32233, 32767))
        self.lneIx31.setObjectName("lneIx31")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lneIx31)
        self.textLabel2_3_3 = QtWidgets.QLabel(self.groupBox1_2)
        self.textLabel2_3_3.setWordWrap(False)
        self.textLabel2_3_3.setObjectName("textLabel2_3_3")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.textLabel2_3_3)
        self.lneIx32 = QtWidgets.QLineEdit(self.groupBox1_2)
        self.lneIx32.setMinimumSize(QtCore.QSize(60, 0))
        self.lneIx32.setMaximumSize(QtCore.QSize(32233, 32767))
        self.lneIx32.setObjectName("lneIx32")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lneIx32)
        self.textLabel2_4_3 = QtWidgets.QLabel(self.groupBox1_2)
        self.textLabel2_4_3.setWordWrap(False)
        self.textLabel2_4_3.setObjectName("textLabel2_4_3")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.textLabel2_4_3)
        self.lneIx33 = QtWidgets.QLineEdit(self.groupBox1_2)
        self.lneIx33.setMinimumSize(QtCore.QSize(60, 0))
        self.lneIx33.setMaximumSize(QtCore.QSize(32233, 32767))
        self.lneIx33.setObjectName("lneIx33")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lneIx33)
        self.textLabel2_5_3 = QtWidgets.QLabel(self.groupBox1_2)
        self.textLabel2_5_3.setWordWrap(False)
        self.textLabel2_5_3.setObjectName("textLabel2_5_3")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.textLabel2_5_3)
        self.lneIx34 = QtWidgets.QLineEdit(self.groupBox1_2)
        self.lneIx34.setMinimumSize(QtCore.QSize(60, 0))
        self.lneIx34.setMaximumSize(QtCore.QSize(32233, 32767))
        self.lneIx34.setObjectName("lneIx34")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lneIx34)
        self.textLabel2_10_2 = QtWidgets.QLabel(self.groupBox1_2)
        self.textLabel2_10_2.setWordWrap(False)
        self.textLabel2_10_2.setObjectName("textLabel2_10_2")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.textLabel2_10_2)
        self.lneIx35 = QtWidgets.QLineEdit(self.groupBox1_2)
        self.lneIx35.setMinimumSize(QtCore.QSize(60, 0))
        self.lneIx35.setMaximumSize(QtCore.QSize(32233, 32767))
        self.lneIx35.setObjectName("lneIx35")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lneIx35)
        self.textLabel2_10_2_2 = QtWidgets.QLabel(self.groupBox1_2)
        self.textLabel2_10_2_2.setWordWrap(False)
        self.textLabel2_10_2_2.setObjectName("textLabel2_10_2_2")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.textLabel2_10_2_2)
        self.lneIx65 = QtWidgets.QLineEdit(self.groupBox1_2)
        self.lneIx65.setMinimumSize(QtCore.QSize(60, 0))
        self.lneIx65.setMaximumSize(QtCore.QSize(32233, 32767))
        self.lneIx65.setObjectName("lneIx65")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lneIx65)
        self.gridLayout.addWidget(self.groupBox1_2, 0, 0, 2, 1)
        self.groupBox1_2_2 = QtWidgets.QGroupBox(self.tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox1_2_2.sizePolicy().hasHeightForWidth())
        self.groupBox1_2_2.setSizePolicy(sizePolicy)
        self.groupBox1_2_2.setObjectName("groupBox1_2_2")
        self.formLayout_4 = QtWidgets.QFormLayout(self.groupBox1_2_2)
        self.formLayout_4.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_4.setContentsMargins(11, 11, 11, 11)
        self.formLayout_4.setSpacing(6)
        self.formLayout_4.setObjectName("formLayout_4")
        self.lLoopSelect = QtWidgets.QLabel(self.groupBox1_2_2)
        self.lLoopSelect.setWordWrap(False)
        self.lLoopSelect.setObjectName("lLoopSelect")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lLoopSelect)
        self.lneLoopSelect = QtWidgets.QLineEdit(self.groupBox1_2_2)
        self.lneLoopSelect.setMinimumSize(QtCore.QSize(60, 0))
        self.lneLoopSelect.setMaximumSize(QtCore.QSize(32222, 32767))
        self.lneLoopSelect.setObjectName("lneLoopSelect")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lneLoopSelect)
        self.lCaptureOn = QtWidgets.QLabel(self.groupBox1_2_2)
        self.lCaptureOn.setWordWrap(False)
        self.lCaptureOn.setObjectName("lCaptureOn")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lCaptureOn)
        self.lneCaptureOn = QtWidgets.QLineEdit(self.groupBox1_2_2)
        self.lneCaptureOn.setMinimumSize(QtCore.QSize(60, 0))
        self.lneCaptureOn.setMaximumSize(QtCore.QSize(32222, 32767))
        self.lneCaptureOn.setObjectName("lneCaptureOn")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lneCaptureOn)
        self.lCaptureFlag = QtWidgets.QLabel(self.groupBox1_2_2)
        self.lCaptureFlag.setWordWrap(False)
        self.lCaptureFlag.setObjectName("lCaptureFlag")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lCaptureFlag)
        self.lneCaptureFlag = QtWidgets.QLineEdit(self.groupBox1_2_2)
        self.lneCaptureFlag.setMinimumSize(QtCore.QSize(60, 0))
        self.lneCaptureFlag.setMaximumSize(QtCore.QSize(32222, 32767))
        self.lneCaptureFlag.setObjectName("lneCaptureFlag")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lneCaptureFlag)
        self.lOutputMode = QtWidgets.QLabel(self.groupBox1_2_2)
        self.lOutputMode.setWordWrap(False)
        self.lOutputMode.setObjectName("lOutputMode")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lOutputMode)
        self.lneOutputMode = QtWidgets.QLineEdit(self.groupBox1_2_2)
        self.lneOutputMode.setMinimumSize(QtCore.QSize(60, 0))
        self.lneOutputMode.setMaximumSize(QtCore.QSize(32222, 32767))
        self.lneOutputMode.setObjectName("lneOutputMode")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lneOutputMode)
        self.gridLayout.addWidget(self.groupBox1_2_2, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 125, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 1, 2, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 26, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.tabAxisSetup.addTab(self.tab1, "")
        self.gridLayout_3.addWidget(self.tabAxisSetup, 1, 0, 1, 3)
        self.btnUpdate = QtWidgets.QPushButton(formAxisSettings)
        self.btnUpdate.setObjectName("btnUpdate")
        self.gridLayout_3.addWidget(self.btnUpdate, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(185, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 2, 1, 1, 1)
        self.btnClose = QtWidgets.QPushButton(formAxisSettings)
        self.btnClose.setObjectName("btnClose")
        self.gridLayout_3.addWidget(self.btnClose, 2, 2, 1, 1)

        self.retranslateUi(formAxisSettings)
        self.tabAxisSetup.setCurrentIndex(1)
        self.btnUpdate.clicked.connect(formAxisSettings.axisUpdate)
        self.btnClose.clicked.connect(formAxisSettings.close)
        self.lneIx11.returnPressed.connect(formAxisSettings.sendIx11)
        self.lneIx12.returnPressed.connect(formAxisSettings.sendIx12)
        self.lneIx13.returnPressed.connect(formAxisSettings.sendIx13)
        self.lneIx14.returnPressed.connect(formAxisSettings.sendIx14)
        self.lneIx15.returnPressed.connect(formAxisSettings.sendIx15)
        self.lneIx16.returnPressed.connect(formAxisSettings.sendIx16)
        self.lneIx17.returnPressed.connect(formAxisSettings.sendIx17)
        self.lneIx19.returnPressed.connect(formAxisSettings.sendIx19)
        self.lneIx20.returnPressed.connect(formAxisSettings.sendIx20)
        self.lneIx21.returnPressed.connect(formAxisSettings.sendIx21)
        self.lneIx22.returnPressed.connect(formAxisSettings.sendIx22)
        self.lneIx23.returnPressed.connect(formAxisSettings.sendIx23)
        self.lneIx24.returnPressed.connect(formAxisSettings.sendIx24)
        self.lneIx25.returnPressed.connect(formAxisSettings.sendIx25)
        self.lneIx26.returnPressed.connect(formAxisSettings.sendIx26)
        self.lneIx30.returnPressed.connect(formAxisSettings.sendIx30)
        self.lneIx31.returnPressed.connect(formAxisSettings.sendIx31)
        self.lneIx32.returnPressed.connect(formAxisSettings.sendIx32)
        self.lneIx33.returnPressed.connect(formAxisSettings.sendIx33)
        self.lneIx34.returnPressed.connect(formAxisSettings.sendIx34)
        self.lneIx35.returnPressed.connect(formAxisSettings.sendIx35)
        self.lneIx65.returnPressed.connect(formAxisSettings.sendIx65)
        self.lneLoopSelect.returnPressed.connect(formAxisSettings.sendLoopSelect)
        self.lneCaptureOn.returnPressed.connect(formAxisSettings.sendCaptureOn)
        self.lneCaptureFlag.returnPressed.connect(formAxisSettings.sendCaptureFlag)
        self.lneOutputMode.returnPressed.connect(formAxisSettings.sendOutputMode)
        self.tabAxisSetup.currentChanged['int'].connect(formAxisSettings.tabChange)
        QtCore.QMetaObject.connectSlotsByName(formAxisSettings)
        formAxisSettings.setTabOrder(self.lneIx11, self.lneIx12)
        formAxisSettings.setTabOrder(self.lneIx12, self.lneIx13)
        formAxisSettings.setTabOrder(self.lneIx13, self.lneIx14)
        formAxisSettings.setTabOrder(self.lneIx14, self.lneIx15)
        formAxisSettings.setTabOrder(self.lneIx15, self.lneIx16)
        formAxisSettings.setTabOrder(self.lneIx16, self.lneIx17)
        formAxisSettings.setTabOrder(self.lneIx17, self.lneIx19)
        formAxisSettings.setTabOrder(self.lneIx19, self.lneIx20)
        formAxisSettings.setTabOrder(self.lneIx20, self.lneIx21)
        formAxisSettings.setTabOrder(self.lneIx21, self.lneIx22)
        formAxisSettings.setTabOrder(self.lneIx22, self.lneIx23)
        formAxisSettings.setTabOrder(self.lneIx23, self.lneIx24)
        formAxisSettings.setTabOrder(self.lneIx24, self.lneIx25)
        formAxisSettings.setTabOrder(self.lneIx25, self.lneIx26)
        formAxisSettings.setTabOrder(self.lneIx26, self.btnUpdate)
        formAxisSettings.setTabOrder(self.btnUpdate, self.btnClose)

    def retranslateUi(self, formAxisSettings):
        _translate = QtCore.QCoreApplication.translate
        formAxisSettings.setWindowTitle(_translate("formAxisSettings", "Axis setup"))
        self.textLabel1.setText(_translate("formAxisSettings", "Note this screen does not update continously.\n"
"Hit the update button to read out the current values from pmac.\n"
"Write demand values in the text fields and hit enter to send."))
        self.groupBox1.setTitle(_translate("formAxisSettings", "Definition I variables"))
        self.textLabel2.setText(_translate("formAxisSettings", "Ix11:"))
        self.textLabel2_2.setText(_translate("formAxisSettings", "Ix12:"))
        self.textLabel2_3.setText(_translate("formAxisSettings", "Ix13:"))
        self.textLabel2_4.setText(_translate("formAxisSettings", "Ix14:"))
        self.textLabel2_5.setText(_translate("formAxisSettings", "Ix15:"))
        self.textLabel2_6.setText(_translate("formAxisSettings", "Ix16:"))
        self.textLabel2_7.setText(_translate("formAxisSettings", "Ix17:"))
        self.textLabel2_8.setText(_translate("formAxisSettings", "Ix19:"))
        self.groupBox2.setTitle(_translate("formAxisSettings", "Safety I variables"))
        self.textLabel2_9.setText(_translate("formAxisSettings", "Ix20"))
        self.textLabel2_2_2.setText(_translate("formAxisSettings", "Ix21"))
        self.textLabel2_3_2.setText(_translate("formAxisSettings", "Ix22"))
        self.textLabel2_4_2.setText(_translate("formAxisSettings", "Ix23"))
        self.textLabel2_5_2.setText(_translate("formAxisSettings", "Ix24"))
        self.textLabel2_6_2.setText(_translate("formAxisSettings", "Ix25"))
        self.textLabel2_7_2.setText(_translate("formAxisSettings", "Ix26"))
        self.tabAxisSetup.setTabText(self.tabAxisSetup.indexOf(self.tab), _translate("formAxisSettings", "definition and safety"))
        self.groupBox1_2.setTitle(_translate("formAxisSettings", "PID tuning variables"))
        self.textLabel2_10.setText(_translate("formAxisSettings", "ix30:"))
        self.textLabel2_2_3.setText(_translate("formAxisSettings", "Ix31:"))
        self.textLabel2_3_3.setText(_translate("formAxisSettings", "Ix32:"))
        self.textLabel2_4_3.setText(_translate("formAxisSettings", "Ix33:"))
        self.textLabel2_5_3.setText(_translate("formAxisSettings", "Ix34:"))
        self.textLabel2_10_2.setText(_translate("formAxisSettings", "ix35:"))
        self.textLabel2_10_2_2.setText(_translate("formAxisSettings", "ix65:"))
        self.groupBox1_2_2.setTitle(_translate("formAxisSettings", "Signal controls"))
        self.lLoopSelect.setText(_translate("formAxisSettings", "loop select:"))
        self.lCaptureOn.setText(_translate("formAxisSettings", "capture on:"))
        self.lCaptureFlag.setText(_translate("formAxisSettings", "capture flag:"))
        self.lOutputMode.setText(_translate("formAxisSettings", "output mode:"))
        self.tabAxisSetup.setTabText(self.tabAxisSetup.indexOf(self.tab1), _translate("formAxisSettings", "PID and macro"))
        self.btnUpdate.setText(_translate("formAxisSettings", "update"))
        self.btnClose.setText(_translate("formAxisSettings", "close"))


