import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def Song_Counts_by_device(x,y):
    plt.figure()
    plt.bar(x, y)
    plt.title("Total # of Songs listened to from Oct, 2019 - Oct, 2020")
    plt.ylabel("# of songs")
    plt.xlabel("Name of Device")
    plt.show()

def Total_Time_by_device(x,y):
    plt.figure()
    plt.bar(x, y)
    plt.title("Total time listening to music from Oct, 2019 - Oct, 2020")
    plt.ylabel("time in hours")
    plt.xlabel("Name of Device")
    plt.show()

def Change_By__Number_Of_Songs(x,y1,y2,y3):
    plt.figure()
    np.arange(len(x)) 
    plt.bar(x, y1,label="Adams Iphone", color="red") 
    plt.bar(x, y2,label="Annas Iphone", color="Purple")
    plt.bar(x, y3,label="Moms Iphone", color="Green")
   # plt.plot(x, y4, label="Amazon Alexa", color="Black") 
    plt.title("Change in total music played by # of Songs Played")
    plt.xlabel("X Values")
    plt.xticks(x, rotation='30')
    plt.ylabel("Y Values")
    plt.legend()
    plt.show()

def Change_By_Total_Time(x,y,name):
    plt.figure()
    plt.bar(x, y,.5, label=name, color="Black")
    plt.title("Change in total music played by Total Time")
    plt.xticks(x, rotation='30')
    plt.ylabel("Total Hours")
    plt.legend()
    plt.show()

def Genres_by_Device(x,y1,y2,y3,y4):
    plt.figure()
    ind = np.arange(len(x))
    width = .2
    plt.bar(ind, y1, width,  label="Adams Iphone", color="red") 
    plt.bar(ind + width, y2, width, label="Annas Iphone", color="Purple")
    plt.bar(ind - width, y3, width, label="Moms Iphone", color="Green")
    plt.bar(ind -(width*2), y4, width, label="Amazon Alexa", color="Blue") 

    plt.title("Genres Played by Device")
    plt.xticks(ind + width / len(x),x, rotation='20')
    plt.ylabel("Play Duration Hours")
    plt.legend() 
    plt.show()
    
def reason_for_end(x, y1,y2,y3,y4):
    plt.figure() 
    plt.pie(y1, labels=x, autopct="%1.2f%%")
    plt.title("Adams Iphone")
    plt.show()

    plt.figure() 
    plt.pie(y2, labels=x, autopct="%1.2f%%")
    plt.title("Annas Iphone")
    plt.show()

    plt.figure()
    plt.pie(y3, labels=x, autopct="%1.2f%%")
    plt.title("Moms Iphone")
    plt.show()

    plt.figure()
    plt.pie(y4, labels=x, autopct="%1.2f%%")
    plt.title("Amazon Echo")
    plt.show()










