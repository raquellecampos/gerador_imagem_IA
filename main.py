"""
python -m venv venv (ativar ambiente virtual)
pip install pySide6
pip install requests - baixar imagens que for geradas com a API - baixar na pasta e exibir os dados
pySide6-uic gerador.ui -o ui_main.py - converter arquivo.ui para arquivo.py
"""
import sys
import os
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtGui import QPixmap
from ui_main import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Raquelle - Gerador de Imagens IA')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    