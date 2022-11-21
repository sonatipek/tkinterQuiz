# Bilgisayar Lab. I - 3 No'lu Bilgisayar | Sonat Saygın İPEK & 90210000216
import tkinter as tk

# Class Tanımlaması
class Bilgiler:
    # Örnek Nitelik (class çağırıldığında çalışacak fonksiyon)
    def __init__(self, name, surname, username, job, authority):
        self.name = name
        self.surname = surname
        self.username = username
        self.job = job
        self.authority = authority
        
        self.buttonConsoleWrite()
        
    # Bilgileri consola yazdıran fonksiyon
    def buttonConsoleWrite(self):
        print(f"Adı:\t\t{self.name}\nSoyadı:\t\t{self.surname}\nKullanıcı Adı:\t{self.username}\nGörvi:\t\t{self.job}\nYetkisi:\t{self.authority}")

# Fonksiyonlar
# Label oluşturma fonksiyonu
def createLabel(labelName, labelText, xEksen, yEksen):
    labelName = tk.Label(mainWindow, text=labelText)
    labelName.place(x=xEksen, y=yEksen)

# Input oluşturma fonksiyonu
def createInput(inputName, xEksen, yEksen):
    inputName = tk.Entry(mainWindow)
    inputName.place(x=xEksen, y=yEksen)
    
    return inputName

# Button oluşturma fonksiyonu
def createButton(buttonName, buttonText, buttonCommand, xEksen, yEksen):
    buttonName = tk.Button(mainWindow, text=buttonText, command=buttonCommand)
    buttonName.place(x=xEksen, y=yEksen)
    
# Bilgileri örnek niteliğe gönderme fonksiyonu
def sendToClass():
    nameInfo = nameGet.get()
    surnameInfo = surnameGet.get()
    usernameInfo = usernameGet.get()
    jobInfo = jobGet.get()
    authorityInfo = authorityGet.get()
    
    bilgileriGonder = Bilgiler(nameInfo, surnameInfo, usernameInfo, jobInfo, authorityInfo)
    

# Window Başlangıç
mainWindow = tk.Tk()

# Main Window Ayarlamaları
mainWindow.title("User Login")
mainWindow.geometry("300x200+100+200")
mainWindow.resizable(False, False)

# Name Input ve Label
createLabel("nameLbl", "Ad:", "0", "0")
nameGet = createInput("nameEntry", "80", "0")

# Surname Input ve Label
createLabel("surnameLbl", "Soyad:", "0", "30")
surnameGet = createInput("surnameEntry", "80", "30")

# User name Input ve Label
createLabel("usernameLbl", "Kullanıcı Adı:", "0", "60")
usernameGet = createInput("usernameEntry", "80", "60")

# Job Input ve Label
createLabel("jobLbl", "Görev:", "0", "90")
jobGet = createInput("jobEntry", "80", "90")

# Authority Input ve Label
createLabel("authorityLbl", "Yetki (0-5):", "0", "120")
authorityGet = createInput("authorityEntry", "80", "120")

# Button
createButton("enterBtn", "Giriş", sendToClass, "0", "150")

# Window Bitiş
mainWindow.mainloop()