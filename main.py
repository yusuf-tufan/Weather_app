import requests
from tkinter import *
import messagebox


windows=Tk()
windows.title('Weather App')
windows.minsize(1000,600)


def get_data():
    user_city=user_input.get()

    #data of weather
    api_key = '0a4209e367094a64a8495348250507'#special key
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={user_city}&aqi=no'
    get_url = requests.get(url)
    responsew=get_url.json()

    if get_url.status_code==200:
        data_lbl=Label(text=f'Location: {responsew['location']['name']}\n'
                            f'Degree: {responsew['current']['temp_c']}°C\n'
                            f'Degree: {responsew['current']['temp_f']}°F\n'
                            f'Air: {responsew['current']['condition']['text']}')
        data_lbl.config(width=50,bg='light green',fg='black',font=('Arial',15,'italic','bold'))
        data_lbl.place(x=300,y=90)
    else:
        messagebox.showinfo(title='Error',message='Please Can You Chack Your Informations.')

#Label Enter
enter_lbl=Label(text='Enter A City',font=('Arial',10,'bold'))
enter_lbl.place(x=490,y=0)

#enter city
user_input=Entry(width=25,font=('Arial',10,'italic','bold'))
user_input.place(x=450,y=30)

#click button
click_button=Button(text='SEARCH',command=get_data,bg='light blue',fg='red',font=('Arial',10,'italic','bold'))
click_button.place(x=510,y=60)

windows.mainloop()
