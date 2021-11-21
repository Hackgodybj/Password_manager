from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk,messagebox

from sha256 import *
import pymysql
from initialize_db import init_db
import os.path
def main():
    init_db()
    root = Tk()

    obj = Signup_system(root)
    root.mainloop()


class Signup_system:
      def __init__(self,root):
          self.check_file=os.path.join(os.path.abspath(os.path.dirname(__file__)),"mysqlcredentials.txt")
          f=open(self.check_file,"r")
          self.output=[i.strip("\n") for i in f.readlines()]
          self.root=root
          self.root.title("Signup system")
          self.root.geometry("1350x700+0+0")
          a=ImageTk.PhotoImage(file="pictures_1/Logo_Password_manager.png")
          self.root.iconphoto(False,a)
          self.bg_pic=ImageTk.Image.open("pictures_1/background2_img.jpg")
          self.resized=self.bg_pic.resize((1350,700),ImageTk.Image.ANTIALIAS)
          self.new_bgpic=ImageTk.PhotoImage(self.resized)

          bg_lbl = Label(self.root, image=self.new_bgpic).pack()
          title=Label(self.root,text="Signup System")

          #====left image====

          self.left_new=ImageTk.PhotoImage( ImageTk.Image.open("pictures_1/side1.png"))
          left=Label(self.root,image=self.left_new).place(x=80,y=100,width=400,height=500)
          #========Security measures===
          self.iv=initialization_vector()
          self.key_salt=key_salt()

          #====Frame=====

          frame1=Frame(self.root,bg="white")

          frame1.place(x=480,y=100,width=700,height=500)
          tilte=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=20,y=40)

          #===profile pic===
          self.web_user = ImageTk.PhotoImage(ImageTk.Image.open("pictures_1/web_user.jpg").resize((100,100),ImageTk.Image.ANTIALIAS))

          dp = Label(frame1, image=self.web_user,bg="white").place(x=550,y=20)

          #username_inFrame
          username=Label(frame1,text="Username",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=20,y=110)
          self.txt_username=Entry(frame1,font=("times new roman",15),bg="lightgray")
          self.txt_username.place(x=120,y=110,width=250)
          #password_input_inFrame
          pass_input=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=20,y=160)
          self.txt_password = Entry(frame1, font=("times new roman", 15), bg="lightgray",show="*")
          self.txt_password.place(x=120, y=160, width=250)
          self.tab_order()

          #confirm password
          pass_confirm=Label(frame1,text="Confirm ",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=20,y=210)
          pass_confirm2 = Label(frame1, text="Password", font=("times new roman", 15, "bold"), bg="white",fg="gray").place(x=20, y=240)
          self.txt_conf_password=Entry(frame1, font=("times new roman", 15), bg="lightgray",show="*")
          self.txt_conf_password.place(x=120, y=220, width=250)

          #country of origin
          c_text_origin=Label(frame1,text="Country of origin",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=20,y=280)
          self.c_origin=ttk.Combobox(frame1,font=("times new roman",13,),state="readonly",justify=CENTER,text="Enter Your Country")
          self.c_origin["values"]=( ('US', 'United States'),
    ('AF', 'Afghanistan'),
    ('AL', 'Albania'),
    ('DZ', 'Algeria'),
    ('AS', 'American Samoa'),
    ('AD', 'Andorra'),
    ('AO', 'Angola'),
    ('AI', 'Anguilla'),
    ('AQ', 'Antarctica'),
    ('AG', 'Antigua And Barbuda'),
    ('AR', 'Argentina'),
    ('AM', 'Armenia'),
    ('AW', 'Aruba'),
    ('AU', 'Australia'),
    ('AT', 'Austria'),
    ('AZ', 'Azerbaijan'),
    ('BS', 'Bahamas'),
    ('BH', 'Bahrain'),
    ('BD', 'Bangladesh'),
    ('BB', 'Barbados'),
    ('BY', 'Belarus'),
    ('BE', 'Belgium'),
    ('BZ', 'Belize'),
    ('BJ', 'Benin'),
    ('BM', 'Bermuda'),
    ('BT', 'Bhutan'),
    ('BO', 'Bolivia'),
    ('BA', 'Bosnia And Herzegowina'),
    ('BW', 'Botswana'),
    ('BV', 'Bouvet Island'),
    ('BR', 'Brazil'),
    ('BN', 'Brunei Darussalam'),
    ('BG', 'Bulgaria'),
    ('BF', 'Burkina Faso'),
    ('BI', 'Burundi'),
    ('KH', 'Cambodia'),
    ('CM', 'Cameroon'),
    ('CA', 'Canada'),
    ('CV', 'Cape Verde'),
    ('KY', 'Cayman Islands'),
    ('CF', 'Central African Rep'),
    ('TD', 'Chad'),
    ('CL', 'Chile'),
    ('CN', 'China'),
    ('CX', 'Christmas Island'),
    ('CC', 'Cocos Islands'),
    ('CO', 'Colombia'),
    ('KM', 'Comoros'),
    ('CG', 'Congo'),
    ('CK', 'Cook Islands'),
    ('CR', 'Costa Rica'),
    ('CI', 'Cote D`ivoire'),
    ('HR', 'Croatia'),
    ('CU', 'Cuba'),
    ('CY', 'Cyprus'),
    ('CZ', 'Czech Republic'),
    ('DK', 'Denmark'),
    ('DJ', 'Djibouti'),
    ('DM', 'Dominica'),
    ('DO', 'Dominican Republic'),
    ('TP', 'East Timor'),
    ('EC', 'Ecuador'),
    ('EG', 'Egypt'),
    ('SV', 'El Salvador'),
    ('GQ', 'Equatorial Guinea'),
    ('ER', 'Eritrea'),
    ('EE', 'Estonia'),
    ('ET', 'Ethiopia'),
    ('FK', 'Falkland Islands (Malvinas)'),
    ('FO', 'Faroe Islands'),
    ('FJ', 'Fiji'),
    ('FI', 'Finland'),
    ('FR', 'France'),
    ('GF', 'French Guiana'),
    ('PF', 'French Polynesia'),
    ('TF', 'French S. Territories'),
    ('GA', 'Gabon'),
    ('GM', 'Gambia'),
    ('GE', 'Georgia'),
    ('DE', 'Germany'),
    ('GH', 'Ghana'),
    ('GI', 'Gibraltar'),
    ('GR', 'Greece'),
    ('GL', 'Greenland'),
    ('GD', 'Grenada'),
    ('GP', 'Guadeloupe'),
    ('GU', 'Guam'),
    ('GT', 'Guatemala'),
    ('GN', 'Guinea'),
    ('GW', 'Guinea-bissau'),
    ('GY', 'Guyana'),
    ('HT', 'Haiti'),
    ('HN', 'Honduras'),
    ('HK', 'Hong Kong'),
    ('HU', 'Hungary'),
    ('IS', 'Iceland'),
    ('IN', 'India'),
    ('ID', 'Indonesia'),
    ('IR', 'Iran'),
    ('IQ', 'Iraq'),
    ('IE', 'Ireland'),
    ('IL', 'Israel'),
    ('IT', 'Italy'),
    ('JM', 'Jamaica'),
    ('JP', 'Japan'),
    ('JO', 'Jordan'),
    ('KZ', 'Kazakhstan'),
    ('KE', 'Kenya'),
    ('KI', 'Kiribati'),
    ('KP', 'Korea (North)'),
    ('KR', 'Korea (South)'),
    ('KW', 'Kuwait'),
    ('KG', 'Kyrgyzstan'),
    ('LA', 'Laos'),
    ('LV', 'Latvia'),
    ('LB', 'Lebanon'),
    ('LS', 'Lesotho'),
    ('LR', 'Liberia'),
    ('LY', 'Libya'),
    ('LI', 'Liechtenstein'),
    ('LT', 'Lithuania'),
    ('LU', 'Luxembourg'),
    ('MO', 'Macau'),
    ('MK', 'Macedonia'),
    ('MG', 'Madagascar'),
    ('MW', 'Malawi'),
    ('MY', 'Malaysia'),
    ('MV', 'Maldives'),
    ('ML', 'Mali'),
    ('MT', 'Malta'),
    ('MH', 'Marshall Islands'),
    ('MQ', 'Martinique'),
    ('MR', 'Mauritania'),
    ('MU', 'Mauritius'),
    ('YT', 'Mayotte'),
    ('MX', 'Mexico'),
    ('FM', 'Micronesia'),
    ('MD', 'Moldova'),
    ('MC', 'Monaco'),
    ('MN', 'Mongolia'),
    ('MS', 'Montserrat'),
    ('MA', 'Morocco'),
    ('MZ', 'Mozambique'),
    ('MM', 'Myanmar'),
    ('NA', 'Namibia'),
    ('NR', 'Nauru'),
    ('NP', 'Nepal'),
    ('NL', 'Netherlands'),
    ('AN', 'Netherlands Antilles'),
    ('NC', 'New Caledonia'),
    ('NZ', 'New Zealand'),
    ('NI', 'Nicaragua'),
    ('NE', 'Niger'),
    ('NG', 'Nigeria'),
    ('NU', 'Niue'),
    ('NF', 'Norfolk Island'),
    ('MP', 'Northern Mariana Islands'),
    ('NO', 'Norway'),
    ('OM', 'Oman'),
    ('PK', 'Pakistan'),
    ('PW', 'Palau'),
    ('PA', 'Panama'),
    ('PG', 'Papua New Guinea'),
    ('PY', 'Paraguay'),
    ('PE', 'Peru'),
    ('PH', 'Philippines'),
    ('PN', 'Pitcairn'),
    ('PL', 'Poland'),
    ('PT', 'Portugal'),
    ('PR', 'Puerto Rico'),
    ('QA', 'Qatar'),
    ('RE', 'Reunion'),
    ('RO', 'Romania'),
    ('RU', 'Russian Federation'),
    ('RW', 'Rwanda'),
    ('KN', 'Saint Kitts And Nevis'),
    ('LC', 'Saint Lucia'),
    ('VC', 'St Vincent/Grenadines'),
    ('WS', 'Samoa'),
    ('SM', 'San Marino'),
    ('ST', 'Sao Tome'),
    ('SA', 'Saudi Arabia'),
    ('SN', 'Senegal'),
    ('SC', 'Seychelles'),
    ('SL', 'Sierra Leone'),
    ('SG', 'Singapore'),
    ('SK', 'Slovakia'),
    ('SI', 'Slovenia'),
    ('SB', 'Solomon Islands'),
    ('SO', 'Somalia'),
    ('ZA', 'South Africa'),
    ('ES', 'Spain'),
    ('LK', 'Sri Lanka'),
    ('SH', 'St. Helena'),
    ('PM', 'St.Pierre'),
    ('SD', 'Sudan'),
    ('SR', 'Suriname'),
    ('SZ', 'Swaziland'),
    ('SE', 'Sweden'),
    ('CH', 'Switzerland'),
    ('SY', 'Syrian Arab Republic'),
    ('TW', 'Taiwan'),
    ('TJ', 'Tajikistan'),
    ('TZ', 'Tanzania'),
    ('TH', 'Thailand'),
    ('TG', 'Togo'),
    ('TK', 'Tokelau'),
    ('TO', 'Tonga'),
    ('TT', 'Trinidad And Tobago'),
    ('TN', 'Tunisia'),
    ('TR', 'Turkey'),
    ('TM', 'Turkmenistan'),
    ('TV', 'Tuvalu'),
    ('UG', 'Uganda'),
    ('UA', 'Ukraine'),
    ('AE', 'United Arab Emirates'),
    ('UK', 'United Kingdom'),
    ('UY', 'Uruguay'),
    ('UZ', 'Uzbekistan'),
    ('VU', 'Vanuatu'),
    ('VA', 'Vatican City State'),
    ('VE', 'Venezuela'),
    ('VN', 'VietNam'),
    ('VG', 'Virgin Islands (British)'),
    ('VI', 'Virgin Islands (U.S.)'),
    ('EH', 'Western Sahara'),
    ('YE', 'Yemen'),
    ('YU', 'Yugoslavia'),
    ('ZR', 'Zaire'),
    ('ZM', 'Zambia'),
    ('ZW', 'Zimbabwe')
)
          self.c_origin.place(x=175, y=280)
          self.c_origin.current(0)
          #===Signup=====
          self.signup_btn= ImageTk.PhotoImage(ImageTk.Image.open("pictures_1/signup.png").resize((100,70),ImageTk.Image.ANTIALIAS))
          my_button=Button(frame1,image=self.signup_btn,borderwidth=0,bg="white",command=self.signup)
          my_button.place(x=60,y=350)

          # ====ExitButton====
          self.exit_btn=ImageTk.PhotoImage(ImageTk.Image.open("pictures_1/2659488-exit-button.jpg").resize((100,70),ImageTk.Image.ANTIALIAS))
          exit_Btn=Button(frame1,image=self.exit_btn,borderwidth=0,bg="white",command=self.exit_function)
          exit_Btn.place(x=550,y=355)
          #======toggle====
          self.check_var=IntVar()
          self.check_var_2=IntVar()
          btn_toggle = Checkbutton(frame1, text="show", bg="white", fg="blue", font=("times new roman", 12),
                                   borderwidth=0, command=self.show_psd_hide, variable=self.check_var, onvalue=1,
                                   offvalue=0).place(x=380, y=160)
          btn_toggle_confirm=Checkbutton(frame1, text="show", bg="white", fg="blue", font=("times new roman", 12),
                                   borderwidth=0, command=self.show_psd_hide_2, variable=self.check_var_2, onvalue=1,
                                   offvalue=0).place(x=380, y=220)
          #====Sign in===
          self.signin_btn=ImageTk.PhotoImage(ImageTk.Image.open("pictures_1/signin_2.jpg").resize((120,105),ImageTk.Image.ANTIALIAS))
          my_button_2=Button(frame1,image=self.signin_btn,borderwidth=0,bg="white",command=self.sign_in)
          my_button_2.place(x=180, y=338)

      def exit_function(self):
          MsgBox = messagebox.askquestion('Exit Application', 'Are you sure you want to Exit the application',
                                          icon='warning', parent=self.root)
          if MsgBox == 'yes':
              self.root.destroy()
          else:
              pass

      def tab_order(self):
          self.txt_username.focus()
          widget = [self.txt_username, self.txt_password]
          for i in widget:
              i.lift()
      def sign_in(self):
          self.a=Toplevel(self.root)
          from login2_system import Login_system
          self.login=Login_system(self.a)






      def show_psd_hide_2(self):
          if (self.check_var_2.get()):

              self.txt_conf_password.config(show="")
          else:

              self.txt_conf_password.config(show="*")
      def show_psd_hide(self):
          if (self.check_var.get()):

              self.txt_password.config(show="")
          else:

              self.txt_password.config(show="*")





      def clear(self):
          self.txt_username.delete(0,END)
          self.txt_password.delete(0, END)
          self.c_origin.current(0)
          self.txt_conf_password.delete(0,END)
      def signup(self):
          if self.txt_username.get()=="" or self.txt_password.get()=="" or self.txt_conf_password=="" or self.c_origin=="":
              messagebox.showerror("Error","All boxes are required to fulfill! ",parent=self.root)
          elif self.txt_password.get()!=self.txt_conf_password.get():
              messagebox.showerror("Error","password and confirm password should be same!",parent=self.root)
          else:
              try:
                  con=pymysql.connect(host=self.output[0],port=int(self.output[1]),user=self.output[2],password=self.output[3],database="password_database" )
                  cur=con.cursor()
                  con_2=pymysql.connect(host=self.output[0],port=int(self.output[1]),user=self.output[2],password=self.output[3],database="password_database")
                  cur_2=con_2.cursor()
                  cur.execute("select * from user where Username=%s",self.txt_username.get())
                  row=cur.fetchone()

                  if row!=None:
                      messagebox.showerror("Error","Username already in use.Please try with another Username",parent=self.root)
                  else:
                      salt=generate_salt()
                      salt_decoded=salt.decode("utf-8")



                      cur.execute("insert into user (Username,Password,Country_of_origin,salt,iv,key_salt) values(%s,%s,%s,%s,%s,%s)",
                                  (self.txt_username.get(),
                                   sha256_algo(self.txt_password.get(),salt),
                                   self.c_origin.get(),salt_decoded,str(self.iv),self.key_salt.decode("latin1")))

                      con.commit()
                      cur_2.execute(
                          "create table {} (Title varchar(50),Username varchar(60),URL varchar(50),Password varchar(60),Email_ID varchar(50),U_ID varchar(50) PRIMARY KEY,Time_of_Entry timestamp DEFAULT current_timestamp())".format(
                              "user_" + str(id_required(self.txt_username.get(),self.output))))
                      con.close()
                      con_2.commit()

                      messagebox.showinfo("Congrats","Successfully signed up!")

                      self.clear()

                  con_2.close()

              except Exception as es:
                  messagebox.showerror("Error", f"Error due to: {str(es)}",parent=self.root)



if __name__ == '__main__':
    main()
