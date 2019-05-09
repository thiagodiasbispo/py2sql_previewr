# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/py2sql_base.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Py2Sql_base(object):
    def setupUi(self, Py2Sql_base):
        Py2Sql_base.setObjectName("Py2Sql_base")
        Py2Sql_base.resize(783, 515)
        self.gridLayout = QtWidgets.QGridLayout(Py2Sql_base)
        self.gridLayout.setObjectName("gridLayout")
        self.statuslabel = QtWidgets.QLabel(Py2Sql_base)
        self.statuslabel.setFrameShape(QtWidgets.QFrame.Box)
        self.statuslabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.statuslabel.setText("")
        self.statuslabel.setObjectName("statuslabel")
        self.gridLayout.addWidget(self.statuslabel, 3, 0, 1, 2)
        self.queryEditorGroupBox = QtWidgets.QGroupBox(Py2Sql_base)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.queryEditorGroupBox.sizePolicy().hasHeightForWidth()
        )
        self.queryEditorGroupBox.setSizePolicy(sizePolicy)
        self.queryEditorGroupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.queryEditorGroupBox.setFont(font)
        self.queryEditorGroupBox.setStyleSheet("QGroupBox { font-weight: bold; }")
        self.queryEditorGroupBox.setObjectName("queryEditorGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.queryEditorGroupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.queryEditor = QtWidgets.QTextEdit(self.queryEditorGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.queryEditor.sizePolicy().hasHeightForWidth())
        self.queryEditor.setSizePolicy(sizePolicy)
        self.queryEditor.setMinimumSize(QtCore.QSize(0, 0))
        self.queryEditor.setBaseSize(QtCore.QSize(0, 120))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        self.queryEditor.setFont(font)
        self.queryEditor.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents
        )
        self.queryEditor.setObjectName("queryEditor")
        self.verticalLayout.addWidget(self.queryEditor)
        self.layoutQuerySourceActions = QtWidgets.QHBoxLayout()
        self.layoutQuerySourceActions.setContentsMargins(1, 1, 1, 1)
        self.layoutQuerySourceActions.setSpacing(6)
        self.layoutQuerySourceActions.setObjectName("layoutQuerySourceActions")
        self.livePreviewCheckBox = QtWidgets.QCheckBox(self.queryEditorGroupBox)
        self.livePreviewCheckBox.setChecked(True)
        self.livePreviewCheckBox.setObjectName("livePreviewCheckBox")
        self.layoutQuerySourceActions.addWidget(self.livePreviewCheckBox)
        self.formatCodeBeforeSaveCheckBox = QtWidgets.QCheckBox(
            self.queryEditorGroupBox
        )
        self.formatCodeBeforeSaveCheckBox.setObjectName("formatCodeBeforeSaveCheckBox")
        self.layoutQuerySourceActions.addWidget(self.formatCodeBeforeSaveCheckBox)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.layoutQuerySourceActions.addItem(spacerItem)
        self.openQueryButton = QtWidgets.QPushButton(self.queryEditorGroupBox)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("./img/btn_open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.openQueryButton.setIcon(icon)
        self.openQueryButton.setObjectName("openQueryButton")
        self.layoutQuerySourceActions.addWidget(self.openQueryButton)
        self.saveQueryButton = QtWidgets.QPushButton(self.queryEditorGroupBox)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap("img/python.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.saveQueryButton.setIcon(icon1)
        self.saveQueryButton.setObjectName("saveQueryButton")
        self.layoutQuerySourceActions.addWidget(self.saveQueryButton)
        self.verticalLayout.addLayout(self.layoutQuerySourceActions)
        self.gridLayout.addWidget(self.queryEditorGroupBox, 0, 0, 3, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Py2Sql_base)
        self.groupBox_2.setStyleSheet("QGroupBox { font-weight: bold; }")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.sqlPreviewr = QtWidgets.QTextEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("FreeMono")
        font.setPointSize(12)
        self.sqlPreviewr.setFont(font)
        self.sqlPreviewr.setReadOnly(True)
        self.sqlPreviewr.setObjectName("sqlPreviewr")
        self.verticalLayout_2.addWidget(self.sqlPreviewr)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_2.addItem(spacerItem1)
        self.exportSqlPreviewButton = QtWidgets.QPushButton(self.groupBox_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap("img/sql.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.exportSqlPreviewButton.setIcon(icon2)
        self.exportSqlPreviewButton.setObjectName("exportSqlPreviewButton")
        self.horizontalLayout_2.addWidget(self.exportSqlPreviewButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.dockWidget = QtWidgets.QDockWidget(Py2Sql_base)
        self.dockWidget.setStyleSheet("QDockWidget {font-weight: bold; }")
        self.dockWidget.setFloating(False)
        self.dockWidget.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.dockWidget.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.queryResultTableView = QtWidgets.QTableView(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.queryResultTableView.sizePolicy().hasHeightForWidth()
        )
        self.queryResultTableView.setSizePolicy(sizePolicy)
        self.queryResultTableView.setMaximumSize(QtCore.QSize(16777215, 400))
        self.queryResultTableView.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded
        )
        self.queryResultTableView.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow
        )
        self.queryResultTableView.setAlternatingRowColors(True)
        self.queryResultTableView.setGridStyle(QtCore.Qt.DashLine)
        self.queryResultTableView.setObjectName("queryResultTableView")
        self.queryResultTableView.horizontalHeader().setCascadingSectionResizes(True)
        self.verticalLayout_4.addWidget(self.queryResultTableView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(self.dockWidgetContents)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.exportToHtmlButton = QtWidgets.QPushButton(self.dockWidgetContents)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap("img/html.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.exportToHtmlButton.setIcon(icon3)
        self.exportToHtmlButton.setObjectName("exportToHtmlButton")
        self.horizontalLayout.addWidget(self.exportToHtmlButton)
        self.exportToCSVButton = QtWidgets.QPushButton(self.dockWidgetContents)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(
            QtGui.QPixmap("img/csv.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.exportToCSVButton.setIcon(icon4)
        self.exportToCSVButton.setObjectName("exportToCSVButton")
        self.horizontalLayout.addWidget(self.exportToCSVButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.dockWidget.setWidget(self.dockWidgetContents)
        self.gridLayout.addWidget(self.dockWidget, 1, 1, 1, 1)

        self.retranslateUi(Py2Sql_base)
        QtCore.QMetaObject.connectSlotsByName(Py2Sql_base)
        Py2Sql_base.setTabOrder(self.queryEditor, self.openQueryButton)
        Py2Sql_base.setTabOrder(self.openQueryButton, self.saveQueryButton)

    def retranslateUi(self, Py2Sql_base):
        _translate = QtCore.QCoreApplication.translate
        Py2Sql_base.setWindowTitle(_translate("Py2Sql_base", "Qt SQL Browser"))
        self.queryEditorGroupBox.setTitle(_translate("Py2Sql_base", "Query editor"))
        self.livePreviewCheckBox.setText(_translate("Py2Sql_base", "Live preview"))
        self.formatCodeBeforeSaveCheckBox.setText(
            _translate("Py2Sql_base", "Format code before save")
        )
        self.openQueryButton.setText(_translate("Py2Sql_base", "&Open query"))
        self.saveQueryButton.setText(_translate("Py2Sql_base", "&Save query"))
        self.saveQueryButton.setShortcut(_translate("Py2Sql_base", "Ctrl+S"))
        self.groupBox_2.setTitle(_translate("Py2Sql_base", "SQL preview"))
        self.exportSqlPreviewButton.setText(_translate("Py2Sql_base", "&Export SQL"))
        self.exportSqlPreviewButton.setShortcut(_translate("Py2Sql_base", "Ctrl+E"))
        self.dockWidget.setWindowTitle(_translate("Py2Sql_base", "Query result"))
        self.label.setText(_translate("Py2Sql_base", "Exporto to:"))
        self.exportToHtmlButton.setText(_translate("Py2Sql_base", "HTML"))
        self.exportToCSVButton.setText(_translate("Py2Sql_base", "CSV"))
