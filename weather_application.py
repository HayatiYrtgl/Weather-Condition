from tkinter import *
from PIL import Image,ImageTk
import requests
from tkinter import messagebox

url = "https://api.openweathermap.org/data/2.5/weather"

api_key = "9def3fa3dd8ecccbdd99d9a9cbd24fd8"

icon_url = "http://openweathermap.org/img/wn/{}@2x.png"

uygulama = Tk()

uygulama.geometry("350x350+600+190")

uygulama.title("CODE-DEM HAVA DURUMU")

uygulama.config(bg="yellow3")

giris_baslik = Label(uygulama,text="CODE_DEM HAVA\nDURUMU",font="Arial 12",fg="red3", bg="yellow3")

giris_baslik.pack()

"""label"""

sehir_ismi = Label(uygulama,text="Şehir Giriniz :",font="Arial 11 bold", bg="yellow3")

sehir_ismi.pack()

sehir_ismi.place(x=0,y=47)

"""entry"""

sehir_ismi_giris = Entry(justify=CENTER,bg="snow4",font="arial 11 bold",fg="snow")

sehir_ismi_giris.focus()

sehir_ismi_giris.place(x=105,y=50)

"""komut"""

def hava_al(sehir):

    parametreler = {'q':sehir,'appid':api_key,'lang':"tr"}

    data = requests.get(url,params=parametreler).json()

    if data:

        sehir = data['name'].capitalize()

        ulke = data['sys']['country']

        sicaklik = int(data['main']['temp'] - 273.15)

        hissedilen_sicaklik = int(data['main']['feels_like'] - 273.15)

        hava_durumu = data['weather'][0]['description'].capitalize()

        icon = data['weather'][0]['icon']

        return (sehir, ulke, sicaklik, hissedilen_sicaklik, hava_durumu, icon)


"""main fonksiyon"""

def ana_fonksiyon():

    sehir = sehir_ismi_giris.get()

    hava = hava_al(sehir)

    yer_label['text'] = '{},{}'.format(hava[0],hava[1])

    sicaklik_label['text'] = 'Sıcaklık : {}°C,  Hissedilen Sıcaklık : {}°C'.format(hava[2],hava[3])

    durum_label['text'] = 'Hava Durumu : {}'.format(hava[4])

    icon = ImageTk.PhotoImage(Image.open(requests.get(icon_url.format(hava[5]),stream=TRUE).raw))

    icon_label.configure(image=icon)

    icon_label.image = icon


"""buton"""

arama_butonu = Button(uygulama,text="Arama Yap",font="Arial 11",fg="black",bg="skyblue2",padx=135,command=ana_fonksiyon)

arama_butonu.place(x=0,y=90)

"""boş labellar"""

icon_label = Label(uygulama,font="Arial 11 bold", bg="yellow3")

icon_label.pack()

icon_label.place(x=120,y=130)

"""yer label"""

yer_label = Label(uygulama,font="Arial 11 bold", bg="yellow3")

yer_label.place(y=200)

"""sıcaklık lable"""

sicaklik_label = Label(uygulama,font="Arial 11 bold", bg="yellow3")

sicaklik_label.place(y=230)

"""durum label"""

durum_label = Label(uygulama,font="Arial 11 bold", bg="yellow3")

durum_label.place(y=260)

uygulama.mainloop()