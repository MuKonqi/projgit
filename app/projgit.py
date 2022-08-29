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

lang_tr="/home/mukonqi/Projelerim/projgit/-tr-.txt"
lang_en="/home/mukonqi/Projelerim/projgit/-en-.txt"

def settings():
    pass

# if not os.path.isdir("/usr/local/bin/projgit/settings/lang/"):
#     messagebox.showerror("Warning","Can't found language setting. When you click 'OK' and enter your true password, language settings will open. ")
#     settings()
#     exit()

bg=""
fg=""
button_bg=""
button_fg=""
a_button_bg=""
a_button_fg=""
if os.path.isfile("/usr/local/bin/projgit/settings/theme/dark.txt"):
    bg="#000000"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#000000"
    a_button_bg="#000000"
    a_button_fg="#FFFFFF"
elif os.path.isfile("/usr/local/bin/projgit/settings/theme/light.txt"):
    bg="#FFFFFF"
    fg="#000000"
    button_bg="#000000"
    button_fg="#FFFFFF"
    a_button_bg="#FFFFFF"
    a_button_fg="#000000"
else:
    bg="#000000"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#000000"
    a_button_bg="#000000"
    a_button_fg="#FFFFFF"
    # if os.path.isfile("/usr/local/bin/projgit/settings/lang/en.txt"):
    #     messagebox.showwarning("Warning","Can't found theme config. When you click 'OK' projgit settings will open.")
    # elif os.path.isfile("/usr/local/bin/projgit/settings/lang/tr.txt"):
    #     messagebox.showwarning("Uyarı","Tema yapılandırması bulunamadı, projgit ayarları 'OK' tuşuna bastığınızda açılacaktır.")
    # settings()
    # exit()

window=Tk()
window.config(background=bg)
window.resizable(0, 0)
window.title("Projgit")

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
        messagebox.showinfo("Notification","Successful! Changes published at "+url+"!")
    if os.path.isfile(lang_tr):
        messagebox.showinfo("Bilgilendirme","Başarılı! Değişiklikler "+url+" adresinde yayınlandı!")
def publish_new_repo():
    dir=entry_dir.get()
    os.system('cd "'+dir+'" ; git init')
    publish()
if os.path.isfile(lang_en):
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