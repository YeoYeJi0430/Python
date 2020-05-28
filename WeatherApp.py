from urllib.request import urlopen
from threadsafe_tkinter import *

def get_weather(city):
    page = urlopen("https://www.weather.go.kr/weather/observation/currentweather.jsp")
    text = page.read().decode("euckr")
    text = text[text.find(">"+city+"</a>"):] #처음인덱스부터 끝까지 가져옴
    for i in range(5):
        text = text[text.find("<td>")+1:] #td 테이블컬럼하나씩가져옴
    start = 3
    end = text.find("</td>")
    tempV.set(u'온도: '+text[start:end]) # u : 유니코드
    print(text[start:end])

def refresh(*args):
    get_weather(cities.get())

app = Tk()
app.title("현재기온")
app.geometry("200x150+200+200")
Label(app, text="도시: ").pack(side="left")
city_list = ["서울","부산","대구","제주"]
cities = StringVar()
cities.set(city_list[0])
cities.trace("w", refresh)
OptionMenu(app, cities, *city_list).pack(side="right")
tempV = StringVar()
tempV.set("온도: ")
Label(app, textvariable=tempV).pack(pady=40, side="top")
Button(app, text="Refresh", command=refresh).pack(pady=40, side="bottom")
app.mainloop()
#184p