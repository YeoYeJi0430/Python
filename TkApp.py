from tkinter import *

root = Tk()
#Label(tk, text='Hello World').pack()
root.title('Event Test')
root.geometry('640x480+20+20') #크*기+위치

def callback():
    #print('이벤트 발생') 
    exit(0) #클릭시 종료

button = Button(root,text='click',width=20,command=callback)
button.pack(padx=10,pady=10)

root.mainloop()