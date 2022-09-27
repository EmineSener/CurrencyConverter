import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox



class FirstFrame(tk.Frame):
    def __init__(self, root):
        self.root = root
        tk.Frame.__init__(self, root, bg="#F5F5DC", width=480, height=200)
        self.inf()
        self.next_btn()
    def inf(self):
        informatin = """Programa hoş geldiniz.
        Program Yönergesi:
        1.Hangi birimi dönüştürmek istediğinizi seçiniz.
        2.Dönüştürmek istediğiniz miktarı giriniz.
        3.Hangi para birimine dönüştürmek istediğinizi seçiniz.
        İlerlemek veya geri almak için butonları kullanınız."""
        label = Label(self, text=informatin, bg="#d3d3d3")
        label.place(x=240, y=100, anchor="center")


    def next_btn(self):
        self.btn_next1 = tk.Button(self.root, text="Next", command=self.next_frame)
        self.btn_next1.place(x=385, y=210)


    def next_frame(self):
        frm_2 = SecondFrame(self.root)
        frm_2.place(x=0, y=35)
        self.btn_next1.destroy()

class SecondFrame(tk.Frame):
    def __init__(self, root):
        self.root = root
        self.unt1 = 0
        tk.Frame.__init__(self, root, bg="#C8AD90", width=480, height=150)
        self.next_btn()
        self.back_btn()
        self.inf()

        lbl1 = Label(self,
                     text='Türk Lirası',
                     bg="red",
                     font=('Times 14'),
                     width=13, height=3)
        lbl1.place(x=0, y=0)
        lbl2 = Label(self,
                     text='Dolar',
                     bg="#335755",
                     font=('Times 14'),
                     width=13, height=3)
        lbl2.place(x=160, y=0)

        lbl3 = Label(self,
                     text='euro',
                     bg="#858786",
                     font=('Times 14'),
                     width=13, height=3)
        lbl3.place(x=320, y=0)

        self.lbl4=Label(self,
                    bg="#C8AD90",
                    width=60,
                    height=30,
        ).place(x=0,y=69)
        self.selected = tk.IntVar()
        self.btns()


    def chc(self):
        self.unt1=self.selected.get()


    def btns(self):

        btn_tl = ttk.Radiobutton(self.lbl4, text='türk lirası', value=1, variable=self.selected, command = self.chc)
        btn_tl.place(x=40, y=130)

        btn_dlr = ttk.Radiobutton(self.lbl4, text='dolar', value=2, variable=self.selected, command = self.chc)
        btn_dlr.place(x=200, y=130)

        btn_eur = ttk.Radiobutton(self.lbl4, text='euro', value=3, variable=self.selected, command = self.chc)
        btn_eur.place(x=360, y=130)


    def inf(self):
        informatin = " 1.Hangi birimi dönüştürmek istediğinizi seçiniz."
        label = Label(self.root, text=informatin, bg="#d3d3d3", height=2, width=60)
        label.place(x=0, y=0)


    def next_btn(self):
        self.btn_next2 = tk.Button(self.root, text="Next", command=self.next_frame)
        self.btn_next2.place(x=385, y=210)


    def back_btn(self):
        self.btn_back2 = tk.Button(self.root, text="Back", command=self.back_frame)
        self.btn_back2.place(x=75, y=210)


    def next_frame(self):
        frm_3 = ThirdFrame(self.root,self.unt1)
        frm_3.place(x=0, y=35)
        self.btn_next2.destroy()
        self.btn_back2.destroy()

    def back_frame(self):
        frm_1 = FirstFrame(self.root)
        frm_1.place(x=0, y=0)
        self.btn_back2.destroy()
        self.btn_next2.destroy()

class ThirdFrame(tk.Frame):
    def __init__(self, root,unt1):
        self.root = root
        self.unt1=unt1

        tk.Frame.__init__(self, root, bg="#C8AD90", width=480, height=150)
        self.next_btn()
        self.back_btn()


        self.inf()
        self.amount=0
        entry_lbl = ttk.Label(self,text="Dönüştürmek istenilen miktar",font=('Times 14'))
        entry_lbl.place(relx = 0.5,
                   rely = 0.4,
                   anchor = 'center')



        def save_text():
            try:
                self.amount=int(amount_entry.get())
            except ValueError:
                warn="Lütfen dönüştürmek istediğiniz miktarı yalnızca rakam kullanarak giriniz."
                messagebox.showinfo("Uyarı",warn)

        amount_entry = ttk.Entry(self)
        amount_entry.place(relx = 0.5,
                   rely = 0.6,
                   anchor = 'center')
        amount_entry.focus()

        ttk.Button(self, text="Kaydet", width=20, command=save_text).place(relx=0.32,rely=0.7)

    def inf(self):
        informatin = "Dönüştürmek istediğiniz miktarı giriniz.."
        label = Label(self.root, text=informatin, bg="#d3d3d3", height=2, width=60)
        label.place(x=0, y=0)

    def next_btn(self):
        self.btn_next = tk.Button(self.root, text="Next", command=self.next_frame)
        self.btn_next.place(x=385, y=210)

    def back_btn(self):
        self.btn_back = tk.Button(self.root, text="Back", command=self.back_frame)
        self.btn_back.place(x=75, y=210)

    def next_frame(self):
        frm_4 = FourthFrame(self.root,self.unt1,self.amount)
        frm_4.place(x=0, y=35)
        self.btn_next.destroy()
        self.btn_back.destroy()

    def back_frame(self):
        frm_2 = SecondFrame(self.root)
        frm_2.place(x=0, y=35)
        self.btn_back.destroy()
        self.btn_next.destroy()

