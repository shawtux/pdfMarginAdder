# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiInformation.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(580, 590)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.groupBoxInput = QGroupBox(self.centralwidget)
        self.groupBoxInput.setObjectName(u"groupBoxInput")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBoxInput.sizePolicy().hasHeightForWidth())
        self.groupBoxInput.setSizePolicy(sizePolicy2)
        self.groupBoxInput.setMaximumSize(QSize(16777215, 210))
        self.gridLayout_2 = QGridLayout(self.groupBoxInput)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.lineEditPathArchivoInput = QLineEdit(self.groupBoxInput)
        self.lineEditPathArchivoInput.setObjectName(u"lineEditPathArchivoInput")
        self.lineEditPathArchivoInput.setEnabled(True)
        self.lineEditPathArchivoInput.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEditPathArchivoInput, 0, 1, 1, 1)

        self.label = QLabel(self.groupBoxInput)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.pushButtonProcess = QPushButton(self.groupBoxInput)
        self.pushButtonProcess.setObjectName(u"pushButtonProcess")

        self.gridLayout_2.addWidget(self.pushButtonProcess, 2, 1, 1, 1)

        self.lineEditPathArchivoOutput = QLineEdit(self.groupBoxInput)
        self.lineEditPathArchivoOutput.setObjectName(u"lineEditPathArchivoOutput")

        self.gridLayout_2.addWidget(self.lineEditPathArchivoOutput, 1, 1, 1, 1)

        self.pushButtonSelectFileInput = QPushButton(self.groupBoxInput)
        self.pushButtonSelectFileInput.setObjectName(u"pushButtonSelectFileInput")

        self.gridLayout_2.addWidget(self.pushButtonSelectFileInput, 2, 0, 1, 1)

        self.pushButtonSelectFileOutput = QPushButton(self.groupBoxInput)
        self.pushButtonSelectFileOutput.setObjectName(u"pushButtonSelectFileOutput")

        self.gridLayout_2.addWidget(self.pushButtonSelectFileOutput, 3, 0, 1, 1)

        self.labelArchivo = QLabel(self.groupBoxInput)
        self.labelArchivo.setObjectName(u"labelArchivo")

        self.gridLayout_2.addWidget(self.labelArchivo, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBoxInput)

        self.horizontalLayoutParameters = QHBoxLayout()
        self.horizontalLayoutParameters.setObjectName(u"horizontalLayoutParameters")
        self.horizontalLayoutParameters.setSizeConstraint(QLayout.SetFixedSize)
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy2.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy2)
        self.groupBox_2.setMinimumSize(QSize(0, 150))
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkBoxFolder = QCheckBox(self.groupBox_2)
        self.checkBoxFolder.setObjectName(u"checkBoxFolder")

        self.verticalLayout.addWidget(self.checkBoxFolder)

        self.pushButtonShowLog = QPushButton(self.groupBox_2)
        self.pushButtonShowLog.setObjectName(u"pushButtonShowLog")
        self.pushButtonShowLog.setMaximumSize(QSize(100, 40))
        self.pushButtonShowLog.setCheckable(True)

        self.verticalLayout.addWidget(self.pushButtonShowLog)


        self.horizontalLayoutParameters.addWidget(self.groupBox_2)

        self.groupBoxMargenes = QGroupBox(self.centralwidget)
        self.groupBoxMargenes.setObjectName(u"groupBoxMargenes")
        sizePolicy2.setHeightForWidth(self.groupBoxMargenes.sizePolicy().hasHeightForWidth())
        self.groupBoxMargenes.setSizePolicy(sizePolicy2)
        self.groupBoxMargenes.setMinimumSize(QSize(0, 150))
        self.lineEdit = QLineEdit(self.groupBoxMargenes)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(125, 44, 61, 60))
        self.lineEdit.setMinimumSize(QSize(40, 40))
        self.lineEdit.setBaseSize(QSize(40, 40))
        self.lineEdit.setInputMethodHints(Qt.ImhNone)
        self.lineEdit.setReadOnly(True)
        self.lineEditLeft = QLineEdit(self.groupBoxMargenes)
        self.lineEditLeft.setObjectName(u"lineEditLeft")
        self.lineEditLeft.setGeometry(QRect(88, 63, 30, 20))
        self.lineEditLeft.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhFormattedNumbersOnly)
        self.lineEditLeft.setMaxLength(3)
        self.lineEditLeft.setAlignment(Qt.AlignCenter)
        self.lineEditRight = QLineEdit(self.groupBoxMargenes)
        self.lineEditRight.setObjectName(u"lineEditRight")
        self.lineEditRight.setGeometry(QRect(190, 63, 30, 20))
        self.lineEditRight.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhFormattedNumbersOnly)
        self.lineEditRight.setMaxLength(3)
        self.lineEditRight.setAlignment(Qt.AlignCenter)
        self.lineEditTop = QLineEdit(self.groupBoxMargenes)
        self.lineEditTop.setObjectName(u"lineEditTop")
        self.lineEditTop.setGeometry(QRect(140, 20, 30, 20))
        self.lineEditTop.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhFormattedNumbersOnly)
        self.lineEditTop.setMaxLength(3)
        self.lineEditTop.setAlignment(Qt.AlignCenter)
        self.lineEditBottom = QLineEdit(self.groupBoxMargenes)
        self.lineEditBottom.setObjectName(u"lineEditBottom")
        self.lineEditBottom.setGeometry(QRect(140, 110, 30, 20))
        self.lineEditBottom.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhFormattedNumbersOnly)
        self.lineEditBottom.setMaxLength(3)
        self.lineEditBottom.setAlignment(Qt.AlignCenter)

        self.horizontalLayoutParameters.addWidget(self.groupBoxMargenes)


        self.verticalLayout_2.addLayout(self.horizontalLayoutParameters)

        self.verticalSpacerLog = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacerLog)

        self.frameLog = QFrame(self.centralwidget)
        self.frameLog.setObjectName(u"frameLog")
        sizePolicy.setHeightForWidth(self.frameLog.sizePolicy().hasHeightForWidth())
        self.frameLog.setSizePolicy(sizePolicy)
        self.frameLog.setMinimumSize(QSize(80, 0))
        self.frameLog.setFrameShape(QFrame.StyledPanel)
        self.frameLog.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frameLog)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.textEditLog = QTextEdit(self.frameLog)
        self.textEditLog.setObjectName(u"textEditLog")

        self.horizontalLayout_4.addWidget(self.textEditLog)


        self.verticalLayout_2.addWidget(self.frameLog)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 580, 22))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PdfMarginAdder", None))
        self.groupBoxInput.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.lineEditPathArchivoInput.setText("")
        self.lineEditPathArchivoInput.setPlaceholderText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Archivo de Salida", None))
        self.pushButtonProcess.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        self.pushButtonSelectFileInput.setText(QCoreApplication.translate("MainWindow", u"Seleccionar\n"
"archivo\n"
"de entrada", None))
        self.pushButtonSelectFileOutput.setText(QCoreApplication.translate("MainWindow", u"Seleccionar\n"
"archivo\n"
"de salida", None))
        self.labelArchivo.setText(QCoreApplication.translate("MainWindow", u"Archivo de Entrada", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Parametros", None))
        self.checkBoxFolder.setText(QCoreApplication.translate("MainWindow", u"Seleccionar Carpeta", None))
        self.pushButtonShowLog.setText(QCoreApplication.translate("MainWindow", u"Mostrar Log", None))
        self.groupBoxMargenes.setTitle(QCoreApplication.translate("MainWindow", u"Margenes", None))
        self.lineEditLeft.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEditLeft.setPlaceholderText("")
        self.lineEditRight.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEditRight.setPlaceholderText("")
        self.lineEditTop.setInputMask("")
        self.lineEditTop.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEditTop.setPlaceholderText("")
        self.lineEditBottom.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEditBottom.setPlaceholderText("")
        self.menuArchivo.setTitle("")
    # retranslateUi

