# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gerador.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(611, 813)
        MainWindow.setStyleSheet(u"background: rgb(58, 58, 58)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title_frame = QFrame(self.centralwidget)
        self.title_frame.setObjectName(u"title_frame")
        self.title_frame.setFrameShape(QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.title_frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 0, 251, 61))
        self.label.setStyleSheet(u"color: rgb(255,255,255);")

        self.verticalLayout.addWidget(self.title_frame)

        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setStyleSheet(u"QFrame{\n"
"background-color: rgb(38,38,38);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLabel{\n"
"border: 1.4px solid white;\n"
"}")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.main_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_esquerda = QPushButton(self.frame)
        self.btn_esquerda.setObjectName(u"btn_esquerda")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.btn_esquerda.setFont(font)
        self.btn_esquerda.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_esquerda, 0, Qt.AlignLeft)

        self.btn_direita = QPushButton(self.frame)
        self.btn_direita.setObjectName(u"btn_direita")
        self.btn_direita.setFont(font)
        self.btn_direita.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_direita, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame)

        self.lbl_img = QLabel(self.main_frame)
        self.lbl_img.setObjectName(u"lbl_img")
        self.lbl_img.setMinimumSize(QSize(512, 500))

        self.verticalLayout_2.addWidget(self.lbl_img)


        self.verticalLayout.addWidget(self.main_frame)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(42,42,42);\n"
"    color: rgb(245,245,245)\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: solid 0px;\n"
"	border-radius: 15px;\n"
"	font: 75 16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0,170,255);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.main_container)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.edt_descricao = QLineEdit(self.main_container)
        self.edt_descricao.setObjectName(u"edt_descricao")
        self.edt_descricao.setMinimumSize(QSize(0, 100))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setItalic(True)
        self.edt_descricao.setFont(font1)
        self.edt_descricao.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.edt_descricao)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.edt_nome_arquivo = QLineEdit(self.main_container)
        self.edt_nome_arquivo.setObjectName(u"edt_nome_arquivo")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(11)
        font2.setItalic(True)
        self.edt_nome_arquivo.setFont(font2)
        self.edt_nome_arquivo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.edt_nome_arquivo)

        self.btn_gerar = QPushButton(self.main_container)
        self.btn_gerar.setObjectName(u"btn_gerar")
        self.btn_gerar.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_2.addWidget(self.btn_gerar)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Gerador de Imagens IA</span></p></body></html>", None))
        self.btn_esquerda.setText(QCoreApplication.translate("MainWindow", u"<<", None))
        self.btn_direita.setText(QCoreApplication.translate("MainWindow", u">>", None))
        self.lbl_img.setText("")
        self.edt_descricao.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Informe o texto para ser gerado a sua imagem. O texto deve ser em ingl\u00eas", None))
        self.edt_nome_arquivo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome do arquivo", None))
        self.btn_gerar.setText(QCoreApplication.translate("MainWindow", u"Gerar", None))
    # retranslateUi

