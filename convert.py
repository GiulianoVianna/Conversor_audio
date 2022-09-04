import pathlib
from PyQt5 import uic, QtWidgets 
from pydub import AudioSegment
from PyQt5.QtWidgets import QMessageBox

formato_audio = ""
bitrate_k = ""


# Mensagens de validação

def msg_arquivo_audio():
    msg1 = QMessageBox()
    msg1.setIcon(QMessageBox.Information)
    msg1.setWindowTitle('Atenção')
    msg1.setText('Favor escolher um arquivo de audio!')
    x = msg1.exec_()

def msg_fortmato_audio():
    msg1 = QMessageBox()
    msg1.setIcon(QMessageBox.Information)
    msg1.setWindowTitle('Atenção')
    msg1.setText('Favor escolher um formato de audio!')
    x = msg1.exec_()

def msg_bitrate_audio():
    msg1 = QMessageBox()
    msg1.setIcon(QMessageBox.Information)
    msg1.setWindowTitle('Atenção')
    msg1.setText('Favor escolher o bitrate do audio!')
    x = msg1.exec_()

def msg_extensao():
    msg1 = QMessageBox()
    msg1.setIcon(QMessageBox.Critical)
    msg1.setWindowTitle('Atenção')
    msg1.setText('A aplicação não encontrou a extensão do arquivo selecionado.\nFavor selecionar um arquivo com a extensão .flv, .mp3, .mp4, .ogg, .wav!')
    x = msg1.exec_()

#################################################################

# Lê o nome do arquivo e endereço do diretório

def ler_arquivo():
    tela.progressBar.setValue(0)
    tela.ln_tipo.setText("")
    arquivo = QtWidgets.QFileDialog.getOpenFileName()[0]
    with open(arquivo) as diretorio: 
        tela.ln_diretorio.setText(diretorio.name)
        file_extension = pathlib.Path(arquivo).suffix        
        tela.ln_tipo.setText(file_extension)

#################################################################

def flv():

    diretorio = tela.ln_diretorio.text()
    salv_arquivo_diretorio = tela.ln_diretorio.text().replace(".flv", "")
    formato_audio = tela.cb_formato.currentText()
    bitrate_k = tela.cb_bitrate.currentText()
 
    if formato_audio == "flv":
        AudioSegment.from_flv(diretorio).export(salv_arquivo_diretorio + ".flv", format="flv", bitrate = bitrate_k)

    elif formato_audio == "mp3":
        AudioSegment.from_flv(diretorio).export(salv_arquivo_diretorio + ".mp3", format="mp3", bitrate = bitrate_k)

    elif formato_audio == "mp4":
        AudioSegment.from_flv(diretorio).export(salv_arquivo_diretorio + ".mp4", format="mp4", bitrate = bitrate_k) 
            
    elif formato_audio == "ogg":
        AudioSegment.from_flv(diretorio).export(salv_arquivo_diretorio + ".ogg", format="ogg", bitrate = bitrate_k) 
    
    elif formato_audio == "wav":        
        AudioSegment.from_flv(diretorio).export(salv_arquivo_diretorio + ".wav", format="wav", bitrate = bitrate_k) 


def mp3():
    diretorio = tela.ln_diretorio.text()
    salv_arquivo_diretorio = tela.ln_diretorio.text().replace(".mp3", "")
    formato_audio = tela.cb_formato.currentText()
    bitrate_k = tela.cb_bitrate.currentText()
 
    if formato_audio == "flv":
        AudioSegment.from_mp3(diretorio).export(salv_arquivo_diretorio + ".flv", format="flv", bitrate = bitrate_k)

    elif formato_audio == "mp3":
        AudioSegment.from_mp3(diretorio).export(salv_arquivo_diretorio + ".mp3", format="mp3", bitrate = bitrate_k)

    elif formato_audio == "mp4":
        AudioSegment.from_mp3(diretorio).export(salv_arquivo_diretorio + ".mp4", format="mp4", bitrate = bitrate_k) 
            
    elif formato_audio == "ogg":
        AudioSegment.from_mp3(diretorio).export(salv_arquivo_diretorio + ".ogg", format="ogg", bitrate = bitrate_k) 
    
    elif formato_audio == "wav":        
        AudioSegment.from_mp3(diretorio).export(salv_arquivo_diretorio + ".wav", format="wav", bitrate = bitrate_k)


