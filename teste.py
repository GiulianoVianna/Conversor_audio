from PyQt5 import uic, QtWidgets
import time

def botao():
    progresso()


def progresso():   
    for valor in range(101):
        time.sleep(0.2)
        tela.progressBar.setValue(valor)
    

app=QtWidgets.QApplication([])
tela=uic.loadUi("progressao.ui")
tela.bt_start.clicked.connect(botao)
tela.show()
app.exec()

