import tkinter as tk

root = tk.Tk()
root.title("Kalkolator")
# root.geometry("480x580")
frame_1 = tk.Frame(root)
frame_1.grid(row=0, column=0)
frame_1.config(background='black')
frame_2 = tk.Frame(root)
frame_2.grid(row=1, column=0)
frame_2.config(background='black')
frame_3 = tk.Frame(root)
frame_3.grid(row=2, column=0)
frame_3.config(background='black')
#poll
pole1 = tk.Text(frame_1, width=60, height=3)
pole2 = tk.Entry(frame_2, width=60)
pole1.grid(row=0, column=0)
pole2.grid(row=1, column=0)
BUT1 = (("", "C","CE","/"), ("7","8","9", "X"),("4","5","6","-"), ("1", "2", "3", "+"), ("-/+", "0", ",", "="))
v = 0
c = 0


def function(ar):
    pole2.insert(10,ar)
    print(ar)


def didi(ar):
    b = tk.Button(frame_3, text=ar, width=15, height=3, command=lambda:function(ar))
    b.grid(row=c, column=v)


for arg in BUT1:
    for ar in BUT1[c]:
        if v == 4:
            v = 0
        didi(ar)
        v += 1
    c += 1


root.mainloop()
