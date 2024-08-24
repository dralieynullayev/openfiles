import subprocess
import os

# Word fayllarını aç
subprocess.Popen([r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE", r"C:\Users\eynul\OneDrive\İş masası\Yoluxucu Konspekt 2-ci nəşr.docx"])
subprocess.Popen([r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE", r"C:\Users\eynul\OneDrive\İş masası\Yoluxucu sual-cavab tipli konspekt X.docx"])

# PDF-ləri Microsoft Edge ilə aç
subprocess.Popen([r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe", r"C:\Users\eynul\OneDrive\İş masası\1-ci hissə yoluxucu konspekt.pdf"])
subprocess.Popen([r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe", r"C:\Users\eynul\OneDrive\İş masası\5. Kitab\Kitab - Yoluxucu Ə.Vəliyev.pdf"])
subprocess.Popen([r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe", r"C:\Users\eynul\OneDrive\İş masası\Ümumi hissə.pdf"])

# Path to the Telegram shortcut
telegram_path = r"C:\Users\eynul\Telegram Desktop.lnk"

# Open Telegram
os.startfile(telegram_path)