class FourthFrame(SecondFrame):
    def __init__(self, root,unt1,amount):
        self.root = root
        self.amount=amount
        self.unt2=0

       # print(self.unt1)
        SecondFrame.__init__(self, root)
        self.unt1 = unt1

    def chc(self):
        self.unt2=self.selected.get()

    def inf(self):
        informatin = " Hangi para birimine dönüştürmek istediğinizi seçiniz."
        label = Label(self.root, text=informatin, bg="#d3d3d3", height=2, width=60)
        label.place(x=0, y=0)


    def next_frame(self):
        frm_5 = LatestFrame(self.root,self.unt1,self.amount,self.unt2)
        frm_5.place(x=0, y=0)
        self.btn_back2.destroy()
        self.btn_next2.destroy()

    def back_frame(self):
        frm_3 = ThirdFrame(self.root,self.unt1)
        frm_3.place(x=0, y=35)
        self.btn_back2.destroy()
        self.btn_next2.destroy()

class LatestFrame(tk.Frame):
    def __init__(self,root,unt1,amount,unt2):
        self.root=root
        self.kur=0
        self.unt1=unt1
        self.amount=amount
        self.unt2=unt2
        self.result=0
        self.mylist = list()
        self.mylist.append(self.amount)
        tk.Frame.__init__(self, root, bg="blue", width=480, height=200)

        self.back_btn()
        warn1="Aynı iki birimi seçtiniz."
        warn2="Her iki birimi de seçtiğinize emin olunuz."



        if self.unt1==1:
            if self.unt2==1:
                messagebox.showinfo("Uyarı", warn1)
            elif self.unt2==2:
                self.kur=1/18.44
                self.convert(self.kur)
                self.mylist.append("Türk lirası")
                self.mylist.append("Dolar")

            elif self.unt2==3:
                self.kur=1/17.72
                self.convert(self.kur)
                self.mylist.append("Türk lirası")
                self.mylist.append("Euro")

            else:
                messagebox.showinfo("Uyarı", warn2)

        elif self.unt1==2:
            if self.unt2==2:
                messagebox.showinfo("Uyarı", warn1)
            elif self.unt2==1:
                self.kur=18.44
                self.convert(self.kur)
                self.mylist.append("Dolar")
                self.mylist.append("Türk lirası")

            elif self.unt2==3:
                self.kur=1.04
                self.convert(self.kur)
                self.mylist.append("Dolar")
                self.mylist.append("Euro")

            else:
                messagebox.showinfo("Uyarı", warn2)

        elif self.unt1==3:
            if self.unt2==3:
                messagebox.showinfo("Uyarı", warn1)
            elif self.unt2==1:
                self.kur=17.72
                self.convert(self.kur)
                self.mylist.append("Euro")
                self.mylist.append("Türk Lirası")

            elif self.unt2==2:
                self.kur=1/1.04
                self.convert(self.kur)
                self.mylist.append("Euro")
                self.mylist.append("Dolar")

            else:
                messagebox.showinfo("Uyarı", warn2)

        else:
             messagebox.showinfo("Uyarı", warn2)

        self.inf()

    def convert(self,kur):
        self.result=self.amount*kur
        self.mylist.append(self.result)
    def inf(self):
        try:
            informatin =f'{self.mylist[0]} {self.mylist[2]} , {self.mylist[1]} {self.mylist[3]} olarak hesaplandı.'
            label = Label(self, text=informatin, bg="#d3d3d3",height=6)
            label.place(x=240, y=100, anchor="center")
        except IndexError:
                pass

    def back_btn(self):
        self.btn_back2 = tk.Button(self.root, text="Back", command=self.back_frame)
        self.btn_back2.place(x=75, y=210)


    def back_frame(self):
        frm_4 =FourthFrame(self.root,self.unt1,self.amount)
        frm_4.place(x=0, y=35)
        self.btn_back2.destroy()



class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Currency Converter')
        self.resizable(False, False)
        self.config(background="BLACK")
        window_width = 480
        window_height = 250

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


def main():
    app = App()  # root
    frm_1 = FirstFrame(app)
    frm_1.pack()
    app.mainloop()


if __name__ == "__main__":
    main()
