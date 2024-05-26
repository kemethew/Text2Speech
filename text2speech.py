import tkinter
import tkinter.filedialog
import pyttsx3
import docx

file_path = "KP add - GBS DRAFT.docx"
if file_path == "":
    root = tkinter.Tk()
    root.withdraw()
    file_path = tkinter.filedialog.askopenfilename()

tts = pyttsx3.init()
speech_rate = tts.getProperty('rate')
tts.setProperty('rate', speech_rate-30)
print(tts.getProperty('rate'))
file = docx.Document(file_path)
full_text = ""
for para in file.paragraphs:
    full_text += para.text

tts.say(full_text)
tts.runAndWait()