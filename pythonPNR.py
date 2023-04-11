import tkinter as tk

from tkinter import ttk
from tkinter import *
import tkinter.font as font
import requests , json
from PIL import ImageTk, Image


win = tk.Tk()
win.title("PNR Stutas Checker")
win.iconbitmap('icon.ico')

win.resizable(width = True, height = True)
win.config(bg='DARKSALMON')
img = Image.open('D:\\Git Projects\\Python PNR\\travelpnr.jpg')

bg = ImageTk.PhotoImage(img)

# win.geometry('1000x1000')
lbl = Label(win , image= bg)
lbl.place(x=0,y=0,relwidth=1, relheight=1)

win.configure(background='green')



heading_font = font.Font(family='Helvetica')
heading_size = font.Font(size=30)


Heading = ttk.Label(win, text = "PNR STATUS CHECKER" ,background= 'yellow'  , borderwidth=2, relief="groove")
Heading['font']= heading_font
Heading['font'] = heading_size
Heading.grid(row=0,columnspan=4,padx = 255)

lEnter_pnr = ttk.Label(win,text='Enter PNR Number',background= 'red',borderwidth=2, relief="groove")
lEnter_pnr['font']= heading_font
lenter_pnr = font.Font(size=20)
lEnter_pnr['font'] = lenter_pnr
lEnter_pnr.grid(row=3,column=1 ,pady=40 ,padx=10)


Enter_pnr = ttk.Entry(win,  font = 50)
Enter_pnr.focus_set()
Enter_pnr.grid(row=3,column=2 ,ipady=6 ,ipadx=30 , padx=0)



def procces():
    
    '''section'''
    url = "https://pnr-status-indian-railway.p.rapidapi.com/pnr-check/4800588940"

    headers = {
	"X-RapidAPI-Key": "f4e0673ea3msh19d52208bf405c2p1bb859jsn92c8e8f885b0",
	"X-RapidAPI-Host": "pnr-status-indian-railway.p.rapidapi.com"
    }

  
    print('responses+')
    '''section'''
    number1=str(Entry.get(Enter_pnr))
    pnr_no = number1
    sxp = tk.StringVar()
    E4 = Entry(win, state='readonly',textvariable = sxp)
    E4.grid(row=5, columnspan=6, ipady=115, ipadx=250, padx=20, pady=10)
    url2 = "https://pnr-status-indian-railway.p.rapidapi.com/pnr-check/" + pnr_no + "/"
    response = requests.request("GET", url2, headers=headers)
    #dk = requests.get(url2)
    result = response.json()
    print(result)

    s = ""
    if result["code"] == 200 :
        pnr_number = number1
        train_no = result['data']['trainInfo']["trainNo"]
        boarding_station = result['data']['boardingInfo']["stationName"]
        train_arrival = result['data']['boardingInfo']["arrivalTime"]
        train_departure = result['data']['boardingInfo']["departureTime"]
        destination_station = result['data']['destinationInfo']["stationName"]
        train_name = result['data']['trainInfo']["name"]
        no_of_seats = result['data']['seatInfo']['noOfSeats']
        passengers_list = result['data']["passengerInfo"]
        for i in passengers_list:
            print(i , 'hh')
        print(passengers_list , 'listings')
        print("'___________________________________________________________________________")
        sxp.set(f"PnrNumber: {pnr_number},\n Train Name :{train_name},\n Train No.: {train_no},\n Boarding Station : {boarding_station},\n Destination Station : {destination_station},\n Train Arrival Time : {train_arrival}, \n Train Departure Time : {train_departure},\n No. of Passengers : {no_of_seats}") 
        s += f"PnrNumber: {pnr_number},\n Train Name :{train_name},\n Train No.: {train_no},\n Boarding Station : {boarding_station},\n Destination Station : {destination_station},\n Train Arrival Time : {train_arrival}, \n Train Departure Time : {train_departure},\n No. of Passengers : {no_of_seats} \n"
        print("_____________________________________________________________________________")
        i = 1
        for passenger in passengers_list:
            
            passenger_coach = passenger["currentCoach"]

            current_no = passenger["currentBerthNo"]
            sxp.set(
                (" passenger number : " + str(i)
                + "\n current status : " + str(passenger_coach)
                + "\n booking_no : " + str(current_no) + "\n")
                    )
            s += f"\n passenger number :  {str(i)}'\n current status :{str(passenger_coach)}'\n booking_no : {str(current_no)}"
            i += 1
            
            
            
            # booking_status = passenger["BookingStatus"]
        
        
        label_1 = ttk.Label(win, text=s,font="Times 14")
        label_1.grid(column=1, row=3)

    else:
        sxp.set("Wrong Pnr Number")

btn = ttk.Button(win, text='Sumbit',command = procces)
btn.grid(row =4 ,columnspan= 5 , ipady = 10 , ipadx=12 , padx = 12)


win.mainloop()
