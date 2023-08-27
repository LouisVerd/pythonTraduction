from PIL import Image as Images
import pytesseract
from deep_translator import GoogleTranslator
from pdf2image import convert_from_path
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from VoiceRec import VoiceRec

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

voiceR = VoiceRec()
textFromImage = ""

root = Tk(className="First application")
root.geometry("600x400")
frm = ttk.Frame(root)
frm.grid()
ttk.Label(frm, text="Texte a traduire").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=3)

entry = ttk.Entry(frm)
entry.grid(column=1, row=0)

def translateAng():
    if "selected" in angCb.state():
        frCB.state(['!selected'])
        frCB.state(['!alternate'])
        textTranslate = GoogleTranslator(source="fr", target='en').translate(text=entry.get())
        translateLabel.config(text=textTranslate)

        if textImage.cget("text") != "":
            imageTrad = GoogleTranslator(source="fr", target='en').translate(text=textImage.cget("text"))
            tradImage.config(text=imageTrad)

def translateFr():
    #traduction text entrez par l'utilisateur
    if "selected" in frCB.state():
        angCb.state(['!selected'])
        angCb.state(['!alternate'])
        textTranslate = GoogleTranslator(source="en", target='fr').translate(text=entry.get())
        translateLabel.config(text=textTranslate)

        #traduction fichier entrez par l'utilisateur
        if textImage.cget("text") != "":
            imageTrad = GoogleTranslator(source="en", target='fr').translate(text=textImage.cget("text"))
            tradImage.config(text=imageTrad)

        #traduction vocal entrez par l'utilisateur
        if textVocaltrad.cget("text") != "":
            voiceTrad = GoogleTranslator(source="en", target='fr').translate(text=textVocaltrad.cget("text"))
            textVocaltrad.config(text=voiceTrad)
    
translateLabel = ttk.Label(frm, text="")
translateLabel.grid(column=4, row=0)

frCB = ttk.Checkbutton(frm, text="francais", command=translateFr)
frCB.grid(column=1, row=3)

angCb = ttk.Checkbutton(frm, text="anglais", command=translateAng)
angCb.grid(column=1, row=4)

#open an image and get the text in it
def openFile():
    filename = fd.askopenfilename()
    textFromImage = (pytesseract.image_to_string(Images.open(filename), lang="eng"))
    textImage.config(text=textFromImage)
    ttk.Label(frm, text="Texte contenu dans l'image: ", font="bold").grid(column=5, row=2)

ttk.Button(frm, text="Choisir un fichier", command=openFile).grid(column=5, row=0)
#Contenu de l'image
textImage = ttk.Label(frm, text="")
textImage.grid(column=5, row=4)
#Contenu de l'image traduit
tradImage = ttk.Label(frm, text="")
tradImage.grid(column=5, row=5)

def vocal():
    vocalText = voiceR.getVoiceText()
    textVocaltrad.config(text=vocalText)

ttk.Button(frm, text="Vocal", command=vocal).grid(column=0, row=10)
textVocaltrad = ttk.Label(frm, text="")
textVocaltrad.grid(column=1, row=10)

root.mainloop()