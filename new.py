from ast import Delete
from ipaddress import collapse_addresses
from time import strftime
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.tix import COLUMN
from PIL import Image,ImageTk
import random,os
import tempfile
from time import strftime

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+0")
        self.root.title("Billing Software")
        
        
        #Variables
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()
       
        
        #Product Categories List
        self.category=["Select Option","Clothing","LifeStyle","Mobiles"]
        
        #SubCatClothing
        self.SubCatClothing=["Pant","T-Shirt","Shirt"]
        
        self.pant=["Levis","Mufti","Spykar"]
        self.price_levis=5000
        self.price_mufti=7000
        self.price_spykar=8000
        
        self.T_shirt=["Polo","Roadster","Jack&Jones"]
        self.price_polo=1500
        self.price_Roadster=1800
        self.price_JackJones=2100
        
        self.Shirt=["Peter England","Louis Phillipe","Park Avenue"]
        self.price_Peter=2100
        self.price_Louis=2700
        self.price_Park=1800
        
        
        #SubCatLifeStyle
        self.SubCatLifeStyle=["Bath Soap","Face Cream","Hair Oil"]
        
        self.Bath_Soap=["LifeBuoy","lux","Santoor","Pearl"]
        self.price_life=float(20)
        self.price_lux=45
        self.price_santoor=30
        self.price_Pears=35
        
        self.Face_cream=["Fair&Lovely","Ponds","Olay","Garnier"]
        self.price_fair=120
        self.price_Ponds=150
        self.price_Olay=125
        self.price_Garnier=125
        
        self.Hair_Oil=["Parachute","Jasmine","Bajaj"]
        self.price_Para=175
        self.price_Jasmine=125
        self.price_Bajaj=150
        
       
        #SubCatMobiles
        self.SubCatMobiles=["Iphone","Samsung","Xiome","Realme","One+"]
        
        self.Iphone=["Iphone_X","Iphone_11","Iphone_12"]
        self.price_ix=40000
        self.price_i11=60000
        self.price_i12=85000
        
        self.Samsung=["Samsung M16","Samsung M13","Samsung M21"]
        self.price_sm16=11000
        self.price_sm13=16000
        self.price_sm21=15000
        
        self.Xiome=["Red11","Redmi_12","Redmi_Pro"]
        self.price_r11=11000
        self.price_r12=16000
        self.price_rpro=15000
        
        self.Realme=["Realme 12","Realme 13","Realme Pro"]
        self.price_rel12=25000
        self.price_rel13=22000
        self.price_relpro=30000
        
        self.OnePlus=["OnePlus1","OnePlus2","OnePlus3"]
        self.price_one1=45000
        self.price_one2=60000
        self.price_one3=45500
        
        
        
        #Image1
        img=Image.open("Images/1.png")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        lbl_img=Label(self.root,image=self.photoimage)
        lbl_img.place(x=0,y=0,width=500,height=155)
        
        
        #Image2
        img_1=Image.open("Images/2.png")
        img_1=img_1.resize((500,130),Image.ANTIALIAS)
        self.photoimage_1=ImageTk.PhotoImage(img_1)
        lbl_img_1=Label(self.root,image=self.photoimage_1)
        lbl_img_1.place(x=500,y=0,width=500,height=155)
        
        
        #Image3
        img_2=Image.open("Images/3.png")
        img_2=img_2.resize((520,130),Image.ANTIALIAS)
        self.photoimage_2=ImageTk.PhotoImage(img_2)
        lbl_img_2=Label(self.root,image=self.photoimage_2)
        lbl_img_2.place(x=1000,y=0,width=520,height=155)
        
        lbl_title=Label(self.root,text="BILLING SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        lbl_title.place(x=0,y=130,width=1525,height=45)
        
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        
        lbl=Label(lbl_title,font=('times new roman',16,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=(-15),width=120,height=45)
        time()
        
        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=175,width=1530,height=620)
        
        
        #Customer LabelFrame
        Cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("times new roman",15,"bold"),bg="white",fg="red")
        Cust_Frame.place(x=10,y=5,width=350,height=140)
        
        
        self.lbl_mob=Label(Cust_Frame,text="Mobile NO.",font=("times new roman",12,"bold"),bg="white")
        self.lbl_mob.grid(row=0,column=0,stick=W,padx=5,pady=2)
        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phon,font=("times new roman",10,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1)
        
        self.lblCustname=Label(Cust_Frame,text="Customer Name",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblCustname.grid(row=1,column=0,stick=W,padx=5,pady=2)
        self.txtCustName=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=("arial",10,"bold"),width=24)
        self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        
        self.lblEmail=Label(Cust_Frame,text="Email",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblEmail.grid(row=2,column=0,stick=W,padx=5,pady=2)
        self.txtEmail=ttk.Entry(Cust_Frame,textvariable=self.c_email,font=("arial",10,"bold"),width=24)
        self.txtEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        
        
        #Product LabelFrame
        Product_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",12,"bold"),bg="white",fg="red")
        Product_Frame.place(x=370,y=5,width=620,height=140)
        
        
        #Category
        self.lblCategory=Label(Product_Frame,text="Select Categories",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblCategory.grid(row=0,column=0,sticky=W,padx=5,pady=2)        
        
        self.Combo_Category=ttk.Combobox(Product_Frame,value=self.category,font=("arial",10,"bold"),width=24,state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,sticky=W,padx=5,pady=2)        
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)
        
        
        #Sub Category
        self.lblSubCategory=Label(Product_Frame,text="Subcategory",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblSubCategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)        
        
        self.Combo_SubCategory=ttk.Combobox(Product_Frame,value=[""],font=("arial",10,"bold"),width=24,state="readonly")
        self.Combo_SubCategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)        
        self.Combo_SubCategory.bind("<<ComboboxSelected>>",self.Product_add)
        
        #Product Name
        self.lblproduct=Label(Product_Frame,text="Product Name",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblproduct.grid(row=2,column=0,sticky=W,padx=5,pady=2)        
        
        self.Combo_Product=ttk.Combobox(Product_Frame,textvariable=self.product,font=("arial",10,"bold"),width=24,state="readonly")
        self.Combo_Product.grid(row=2,column=1,sticky=W,padx=5,pady=2)        
        self.Combo_Product.bind("<<ComboboxSelected>>",self.Price)
        
        
        #Price
        self.lblPrice=Label(Product_Frame,text="Price",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblPrice.grid(row=0,column=2,sticky=W,padx=5,pady=2)        
        
        self.Combo_Price=ttk.Combobox(Product_Frame,textvariable=self.prices,font=("arial",10,"bold"),width=24,state="readonly")
        self.Combo_Price.grid(row=0,column=3,sticky=W,padx=5,pady=2)        
        
        
        #Qty
        self.lblQty=Label(Product_Frame,text="Qty",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblQty.grid(row=1,column=2,sticky=W,padx=5,pady=2)        
        
        self.ComboQty=ttk.Entry(Product_Frame,textvariable=self.qty,font=("arial",10,"bold"),width=26)
        self.ComboQty.grid(row=1,column=3,sticky=W,padx=5,pady=2)        
             
             
        #Middle Frame
        MiddleFrame=Frame(Main_Frame,bd=10)
        MiddleFrame.place(x=10,y=150,width=980,height=340)
        
        #Image1
        img11=Image.open("Images/11.png")
        img11=img11.resize((490,340),Image.ANTIALIAS)
        self.photoimage11=ImageTk.PhotoImage(img11)
        lbl_img11=Label(MiddleFrame,image=self.photoimage11)
        lbl_img11.place(x=0,y=0,width=490,height=340)
        
        
        #Image2
        img_12=Image.open("Images/15.png")
        img_12=img_12.resize((490,340),Image.ANTIALIAS)
        self.photoimage_12=ImageTk.PhotoImage(img_12)
        lbl_img_12=Label(MiddleFrame,image=self.photoimage_12)
        lbl_img_12.place(x=490,y=0,width=500,height=340)
        
        
        
        #Search
        Search_Frame=Frame(Main_Frame,bd=2,bg="white")
        Search_Frame.place(x=1020,y=15,width=500,height=40)
        
        self.lblBill=Label(Search_Frame,text="Bill Number",font=("arial",12,"bold"),bg="red",fg="white")
        self.lblBill.grid(row=0,column=0,sticky=W,padx=1)        
        
        
        self.txt_Entry_Search=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=("arial",10,"bold"),width=24)
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=2)
        
        self.BtnSearch=Button(Search_Frame,command=self.find_bill,text="Search",font=('arial',10,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnSearch.grid(row=0,column=2)
        
        
        
        #RightFrame Bill Area
        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Area",font=("times new roman",12,"bold"),bg="white",fg="red")
        RightLabelFrame.place(x=1000,y=45,width=480,height=440)
        
        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
        
        
        #Bill Counter LabelFrame
        Bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman",12,"bold"),bg="white",fg="red")
        Bottom_Frame.place(x=0,y=485,width=1520,height=125)
        
        self.lblSubTotal=Label(Bottom_Frame,text="Sub Total",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblSubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)        
        
        self.EntySubTotal=ttk.Entry(Bottom_Frame,textvariable=self.sub_total,font=("arial",10,"bold"),width=24)
        self.EntySubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        
        self.lbl_Tax=Label(Bottom_Frame,text="Gov. Tax",font=("arial",12,"bold"),bg="white",bd=4)
        self.lbl_Tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)        
        
        self.txt_tax=ttk.Entry(Bottom_Frame,textvariable=self.tax_input,font=("arial",10,"bold"),width=24)
        self.txt_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        
        self.lblAmountTotal=Label(Bottom_Frame,text="Total",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblAmountTotal.grid(row=2,column=0,sticky=W,padx=5,pady=2)        
        
        self.txtAmountTotal=ttk.Entry(Bottom_Frame,textvariable=self.total,font=("arial",10,"bold"),width=24)
        self.txtAmountTotal.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        
        
        #Button Frame
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg="white")
        Btn_Frame.place(x=320,y=0)
        
        self.BtnAddToCart=Button(Btn_Frame,command=self.AddItem,height=2,text="Add To Cart",font=('arial',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)
        
        self.BtnGenerate_bill=Button(Btn_Frame,command=self.gen_bill,height=2,text="Generate Bill",font=('arial',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnGenerate_bill.grid(row=0,column=1)
        
        self.BtnSave=Button(Btn_Frame,command=self.save_bill,height=2,text="Save Bill",font=('arial',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnSave.grid(row=0,column=2)
        
        self.BtnPrint=Button(Btn_Frame,command=self.iprint,height=2,text="Print",font=('arial',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnPrint.grid(row=0,column=3)
        
        self.BtnClear=Button(Btn_Frame,command=self.clear,height=2,text="Clear",font=('arial',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnClear.grid(row=0,column=4)
        
        self.BtnExit=Button(Btn_Frame,command=self.root.destroy,height=2,text="Exit",font=('arial',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnExit.grid(row=0,column=5)
        self.welcome()
        
        
        
        
        self.l=[]
     #================Function Declaration==========================
    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t       Welcome To Mohit & Nishant Mini Mall")
        self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()} ")
        self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()} ")
        self.textarea.insert(END,f"\n Phone Number:{self.c_phon.get()}")
        self.textarea.insert(END,f"\n Customer Email:{self.c_email.get()}")
        
        
        self.textarea.insert(END,"\n=============================================")
        self.textarea.insert(END,f"\n Products\t\tQty\t\tPrice")
        self.textarea.insert(END,"\n=============================================\n")
    
        
    def AddItem(self):
        if self.product.get()=="":
            messagebox.showerror("Error","Please Select The Product Name")
        else:
            Tax=1
            self.n=self.prices.get()
            self.m=self.qty.get()*self.n
            self.l.append(self.m)
            self.textarea.insert(END,f"\n{self.product.get()}\t\t{self.qty.get()}\t\t{self.m}")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l))-(self.prices.get()))*Tax)/100)))            
            self.total.set(str("Rs.%.2f"%(((sum(self.l))+((((sum(self.l))-(self.prices.get()))*Tax)/100))))) 
    
    
    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error","Please Add Product To The Cart")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n =============================================")
            self.textarea.insert(END,f"\n Sub Amount: \t\t\t{self.sub_total.get()} ")
            self.textarea.insert(END,f"\n Tax Amount: \t\t\t{self.tax_input.get()} ")
            self.textarea.insert(END,f"\n Total Amount: \t\t\t{self.total.get()} ")
            self.textarea.insert(END,"\n=============================================")
            
        
        
    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do You Want To Save The Bill")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open('bills/'+str(self.bill_no.get())+".txt",'w')
            f1.write(self.bill_data)
            op=messagebox.showinfo("Saved",f"Bill no:{self.bill_no.get()} Saved Successfully")
        
            f1.close()
            
              
    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")
        
        
    def find_bill(self):
        found="no"
        for i in os.listdir("bills/"):
            if i.split(".")[0]==self.search_bill.get():
                f1=open(f'bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="yes"
        if found=='no':
                messagebox.showerror("Error","Invalid Bill No.")
    
    
    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phon.set("")
        self.bill_no.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(x)
        self.c_email.set("")
        self.search_bill.set("")
        self.product.set("")
        self.l=[0]
        self.prices.set("")
        self.qty.set("")
        self.sub_total.set("")
        self.tax_input.set("")
        self.total.set("")
        self.welcome()
        
    
    def Categories(self,event=""):
        
        if self.Combo_Category.get()=="Clothing":
            self.Combo_SubCategory.config(value=self.SubCatClothing)
            self.Combo_SubCategory.current(0)
        
        if self.Combo_Category.get()=="LifeStyle":
            self.Combo_SubCategory.config(value=self.SubCatLifeStyle)
            self.Combo_SubCategory.current(0)
        
        if self.Combo_Category.get()=="Mobiles":
            self.Combo_SubCategory.config(value=self.SubCatMobiles)
            self.Combo_SubCategory.current(0)
            
            
    def Product_add(self,event=""):
        if self.Combo_SubCategory.get()=="Pant":
            self.Combo_Product.config(value=self.pant)
            self.Combo_Product.current(0)
            
        if self.Combo_SubCategory.get()=="T-Shirt":
            self.Combo_Product.config(value=self.T_shirt)
            self.Combo_Product.current(0)
        
        if self.Combo_SubCategory.get()=="Shirt":
            self.Combo_Product.config(value=self.Shirt)
            self.Combo_Product.current(0)
            
            
        #LifeStyle
        if self.Combo_SubCategory.get()=="Bath Soap":
            self.Combo_Product.config(value=self.Bath_Soap)
            self.Combo_Product.current(0)
        
        if self.Combo_SubCategory.get()=="Face Cream":
            self.Combo_Product.config(value=self.Face_cream)
            self.Combo_Product.current(0)
        
        if self.Combo_SubCategory.get()=="Hair Oil":
            self.Combo_Product.config(value=self.Hair_Oil)
            self.Combo_Product.current(0)
        
        #Mobiles
        if self.Combo_SubCategory.get()=="Iphone":
            self.Combo_Product.config(value=self.Iphone)
            self.Combo_Product.current(0)
        
        if self.Combo_SubCategory.get()=="Samsung":
            self.Combo_Product.config(value=self.Samsung)
            self.Combo_Product.current(0)
        
        if self.Combo_SubCategory.get()=="Xiome":
            self.Combo_Product.config(value=self.Xiome)
            self.Combo_Product.current(0)
        
        if self.Combo_SubCategory.get()=="Realme":
            self.Combo_Product.config(value=self.Realme)
            self.Combo_Product.current(0)
       
         
        if self.Combo_SubCategory.get()=="One+":
            self.Combo_Product.config(value=self.OnePlus)
            self.Combo_Product.current(0)
        
        
    def Price(self,event=""):
        if self.Combo_Product.get()=="Levis":
            self.Combo_Price.config(value=self.price_levis)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="Mufti":
            self.Combo_Price.config(value=self.price_mufti)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="Spykar":
            self.Combo_Price.config(value=self.price_spykar)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
            
        #T-Shirt
        if self.Combo_Product.get()=="Polo":
            self.Combo_Price.config(value=self.price_polo)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="Roadster":
            self.Combo_Price.config(value=self.price_Roadster)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="Jack&Jones":
            self.Combo_Price.config(value=self.price_JackJones)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        #Shirt    
        if self.Combo_Product.get()=="Peter England":
            self.Combo_Price.config(value=self.price_Peter)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="Louis Phillipe":
            self.Combo_Price.config(value=self.price_Louis)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="Park Avenue":
            self.Combo_Price.config(value=self.price_Park)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        #Soaps
        if self.Combo_Product.get()=="LifeBuoy":
            self.Combo_Price.config(value=self.price_life)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="lux":
            self.Combo_Price.config(value=self.price_lux)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="Santoor":
            self.Combo_Price.config(value=self.price_santoor)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="Pearl":
            self.Combo_Price.config(value=self.price_Pears)
            self.Combo_Price.current(0)
            self.qty.set(1)
        
        #Cream    
        if self.Combo_Product.get()=="Fair&Lovely":
            self.Combo_Price.config(value=self.price_fair)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="Ponds":
            self.Combo_Price.config(value=self.price_Ponds)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="Olay":
            self.Combo_Price.config(value=self.price_Olay)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="Garnier":
            self.Combo_Price.config(value=self.price_Garnier)
            self.Combo_Price.current(0)
            self.qty.set(1)
        
        #Oil    
        if self.Combo_Product.get()=="Parachute":
            self.Combo_Price.config(value=self.price_Para)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="Jasmine":
            self.Combo_Price.config(value=self.price_Jasmine)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="Bajaj":
            self.Combo_Price.config(value=self.price_Bajaj)
            self.Combo_Price.current(0)
            self.qty.set(1)
          
          #Mobiles  
        if self.Combo_Product.get()=="Iphone_X":
            self.Combo_Price.config(value=self.price_ix)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="Iphone_11":
            self.Combo_Price.config(value=self.price_i11)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="Iphone_12":
            self.Combo_Price.config(value=self.price_i12)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="Samsung M16":
            self.Combo_Price.config(value=self.price_sm16)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="Samsung M13":
            self.Combo_Price.config(value=self.price_sm13)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="Samsung M21":
            self.Combo_Price.config(value=self.price_sm21)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="Red11":
            self.Combo_Price.config(value=self.price_r11)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="Redmi_12":
            self.Combo_Price.config(value=self.price_r12)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="Redmi_Pro":
            self.Combo_Price.config(value=self.price_rpro)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="Realme 12":
            self.Combo_Price.config(value=self.price_rel12)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="Realme 13":
            self.Combo_Price.config(value=self.price_rel13)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="Realme Pro":
            self.Combo_Price.config(value=self.price_relpro)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="OnePlus1":
            self.Combo_Price.config(value=self.price_one1)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="OnePlus3":
            self.Combo_Price.config(value=self.price_one3)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="OnePlus2":
            self.Combo_Price.config(value=self.price_one2)
            self.Combo_Price.current(0)
            self.qty.set(1)
            
        
if __name__=='__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()
    