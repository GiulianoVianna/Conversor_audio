
from PyQt5 import uic, QtWidgets 
from pydub import AudioSegment
from PyQt5.QtWidgets import QMessageBox

formato_audio = ""
bitrate_k = ""

def msg_arquivo_audio():
    msg1 = QMessageBox()
    msg1.setIcon(QMessageBox.Critical)
    msg1.setWindowTitle('Atenção')
    msg1.setText('Favor escolher um arquivo de audio!')
    x = msg1.exec_()

def msg_fortmato_audio():
    msg1 = QMessageBox()
    msg1.setIcon(QMessageBox.Critical)
    msg1.setWindowTitle('Atenção')
    msg1.setText('Favor escolher um formato de audio!')
    x = msg1.exec_()

def msg_bitrate_audio():
    msg1 = QMessageBox()
    msg1.setIcon(QMessageBox.Critical)
    msg1.setWindowTitle('Atenção')
    msg1.setText('Favor escolher o bitrate do audio!')
    x = msg1.exec_()



def ler_arquivo():
    arquivo = QtWidgets.QFileDialog.getOpenFileName()[0]
    with open(arquivo) as diretorio: 
        tela.ln_diretorio.setText(diretorio.name)

def convert():

    diretorio = tela.ln_diretorio.text()
    salv_arquivo_diretorio = tela.ln_diretorio.text().replace(".mp3", "")
    formato_audio = tela.cb_formato.currentText()
    bitrate_k = tela.cb_bitrate.currentText()

    if formato_audio == "flv":
        AudioSegment.from_mp3(diretorio).export(salv_arquivo_diretorio + ".flv", format="flv", bitrate = bitrate_k)
    elif formato_audio == "mp4":
        AudioSegment.from_mp3(diretorio).export(salv_arquivo_diretorio + ".mp4", format="mp4", bitrate = bitrate_k) 
    elif formato_audio == "ogg":
        AudioSegment.from_mp3(diretorio).export(salv_arquivo_diretorio + ".ogg", format="ogg", bitrate = bitrate_k) 
    elif formato_audio == "wav":
        AudioSegment.from_mp3(diretorio).export(salv_arquivo_diretorio + ".wav", format="wav", bitrate = bitrate_k)
          
        
def verificar():

    if tela.ln_diretorio.text() != "": 

        if tela.cb_formato.currentText() != "":      

            if tela.cb_bitrate.currentText() != "":
  
                convert()

            else:
                msg_bitrate_audio()

        else:
            msg_fortmato_audio()

    else:
        msg_arquivo_audio()  



app = QtWidgets.QApplication([])
tela = uic.loadUi("convert.ui")
tela.bt_diretorio.clicked.connect(ler_arquivo)
tela.bt_convert.clicked.connect(verificar)

tela.show()
app.exec()
