# This Python file uses the following encoding: utf-8
import logging
import os
import sys
from pathlib import Path

from pdfCropMargins import crop
from PySide6.QtGui import QIntValidator
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (QApplication, QFileDialog, QMainWindow, QMessageBox)

from ui.ui_uiInformation import Ui_MainWindow

fileExtensions = [".pdf"]

fileExtensionString = ""

currentButton = ""

logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', level=logging.DEBUG, datefmt="%d/%m/%Y %I:%M:%S %p")



for strIn in fileExtensions:
    if fileExtensionString == '':
        fileExtensionString = "*"+strIn
    else:
        fileExtensionString = fileExtensionString +", *"+strIn

# https://pypi.org/project/pdfCropMargins/
# -a4 BP BP BP BP  The four floating point arguments should be the left, bottom, right, and top offset values, respectively

# pipenv run pyinstaller --onefile --windowed --name PdfMarginAdder mainwindow.py

def processPdf(inputFile,outPutFile, bottom, top, left, right, textEditLog):

    logging.info("bottom modificator: "+bottom)
    logging.info("top modificator: "+top)
    logging.info("left modificator: "+left)
    logging.info("right modificator: "+right)

    textEditLog.insertPlainText("input file: "+inputFile+"\n")
    if( not outPutFile):
        output_doc_pathname, exit_code, stdout_str, stderr_str = crop(["-p", "0","-p", "100", "-a4", str(int(left) * 72), str(int(bottom) * 72), str(int(right) * 72), str(int(top) * 72), inputFile])
        
        textEditLog.insertPlainText("output file: "+output_doc_pathname+"\n")
    else:
        output_doc_pathname, exit_code, stdout_str, stderr_str = crop(["-p", "0","-p", "100", "-a4", str(int(left) * 72), str(int(bottom) * 72), str(int(right) * 72), str(int(top) * 72), "-o", outPutFile, inputFile])
    
    textEditLog.insertPlainText("-----\n")
    # crop(["-p", "0", "-a4", "0","0", "-50","-10" ,"-o", outPutFile, inputFile])


class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):

        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.frameLog.setHidden(True)
        self.pushButtonSelectFileInput.clicked.connect(lambda x: self.loadFile(self.lineEditPathArchivoInput,self.checkBoxFolder,"input"))
        self.pushButtonSelectFileOutput.clicked.connect(lambda x: self.loadFile(self.lineEditPathArchivoOutput,self.checkBoxFolder,"output"))
        self.lineEditBottom.setValidator( QIntValidator(-10,0,self))
        self.lineEditTop.setValidator( QIntValidator(-10,0,self))
        self.lineEditLeft.setValidator( QIntValidator(-10,0,self))
        self.lineEditRight.setValidator( QIntValidator(-10,0,self))

        self.pushButtonProcess.clicked.connect(self.pdfCreator)
        self.pushButtonShowLog.clicked.connect(self.showLogFile)
        

    def loadFile(self, textBox, checkboxInput, typeIO):

        if not checkboxInput.isChecked():
            if typeIO == "input":
                filename, ok = QFileDialog.getOpenFileName(self,None,None,"Documentos ("+fileExtensionString+")")
                if filename:
                    logging.info("file input: "+filename)
                    path = Path(filename)
                    textBox.setText(str(path))
            if typeIO == "output":
                filename, ok = QFileDialog.getSaveFileName(self,None,None,"Documentos ("+fileExtensionString+")")
                if filename:
                    logging.info("file output: "+filename)
                    path = Path(filename)
                    textBox.setText(str(path))    
        else:
            dir = QFileDialog.getExistingDirectory(None,"Seleccionar Directorio","D:\Download\MBA",options=QFileDialog.ShowDirsOnly)
            if dir:
                logging.info(str(dir))
                textBox.setText(str(dir))
     

    def load_ui(w):
        w.setWindowTitle("MainWindow Title")
    


    def pdfCreator(self):
        topMargin = str(int(self.lineEditTop.text())*-1)
        bottomMargin = str(int(self.lineEditBottom.text())*-1)
        leftMargin = str(int(self.lineEditLeft.text())*-1)
        rightMargin = str(int(self.lineEditRight.text())*-1)
        logging.info("Input path: "+self.lineEditPathArchivoInput.text())
        logging.info("Output path: "+self.lineEditPathArchivoOutput.text())
        if self.lineEditPathArchivoInput.text():
            if not self.checkBoxFolder.isChecked():
                processPdf(self.lineEditPathArchivoInput.text(),self.lineEditPathArchivoOutput.text(),bottomMargin, topMargin, leftMargin, rightMargin, self.textEditLog)
            else:
                for file in os.listdir(self.lineEditPathArchivoInput.text()):
                    if file.endswith(tuple(fileExtensions)):
                        if not self.lineEditPathArchivoOutput.text():
                            if not os.path.exists(self.lineEditPathArchivoInput.text()+"/output/"):
                                os.makedirs(self.lineEditPathArchivoInput.text()+"/output/")
                            processPdf(self.lineEditPathArchivoInput.text()+"/"+file,self.lineEditPathArchivoInput.text()+"/output/"+file, bottomMargin, topMargin, leftMargin, rightMargin, self.textEditLog)
                        else:
                            processPdf(self.lineEditPathArchivoInput.text()+"/"+file,self.lineEditPathArchivoOutput.text()+"/"+file, bottomMargin, topMargin, leftMargin, rightMargin, self.textEditLog)


        else:
            #TODO popup para cuando faltan ambos archivos
            logging.error("pending logic")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Texto de entrada no ha sido ingresado")
            msg.setWindowTitle("Error")
            #msg.setDetailedText("The details are as follows:")
            msg.exec_()

    def showLogFile(self):
        logging.info("Pressed")
        if self.pushButtonShowLog.isChecked():
            self.frameLog.setVisible(True)
        else:       
            self.frameLog.setHidden(True)

if __name__ == "__main__":
    logging.info("Starting app")
    loader = QUiLoader()
    app = QApplication(sys.argv)
    #window = loader.load(Path(__file__).resolve().parent / "ui\\uiInformation.ui", None)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())



