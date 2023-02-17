from  tkinter  import  *
from  tkinter  import ttk
from  tkinter  import  messagebox
GUI = Tk()
GUI.title
GUI.geometry ('500x300')
L1 = Label(GUI,text ='โครงการประชารัฐ',font=('Angsana New',30 ,),fg='red')
L1.place(x=180 , y=20)
def Button2():
    text = 'ตอนนี้มีเงินอยู่ในบัญชี500'
    messagebox.showinfo('เงินในบัญชี',text)
FB1 = Frame (GUI)    
FB1.place(x=180 , y=  80)
B2 =ttk.Button (FB1 , text = 'เงินมีอยู่กี่บาท',command=Button2) 
B2.pack (ipadx=50 , ipady = 20) #ขนาดปุ่ม
B2.pack(pady = 10)
#################################################
def Button3():
    text = 'เริ่มเรียนพื้นฐานไพทอน 101 ครั้งที่ 2'
    messagebox.showinfo('วันที่เรียน 10 กุมภาพันธ์ 2566' , text)
FB2 = Frame (GUI) # คล้ายกระดาน
FB2.place(x=150 , y=180)
B3 =  ttk.Button (FB1 , text = 'สัปดาห์นี้เรียนวิชาไพทอน',command=Button3) 
B3.pack (ipadx=20,ipady = 20)
B3.pack(pady = 10)


GUI.mainloop ()    