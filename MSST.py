import PySimpleGUI as sg
import pyperclip
import shutil
import zipfile
import pyAesCrypt
import base64
import os
import io
import re
def base64_d(b):
    return base64.b64decode(b.encode('utf-8'))
def rmd(directory):
    try:
        shutil.rmtree(os.path.join(os.path.abspath(os.path.dirname(__file__)), directory))
    except:
        pass
def rm(file):
    try:
        os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)), file))
    except:
        pass
def rmfiles_e():
    try:
        rmd("1")
        rm("name.aes")
        rm("n.text")
        rm(outputf)
    except:
        pass
def rmfiles_d():
    try:
        rmd("2")
        rm("name1.aes")
        rm("n1.text")
        rm("doc.aes")
    except:
        pass
def ext_file(p):
    try:
            root, extension = os.path.splitext(os.path.join(os.path.abspath(os.path.dirname(__file__)), p))
            return extension
    except:
        pass
rmfiles_e()
rmfiles_d()
sg.theme('DarkBlue4')
progressbar = [[sg.ProgressBar(5, orientation='h', size=(36, 15), key='progressbar')]]
layout = [
    [sg.Text('MS File:'), sg.InputText(key='-file1-', do_not_clear=False), sg.FileBrowse("...",file_types=(("MS Files", "*.docx"),("MS Files", "*.pptx"),("MS Files", "*.xlsx")))
     ],
    [sg.Text('Cry File:'), sg.InputText(key='-file2-', do_not_clear=False), sg.FileBrowse("...")],
    [sg.Text('Password:'), sg.InputText(key='-pswd-', do_not_clear=True,password_char='*')],
    [sg.Frame('Progress',layout= progressbar)],
    [sg.Button("Encrypt and Hide"), sg.Button('Decrypt and Show'), sg.Button('About'),sg.Cancel("Exit")]
]
window = sg.Window('MS Stenography Tool by LordAT1', layout)
progress_bar = window['progressbar']
while True:                                                         # The Event Loop
    try:
        event, values = window.read()
        # print(event, values) #debug
        if event in (None, 'Exit', 'Cancel'):
                break
        if event == 'Encrypt and Hide':
                word = values['-file1-']
                inputf = values['-file2-']
                password = values['-pswd-']
                outputf=inputf+".aes"
                outputname="name.aes"
                progress_bar.UpdateBar(1)
                with open("n.text", 'w') as f:
                        f.write(os.path.basename(inputf))
                progress_bar.UpdateBar(2)
                pyAesCrypt.encryptFile("n.text", outputname, password)
                pyAesCrypt.encryptFile(inputf, outputf, password)
                with open(outputf, "rb") as f:
                        str1 = base64.b64encode(f.read()).decode('utf-8')
                with open(outputname, "rb") as f:
                        str2 = base64.b64encode(f.read()).decode('utf-8')
                with zipfile.ZipFile(word,"r") as zip_ref:
                        zip_ref.extractall("1")
                progress_bar.UpdateBar(3)
                os.chdir("1")
                with open("[Content_Types].xml", 'a') as f:
                        f.write("\n<!--"+str1+"-->")
                        f.write("\n<!--"+str2+"-->")
                progress_bar.UpdateBar(4)
                os.chdir("..")
                shutil.make_archive(word[0:-5]+"_cry", 'zip', "1")
                ext=ext_file(word)
                os.rename(word[0:-5]+"_cry"+'.zip', word[0:-5]+"_cry"+ext)
                progress_bar.UpdateBar(5)
                rm(inputf)
                rmfiles_e()
                progress_bar.UpdateBar(0)
                sg.popup("Your file encrypted in "+word[0:-5]+"_cry"+ext)
        if event == 'Decrypt and Show':
                word = values['-file1-']
                password = values['-pswd-']
                with zipfile.ZipFile(word,"r") as zip_ref:
                        zip_ref.extractall("2")
                progress_bar.UpdateBar(1)
                os.chdir("2")
                with open("[Content_Types].xml", 'r',encoding="utf8") as f:
                        ff=base64_d(f.readlines()[-2][4:-3])
                        os.chdir("..")
                        with open("doc.aes", 'wb') as f:
                                        f.write(ff)
                progress_bar.UpdateBar(2)
                os.chdir("2")
                with open("[Content_Types].xml", 'r',encoding="utf8") as f:
                        ffn=base64_d(f.readlines()[-1][4:-3])
                        progress_bar.UpdateBar(3)
                        os.chdir("..")
                        with open("name1.aes", 'wb') as f:
                                        f.write(ffn)
                pyAesCrypt.decryptFile("name1.aes", "n1.text", password)
                progress_bar.UpdateBar(4)
                nn=""
                with open("n1.text", 'r') as f:
                        nn=f.readlines()[-1]
                        pyAesCrypt.decryptFile("doc.aes",nn, password)
                progress_bar.UpdateBar(5)
                rmfiles_d()
                progress_bar.UpdateBar(0)
                sg.popup("File "+nn+ " Extracted!")
        if event == 'About':
                l=[[sg.Text('MS Stenography Tool created for encrypting and hiding your any files in Microsoft Office Documents(DOCX,PPTX,XLSX).The structure \nof the documents will be not violated! WARNING! If you will be changed encrypted document in MS Office then hidden encrypted information\nwill be vanished! Coded by LordAT1.')],[sg.Text('\n Support the project please.\n Monero:\n43kpHUzR5otCHnqYJxDNz3S4uPBaKq6YCBwY4BtnCCABEhRpbbYud8nf4PCYbL2HxqgbzGQesJ13m4nPMbtZeuJW4cquM3R')],[sg.Button("Copy Monero"),sg.Button("Close")]]
                ab=sg.Window("About",l)
                while True:  
                        try:
                                event1, values1 = ab.read()
                                if event1 == 'Close':
                                        ab.close()
                                        break
                                if event1 == 'Copy Monero':
                                        pyperclip.copy("43kpHUzR5otCHnqYJxDNz3S4uPBaKq6YCBwY4BtnCCABEhRpbbYud8nf4PCYbL2HxqgbzGQesJ13m4nPMbtZeuJW4cquM3R")
                                if event1 == sg.WIN_CLOSED:
                                        break
                        except:
                                pass
    except():
        pass
window.close()