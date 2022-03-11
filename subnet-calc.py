from tkinter import *
from tkinter import ttk
from tkinter import messagebox


window=Tk()
window.title("Subnet Calculator")

####
def calc():
    
    # A Class
    if choice.get() =="1":
        Octel_range.config(text="1 - 126")
        subnet_mask.config(text="255.0.0.0")
        a_bit=int(bit_var.get())
        a_subnet= [1, 2, 4, 8, 16, 32, 64, 128]
        a_int = 16 - a_bit
        min_bit=a_subnet[a_int:]
        out_subnet = sum(min_bit)
        if out_subnet < 256:
            a_bit_1=out_subnet
            a_bit_2=0
            a_bit_3=0
            a_text=f"255.{a_bit_1}.{a_bit_2}.{a_bit_3}"
        if a_bit >= 20:
            a_bit_1=255
            a_bit_2=sum(a_subnet[16-a_bit:])
            a_bit_3=0
            a_text=f"255.{a_bit_1}.{a_bit_2}.{a_bit_3}"
        if a_bit >= 24:
            a_bit_1=255
            a_bit_2=255
            a_bit_3=sum(a_subnet[32-a_bit:])
            a_text=f"255.{a_bit_1}.{a_bit_2}.{a_bit_3}"
        subnet_mask.config(text=a_text)
        subnet_id.config(text="10.0.0.0")
        a_hosts= 32-a_bit
        hosts.config(text=2**a_hosts-2)
        broadcast.config(text="10.255.255.255")
        bit_map.config(text="11111111.00000000.00000000.00000000")
        
    # B Class   
    elif choice.get() =="2":
        Octel_range.config(text="128 - 191")
        subnet_mask.config(text="255.255.0.0")
        b_bit=int(bit_var.get())
        b_subnet= [1, 2, 4, 8, 16, 32, 64, 128]
        b_int = 16 - b_bit
        min_bit=b_subnet[b_int:]
        out_subnet = sum(min_bit)
        if out_subnet <256:
            b_bit_1 = out_subnet
            b_bit_2 = 0
            b_text=f"255.255.{b_bit_1}.{b_bit_2}"
        if out_subnet >254:
            b_bit_1 = 255
            b_bit_2 = sum(b_subnet[32-b_bit:])
            b_text=f"255.255.{b_bit_1}.{b_bit_2}"
        subnet_mask.config(text=b_text)
        b_hosts=32-b_bit
        hosts.config(text=2**b_hosts-2)
        broad_c_t = 2**b_hosts-2+1
        broadcast.config(text="172.16.0.{}".format(broad_c_t))
        host_range.config(text="172.16.0.1 - 172.16.0.{}".format(2**b_hosts-2))
        subnet_id.config(text="172.16.0.0")
        bit_map.config(text="11111111.11111111.00000000.00000000")

    # C Class    
    else:
        Octel_range.config(text="192 - 223")
        c_bit=int(bit_var.get())
        c_subnet= [1, 2, 4, 8, 16, 32, 64, 128]
        c_int = c_bit - 32
        min_bit=c_subnet[abs(c_int):]
        out_subnet = sum(min_bit)
        c_text="255.255.255.%i"%(out_subnet)
        subnet_mask.config(text=c_text)
        hosts.config(text=2**abs(c_int)-2)
        broad_c_t = 2**abs(c_int)-2+1
        broadcast.config(text="192.168.0.{}".format(broad_c_t))
        host_range.config(text="192.168.0.1 - 192.168.0.{}".format(broad_c_t-1))
        subnet_id.config(text="192.168.0.0")
        bit_map.config(text="11111111.11111111.11111111.00000000")
        
####

def about_us():
    messagebox.showinfo("درباره ما", "اين برنامه توسط محمدحسين شفيعي نوشته شده است")
def ver():
    messagebox.showinfo("نسخه فعلي برنامه", "نسخه فعلي 1.0")
    
menu_bar=Menu(window)
#file_menu=Menu(menu_bar, tearoff=0)
help_menu=Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=about_us)
help_menu.add_command(label="Vesion", command=ver)
help_menu.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label="Help", menu=help_menu)

window.config(menu=menu_bar)

####

Frame0=Frame(window)
choice=StringVar()
choice.set("3")
A_class=Radiobutton(Frame0, text="A", variable=choice, value="1").grid(row=1, column=0)
B_class=Radiobutton(Frame0, text="B", variable=choice, value="2").grid(row=1, column=1)
C_class=Radiobutton(Frame0, text="C", variable=choice, value="3").grid(row=1, column=2)
Frame0.grid(row=0, column=0)

Frame1=Frame(window)
Label(Frame1,text="IP Address").grid(row=3, column=0)
ip_address=Entry(Frame1,width=20)
ip_address.grid(row=4, column=0)
Frame1.grid(row=2, column=0)
Label(Frame1, text="Mask Bits").grid(row=3, column=1)

####
bit_var= StringVar()
bit_list = ttk.Combobox(Frame1, width = 30, textvariable = bit_var)
bit_list['values'] = (' 1', ' 2',' 3',  ' 4',
                      ' 5',' 6',' 7',' 8',' 9',' 10',
                      ' 11',' 12',' 13',' 14',' 15',
                      ' 16',' 17',' 18',' 19',' 20',
                      ' 21',' 22',' 23',' 24',' 25',
                      ' 26',' 27',' 28',' 29',' 30',)
                          
bit_list.grid(row=4, column=1)
bit_list.current()
Frame1.grid(row=2, column=0)
####

Button(Frame1, text="Hosts per Subnet",width=20, fg="green", bg="yellow").grid(row=5, column=0)
hosts=Button(Frame1, width=30,text="0", bg="blue", fg="yellow")
hosts.grid(row=5, column=1)

Button(Frame1, text="Subnet Mask",width=20, fg="green", bg="yellow").grid(row=6, column=0)
subnet_mask=Button(Frame1,width=30, text="0.0.0.0", bg="blue", fg="yellow")
subnet_mask.grid(row=6, column=1)

Button(Frame1, text="First Octel Range",width=20, fg="green", bg="yellow").grid(row=7, column=0)
Octel_range=Button(Frame1,width=30, text="192 - 223", bg="blue", fg="yellow")
Octel_range.grid(row=7, column=1)

Button(Frame1, text="Subnet ID", fg="green",width=20, bg="yellow").grid(row=8, column=0)
subnet_id=Button(Frame1,width=30, text="192.168.0.0", bg="blue", fg="yellow")
subnet_id.grid(row=8, column=1)

Button(Frame1, text="Broadcast Address",width=20, fg="green", bg="yellow").grid(row=9, column=0)
broadcast=Button(Frame1, width=30,text="192.168.0.0", bg="blue", fg="yellow")
broadcast.grid(row=9, column=1)

Button(Frame1, text="Host Address Range",width=20, fg="blue", bg="orange").grid(row=10, column=0)
host_range=Button(Frame1,width=30, text="192.168.0.1 - 192.168.0.0", bg="pink")
host_range.grid(row=10, column=1)

Button(Frame1, text="Subnet bitmap",width=20, fg="blue", bg="orange").grid(row=11, column=0)
bit_map=Button(Frame1, text="00000000.00000000.00000000.00000000",width=30, bg="pink")
bit_map.grid(row=11, column=1)

Label(window, text="Click For Calculattor").grid(row=12, column=0)
Button(window, text="click", command=calc, width=19, bg="green", fg="blue").grid(row=13, column=0)

####






window.geometry("400x500")
window.mainloop()
