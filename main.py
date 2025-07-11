import requests
from tkinter import *
import messagebox
from PIL import ImageTk, Image

#window
window=Tk()
window.title('Weather App')
window.minsize(1000,700)
window.configure(bg='light blue')
#image
img=Image.open('image_weather.png')
resized=img.resize((1000,700),Image.Resampling.LANCZOS)
itk=ImageTk.PhotoImage(resized)
lbl=Label(window,image=itk)
lbl.image=itk
lbl.pack()

# get data
def get_data():
    user_city=user_input.get()

    #get data of weather from url
    api_key = '0a4209e367094a64a8495348250507'#special key
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={user_city}&aqi=no'
    get_url = requests.get(url)

    responsew=get_url.json()

    #show weather
    if get_url.status_code==200:
        data_lbl=Label(text=f'\nLocation: {responsew['location']['name']}\n'
                            f'Degree(°C): {responsew['current']['temp_c']}°C\n'
                            f'Degree(°F): {responsew['current']['temp_f']}°F\n'
                            f'Air: {responsew['current']['condition']['text']}\n'
                            f'Humidity: {responsew['current']['humidity']}%\n'
                            f'Wind(kph): {responsew['current']['wind_kph']}kph\n'
                            f'Precipitation(mm): {responsew['current']['precip_mm']}%\n'
                       )
        data_lbl.config(width=70,bg='light green',fg='black',font=('Arial',15,'italic','bold'))
        data_lbl.place(x=120,y=100)
    else:
        messagebox.showinfo(title='Error',message='Please Can You Chack Your Informations.\n'
                                                  '-Check characters of word.\n'
                                                  '-Make sure you enter the correct city.'
                            )

#Label Enter
enter_lbl=Label(text='Enter A City',bg='orange',fg='black',font=('Arial',11,'bold'))
enter_lbl.place(x=495,y=5)

#enter city
user_input=Entry(width=25,font=('Arial',10,'italic','bold'))
user_input.place(x=450,y=30)

#click button
click_button=Button(text='SEARCH',command=get_data,bg='light blue',fg='red',font=('Arial',10,'italic','bold'))
click_button.place(x=510,y=60)



window.mainloop()