def mp4():
    diretorio = tela.ln_diretorio.text()
    salv_arquivo_diretorio = tela.ln_diretorio.text().replace(".mp4", "")
    formato_audio = tela.cb_formato.currentText()
    bitrate_k = tela.cb_bitrate.currentText()
 
    if formato_audio == "flv":
        AudioSegment.from_file(diretorio).export(salv_arquivo_diretorio + ".flv", format="flv", bitrate = bitrate_k)

    elif formato_audio == "mp3":
        AudioSegment.from_file(diretorio).export(salv_arquivo_diretorio + ".mp3", format="mp3", bitrate = bitrate_k)

    elif formato_audio == "mp4":
        AudioSegment.from_file(diretorio).export(salv_arquivo_diretorio + ".mp4", format="mp4", bitrate = bitrate_k) 
            
    elif formato_audio == "ogg":
        AudioSegment.from_file(diretorio).export(salv_arquivo_diretorio + ".ogg", format="ogg", bitrate = bitrate_k) 
    
    elif formato_audio == "wav":        
        AudioSegment.from_file(diretorio).export(salv_arquivo_diretorio + ".wav", format="wav", bitrate = bitrate_k)

def ogg():
    diretorio = tela.ln_diretorio.text()
    salv_arquivo_diretorio = tela.ln_diretorio.text().replace(".ogg", "")
    formato_audio = tela.cb_formato.currentText()
    bitrate_k = tela.cb_bitrate.currentText()
 
    if formato_audio == "flv":
        AudioSegment.from_ogg(diretorio).export(salv_arquivo_diretorio + ".flv", format="flv", bitrate = bitrate_k)

    elif formato_audio == "mp3":
        AudioSegment.from_ogg(diretorio).export(salv_arquivo_diretorio + ".mp3", format="mp3", bitrate = bitrate_k)

    elif formato_audio == "mp4":
        AudioSegment.from_ogg(diretorio).export(salv_arquivo_diretorio + ".mp4", format="mp4", bitrate = bitrate_k) 
            
    elif formato_audio == "ogg":
        AudioSegment.from_ogg(diretorio).export(salv_arquivo_diretorio + ".ogg", format="ogg", bitrate = bitrate_k) 
    
    elif formato_audio == "wav":        
        AudioSegment.from_ogg(diretorio).export(salv_arquivo_diretorio + ".wav", format="wav", bitrate = bitrate_k)


def wav():
    diretorio = tela.ln_diretorio.text()
    salv_arquivo_diretorio = tela.ln_diretorio.text().replace(".wav", "")
    formato_audio = tela.cb_formato.currentText()
    bitrate_k = tela.cb_bitrate.currentText()
 
    if formato_audio == "flv":
        AudioSegment.from_file(diretorio).export(salv_arquivo_diretorio + ".flv", format="flv", bitrate = bitrate_k)

    elif formato_audio == "mp3":
        AudioSegment.from_wav(diretorio).export(salv_arquivo_diretorio + ".mp3", format="mp3", bitrate = bitrate_k)

    elif formato_audio == "mp4":
        AudioSegment.from_wav(diretorio).export(salv_arquivo_diretorio + ".mp4", format="mp4", bitrate = bitrate_k) 
            
    elif formato_audio == "ogg":
        AudioSegment.from_wav(diretorio).export(salv_arquivo_diretorio + ".ogg", format="ogg", bitrate = bitrate_k) 
    
    elif formato_audio == "wav":        
        AudioSegment.from_wav(diretorio).export(salv_arquivo_diretorio + ".wav", format="wav", bitrate = bitrate_k)    


# Regra de validação para os campos obrigatórios

def verificar():

    tela.progressBar.setValue(0)
    if tela.ln_tipo.text() != "":

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
    else:
        
        msg_extensao() 


#################################################################

# Faz a conversão do arquivo conforme o formato escolhido

def convert():

    diretorio = tela.ln_diretorio.text()
    salv_arquivo_diretorio = tela.ln_diretorio.text().replace(".mp3", "")
    formato_audio = tela.cb_formato.currentText()
    bitrate_k = tela.cb_bitrate.currentText()
 
    if tela.ln_tipo.text() == ".flv":

        flv()

    elif tela.ln_tipo.text() == ".mp3": 
        
        mp3()

    elif tela.ln_tipo.text() == ".mp4": 
        
        mp4()

    elif tela.ln_tipo.text() == ".ogg": 
        
        ogg()

    elif tela.ln_tipo.text() == ".wav": 
        
        wav()

    # Atualiza Barra de Progressão

    file_size = len(salv_arquivo_diretorio)
    if file_size > 0:
        for valor in range(101):
            tela.progressBar.setValue(valor)
          
################################################################# 
 

app = QtWidgets.QApplication([])
tela = uic.loadUi("convert.ui")
tela.bt_diretorio.clicked.connect(ler_arquivo)
tela.bt_convert.clicked.connect(verificar)

tela.show()
app.exec()
