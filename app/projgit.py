#!/usr/bin/env python3

# Copyright (C) 22022 MuKonqi (Muhammed Abdurrahman)

# Projgit is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Projgit is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Projgit.  If not, see <https://www.gnu.org/licenses/>.

from tkinter import *
from tkinter import messagebox
import os
import getpass
username=getpass.getuser()

lang_en="/home/"+username+"/.config/projgit/lang/en.txt"
lang_tr="/home/"+username+"/.config/projgit/lang/tr.txt"

def settings():
    if not os.path.isfile("/home/"+username+"/.config/projgit/theme/dark.txt") and not os.path.isfile("/home/"+username+"/.config/projgit/theme/light.txt"):
        bg="#000000"
        fg="#FFFFFF"
        button_bg="#FFFFFF"
        button_fg="#000000"
        a_button_bg="#000000"
        a_button_fg="#FFFFFF"
    if os.path.isfile("/home/"+username+"/.config/projgit/theme/dark.txt"):
        bg="#000000"
        fg="#FFFFFF"
        button_bg="#FFFFFF"
        button_fg="#000000"
        a_button_bg="#000000"
        a_button_fg="#FFFFFF"
    elif os.path.isfile("/home/"+username+"/.config/projgit/theme/light.txt"):
        bg="#FFFFFF"
        fg="#000000"
        button_bg="#000000"
        button_fg="#FFFFFF"
        a_button_bg="#FFFFFF"
        a_button_fg="#000000"
    def dark():
        os.system("cd /home/"+username+"/.config/projgit/theme/ ; rm * ; touch dark.txt")
        if os.path.isfile(lang_en):
            messagebox.showinfo("Information","Successful! Dark theme applied.")
        if os.path.isfile(lang_tr):
            messagebox.showinfo("Bilgilendirme","Başarılı! Koyu tema uygulandı.")
        exit()
    def light():
        os.system("cd /home/"+username+"/.config/projgit/theme/ ; rm * ; touch light.txt")
        if os.path.isfile(lang_en):
            messagebox.showinfo("Information","Successful! Light theme applied.")
        if os.path.isfile(lang_tr):
            messagebox.showinfo("Bilgilendirme","Başarılı! Açık tema uygulandı.")
        exit()
    def langen():
        os.system("cd /home/"+username+"/.config/projgit/lang/ ; rm * ; touch en.txt")
        messagebox.showinfo("Information","Successful! English language applied.")
        exit()
    def langtr():
        os.system("cd /home/"+username+"/.config/projgit/lang/ ; rm * ; touch tr.txt")
        messagebox.showinfo("Bilgilendirme","Başarılı! Türkçe dili uygulandı.") 
        exit()       
    window2=Tk()
    window2.config(background=bg)
    window2.resizable(0, 0)
    if os.path.isfile(lang_en):
        window2.title("Settings | Projgit")
        text11=Label(window2, background=bg, foreground=fg, font="arial 10 bold", text="Please select the theme you want to apply.")
        space11=Label(window2, background=bg, foreground=fg, font="arial 3", text="\n")
        button11=Button(window2, text="Dark", command=dark, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font=",arial 10", cursor="hand2", borderwidth="3 ")
        button12=Button(window2, text="Light", command=light, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3" )
        space2=Label(window2, background=bg, foreground=fg, font="arial 3", text="\n\n")
        text12=Label(window2, background=bg, foreground=fg, font="arial 10 bold", text="You can change your language preferences below.")
        space12=Label(window2, background=bg, foreground=fg, font="arial 3", text="\n")
        button13=Button(window2, text="English (English)", command=langen, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font=",arial 10", cursor="hand2", borderwidth ="3")
        button14=Button(window2, text="Turkish (Turkish)", command=langtr, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth= "3")
    if os.path.isfile(lang_tr):
        window2.title("Ayarlar | Projgit")
        text11=Label(window2, background=bg, foreground=fg, font="arial 10 bold", text="Lütfen uygulamak istediğiniz temayı seçiniz.")
        space11=Label(window2, background=bg, foreground=fg, font="arial 3", text="\n")
        button11=Button(window2, text="Koyu", command=dark, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg,  font=",arial 10", cursor="hand2", borderwidth="3")
        button12=Button(window2, text="Açık", command=light, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        space2=Label(window2, background=bg, foreground=fg, font="arial 3", text="\n\n")
        text12=Label(window2, background=bg, foreground=fg, font="arial 10 bold", text="Aşağıdan dil tercihlerinizi değiştirebilirsiniz.")
        space12=Label(window2, background=bg, foreground=fg, font="arial 3", text="\n")
        button13=Button(window2, text="English (İngilizce)", command=langen, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg,  font=",arial 10", cursor="hand2", borderwidth="3")
        button14=Button(window2, text="Türkçe (Turkish)", command=langtr, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
    text11.pack()
    space11.pack()
    button11.pack()
    button12.pack()
    space2.pack()
    text12.pack()
    space12.pack()
    button13.pack()
    button14.pack()
    mainloop()
def first_start():
    bg="#000000"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#000000"
    a_button_bg="#000000"
    a_button_fg="#FFFFFF"
    os.system("cd /home/"+username+"/.config/; mkdir projgit ; cd projgit ; mkdir lang theme")
    def llangen():
        os.system("cd /home/"+username+"/.config/projgit/lang/ ; rm * ; touch en.txt")
        messagebox.showinfo("Information","English language applied! When you click 'OK', Projgit settings will open.")
        lwindow.destroy()
        settings()
    def llangtr():
        os.system("cd /home/"+username+"/.config/projgit/lang/ ; rm * ; touch tr.txt")
        messagebox.showinfo("Bilgilendirme","İstenilen dil uygulandı! 'OK' tuşuna bastığınızda Projgit ayarları açılacak.")
        lwindow.destroy()
        settings()
    lwindow=Tk()
    lwindow.title("Choose a language for Projgit")
    lwindow.config(background=bg)
    lwindow.resizable(0, 0)
    text1=Label(lwindow, background=bg, foreground=fg, font="arial 10 bold", text="Please choose a language.\nLütfen bir dil seçin.")
    text1.pack()
    space1=Label(lwindow, background=bg, foreground=fg, font="arial 3", text="\n")
    space1.pack()
    button1=Button(lwindow, text="English (İngilizce)", command=llangen, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg,  font=",arial 10", cursor="hand2", borderwidth="3")
    button1.pack()
    button2=Button(lwindow, text="Türkçe (Turkish)", command=llangtr, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
    button2.pack()
    mainloop()

if not os.path.isdir("/home/"+username+"/.config/projgit/lang/"):
    messagebox.showerror("Warning","Can't found language setting. When you click 'OK' language settings will open. ")
    first_start()
    exit()

bg=""
fg=""
button_bg=""
button_fg=""
a_button_bg=""
a_button_fg=""
if os.path.isfile("/home/"+username+"/.config/projgit/theme/dark.txt"):
    bg="#000000"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#000000"
    a_button_bg="#000000"
    a_button_fg="#FFFFFF"
elif os.path.isfile("/home/"+username+"/.config/projgit/theme/light.txt"):
    bg="#FFFFFF"
    fg="#000000"
    button_bg="#000000"
    button_fg="#FFFFFF"
    a_button_bg="#FFFFFF"
    a_button_fg="#000000"
else:
    if os.path.isfile("/home/"+username+"/.config/projgit/lang/en.txt"):
        messagebox.showwarning("Warning","Can't found theme config. When you click 'OK' Projgit settings will open.")
    elif os.path.isfile("/home/"+username+"/.config/projgit/lang/tr.txt"):
        messagebox.showwarning("Uyarı","Tema yapılandırması bulunamadı, Projgit ayarları 'OK' tuşuna bastığınızda açılacaktır.")
    settings()
    exit()

window=Tk()
window.config(background=bg)
window.resizable(0, 0)
window.title("Projgit")

def about():
    def projgit():
        if os.path.isfile(lang_en):
            if os.getuid() == 0:
                messagebox.showerror("Error","Links cannot be opened while rooted.")
        elif os.path.isfile(lang_tr):
            if os.getuid() == 0:
                messagebox.showerror("Hata","Bağlantılar, kök haklarına sahipken açılamaz.")
        if not os.getuid() == 0:
            os.system("xdg-open https://github.com/MuKonqi/projgit")
    def foss():
        if os.path.isfile(lang_en):
            if os.getuid() == 0:
                messagebox.showerror("Error","Links cannot be opened while rooted.")
        elif os.path.isfile(lang_tr):
            if os.getuid() == 0:
                messagebox.showerror("Hata","Bağlantılar, kök haklarına sahipken açılamaz.")
        if not os.getuid() == 0:
            os.system("xdg-open https://www.gnu.org/philosophy/free-sw.tr.html")
    def developer():
        if os.path.isfile(lang_en):
            if os.getuid() == 0:
                messagebox.showerror("Error","Links cannot be opened while rooted.")
            if not os.getuid() == 0:
                os.system("xdg-open https://github.com/MuKonqi")
        elif os.path.isfile(lang_tr):
            if os.getuid() == 0:
                messagebox.showerror("Hata","Bağlantılar, kök haklarına sahipken açılamaz.")
            if not os.getuid() == 0:
                os.system("xdg-open https://mukonqi.github.io")
    def license():
        if os.path.isfile(lang_en):
            if os.getuid() == 0:
                messagebox.showerror("Error","Links cannot be opened while rooted.")
        elif os.path.isfile(lang_tr):
            if os.getuid() == 0:
                messagebox.showerror("Hata","Bağlantılar, kök haklarına sahipken açılamaz.")
        if not os.getuid() == 0:
            os.system("xdg-open https://www.gnu.org/licenses/gpl-3.0-standalone.html")
    if os.path.isfile(lang_en):
        window=Tk()
        window.title("About | Projgit")
        window.config(background=bg)
        window.resizable(0, 0)
        space1=Label(window, background=bg, foreground=fg, text="\n", font="arial 7") 
        button1=Button(window, font="arial 15 bold italic", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="Projgit\nYet another simple application for Git written using Python3 and Tkinter", command=projgit)
        space2=Label(window, background=bg, foreground=fg, text="\n", font="arial 1")
        button2=Button(window, font="arial 12 bold", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="License: GNU General Public License, Version 3.0 (GPLv3)", command=license)
        button3=Button(window, font="arial 12 bold", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="License type: Free and Open Source Software (FOSS)", command=foss)
        button4=Button(window, font="arial 12 bold", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="Developer: MuKonqi (Muhammed Abdurrahman)", command=developer)
    elif os.path.isfile(lang_tr):
        window=Tk()
        window.title("Hakkında | Projgit")
        window.config(background=bg)
        window.resizable(0, 0)
        space1=Label(window, background=bg, foreground=fg, text="\n", font="arial 7") 
        button1=Button(window, font="arial 15 bold italic", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="Projgit\nPython3 ve Tkinter kullanılarak yazılmış Git için yine bir başka basit uygulama.", command=projgit)
        space2=Label(window, background=bg, foreground=fg, text="\n", font="arial 1")
        button2=Button(window, font="arial 12 bold", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="Lisans: GNU General Public License, Version 3.0 (GPLv3)", command=license)
        button3=Button(window, font="arial 12 bold", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="Lisans türü: Özgür ve Açık Kaynaklı Yazılım (FOSS)", command=foss)
        button4=Button(window, font="arial 12 bold", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="Geliştirici: MuKonqi (Muhammed Abdurrahman)", command=developer)
    space1.pack()
    button1.pack()
    space2.pack()
    button2.pack()
    button3.pack()
    button4.pack()

def publish():
    dir=entry_dir.get()
    files=entry_files.get()
    commit=entry_commit.get()
    url=entry_url.get()
    branch=entry_branch.get()
    print(dir+files+commit+url+branch)
    os.system('cd "'+dir+'" ; git add '+files)
    os.system('cd "'+dir+'" ; git commit -m "'+commit+'"')
    os.system('cd "'+dir+'" ; git remote add origin '+url)
    os.system('cd "'+dir+'" ; git branch -M '+branch)
    os.system('cd "'+dir+'" ; git push -u origin '+branch)
    if os.path.isfile(lang_en):
        messagebox.showinfo("Information","Successful! Changes published at "+url+"!")
    if os.path.isfile(lang_tr):
        messagebox.showinfo("Bilgilendirme","Başarılı! Değişiklikler "+url+" adresinde yayınlandı!")
def publish_new_repo():
    dir=entry_dir.get()
    os.system('cd "'+dir+'" ; git init')
    publish()

if os.path.isfile(lang_en):
    menu1=Menu(window)
    window.config(menu=menu1)
    file=Menu(menu1, tearoff=0)
    menu1.add_cascade(label="File",menu=file)
    file.add_command(label="Quit", command=window.destroy)
    run=Menu(menu1, tearoff=0)
    menu1.add_cascade(label="Run",menu=run)
    run.add_command(label="Settings", command=settings)
    run.add_command(label="About", command=about)
    text1=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="Please enter the requested information.")
    space1=Label(window, background=bg, foreground=fg, font="arial 3", text="\n")
    text2=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="Project folder:")
    entry_dir=Entry()
    text3=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="File(s) to publish: Options: . (meaning all) or filename(s):")
    entry_files=Entry()
    text4=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="Description:")
    entry_commit=Entry()
    text5=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="Repository address:")
    entry_url=Entry()
    text6=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="Branch:")
    entry_branch=Entry()
    space2=Label(window, background=bg, foreground=fg, font="arial 1", text="\n")
    button1=Button(window, text="Publish for a new repository", command=publish_new_repo, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth ="3")
    button2=Button(window, text="Publish to an existing repository", command=publish, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2 ", borderwidth="3")
if os.path.isfile(lang_tr):
    menu1=Menu(window)
    window.config(menu=menu1)
    file=Menu(menu1, tearoff=0)
    menu1.add_cascade(label="Dosya",menu=file)
    file.add_command(label="Çıkış", command=window.destroy)
    run=Menu(menu1, tearoff=0)
    menu1.add_cascade(label="Çalıştır",menu=run)
    run.add_command(label="Ayarlar", command=settings)
    run.add_command(label="Hakkında", command=about)
    text1=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="Lütfen istenilen bilgileri girin.")
    space1=Label(window, background=bg, foreground=fg, font="arial 3", text="\n")
    text2=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="Proje klasörü:")
    entry_dir=Entry()
    text3=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="Yayınlanacak dosya(lar): Seçenekler: . (hepsi anlamına gelmektedir) veya dosya ad(lar)ı:")
    entry_files=Entry()
    text4=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="Açıklama:")
    entry_commit=Entry()
    text5=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="Depo adresi:")
    entry_url=Entry()
    text6=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="Dal:")
    entry_branch=Entry()
    space2=Label(window, background=bg, foreground=fg, font="arial 1", text="\n")
    button1=Button(window, text="Yeni bir depo için yayınla", command=publish_new_repo, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
    button2=Button(window, text="Hali hazırda var olan bir depo için yayınla", command=publish, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
text1.pack()
space1.pack()
text2.pack()
entry_dir.pack()
text3.pack()
entry_files.pack()
text4.pack()
entry_commit.pack()
text5.pack()
entry_url.pack()
text6.pack()
entry_branch.pack()
space2.pack()
button1.pack()
button2.pack()

mainloop()