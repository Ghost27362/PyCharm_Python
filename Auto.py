from tkinter import *
from tkinter.messagebox import *


class LoginWindow(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master1 = master
        self.master1.title('Login')
        self.master1.geometry('400x230+550+250')
        self.master1.resizable(width=False, height=False)
        self.master1['bg'] = 'black'
        self.create_widgets()

    def create_widgets(self):
        self.var = IntVar()

        main_label = Label(self.master1, text='Вход', font='Arial 15 bold', bg='black', fg='white')
        main_label.pack()
        username_label = Label(self.master1, text='Имя пользователя', font='Arial 11 bold', bg='black', fg='white', padx=10, pady=8)
        username_label.pack()

        self.username_entry = Entry(self.master1, bg='black', fg='Lime', font='Arial 12')
        self.username_entry.pack()

        password_label = Label(self.master1, text='Пароль', font='Arial 11 bold', bg='black', fg='white', padx=10,
                               pady=8)
        password_label.pack()

        self.password_entry = Entry(self.master1, bg='black', show='*', fg='Lime', font='Arial 12')
        self.password_entry.pack()

        self.send_btn = Button(self.master1, text='Войти', command=self.login)
        self.send_btn.pack(padx=10, pady=8)

        self.show_btn = Button(self.master1, text='показывать', command=self.show_password)
        self.show_btn.place(relx=0.78, rely=0.55)

        self.send_btn = Button(self.master1, text='Зарегистрироваться', command=self.sign)
        self.send_btn.pack(padx=10, pady=8)

    def login(self):
        text = self.username_entry.get()
        result1 = 'Имя пользователя: ' + text
        self.username_entry['text'] = result1
        print(result1)

        text = self.password_entry.get()
        result2 = 'Пароль: ' + text
        self.password_entry['text'] = result2
        print(result2)

        self.file = open('login_information.txt', 'w')
        self.file.writelines(self.username_entry.get())
        self.file.close()

        self.file = open('password_information.txt', 'w')
        self.file.writelines(self.password_entry.get())
        self.file.close()

        log = self.username_entry.get()
        psw = self.password_entry.get()
        if log == 'Admin' and psw == 'admin' or log == 'admin':
            showinfo('Azpetrol', 'Вход успешно выполнен!  Чтобы продолжить нажмите ОК')
            self.master1.withdraw()
            self.new_window = Toplevel(self.master1)
            self.menu_window = Input_Selection(self.new_window)
        else:
            log = self.username_entry.get()
            psw = self.password_entry.get()
            showerror('ERROR', 'Введено не верное имя или пароль')


    def sign(self):
        cno = self.send_btn
        self.master1.withdraw()
        self.my_window3 = Toplevel(self.master1)
        self.sign_menu = Sign_Menu(self.my_window3)

    def show_password(self):
        if self.password_entry['show'] == '*':
            self.password_entry['show'] = ''
        else:
            self.password_entry['show'] = '*'


class Sign_Menu(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master3 = master
        self.master3.title = ('Sign up')
        self.master3.geometry('400x230+550+250')
        self.master3.resizable(width=False, height=False)
        self.master3['bg'] = 'black'
        self.create_window_widgets()

    def create_window_widgets(self):
        self.var = IntVar

        maie_label = Label(self.master3, text='Регистрация', font='Arial 15 bold', bg='black', fg='white')
        maie_label.pack()
        usernam_label = Label(self.master3, text='Имя пользователя', font='Arial 11 bold', bg='black', fg='white',
                              padx=10, pady=8)
        usernam_label.pack()

        self.usernam_entry = Entry(self.master3, bg='black', fg='Lime', font='Arial 12')
        self.usernam_entry.pack()

        pasword_label = Label(self.master3, text='Пароль', font='Arial 11 bold', bg='black', fg='white', padx=10,
                              pady=8)
        pasword_label.pack()

        self.pasword_entry = Entry(self.master3, bg='black', fg='Lime', font='Arial 12')
        self.pasword_entry.pack()

        self.snd_btn = Button(self.master3, text='Зарегистрироваться', command=self.login_win)
        self.snd_btn.pack(padx=10, pady=8)

        self.pas_btn = Button(self.master3, text='Войти в аккаунт', command=self.return_window)
        self.pas_btn.pack(padx=10, pady=8)

    def login_win(self):
        self.file = open('login_user.txt', 'w')
        self.file.writelines(self.usernam_entry.get())
        self.file.close()

        self.file = open('password_user.txt', 'w')
        self.file.writelines(self.pasword_entry.get())
        self.file.close()

        log = self.usernam_entry.get()
        psw = self.pasword_entry.get()
        if log == '' and psw == '':
            showerror('Registration', 'С пустыми данными зарегистрироваться нельзя')

        else:

            showinfo('Registration', 'Вы успешно были зарегистрированы!')
            self.master3.withdraw()
            self.new_window = Toplevel(self.master3)
            self.menu_window = Input_Selection(self.new_window)

        text = self.usernam_entry.get()
        result1 = 'Имя пользователя: ' + text
        self.usernam_entry['text'] = result1
        print(result1)

        text = self.pasword_entry.get()
        result2 = 'Пароль: ' + text
        self.pasword_entry['text'] = result2
        print(result2)

    def return_window(self):
        self.master3.destroy()
        self.new_log = Toplevel()
        self.log = LoginWindowSelect(self.new_log)

class LoginWindowSelect(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master7 = master
        self.master7.title('Вход')
        self.master7.geometry('400x230+550+250')
        self.master7.resizable(width=False, height=False)
        self.master7['bg'] = 'black'
        self.widgets1()

    def widgets1(self):
        self.var = IntVar()

        main_label = Label(self.master7, text='Вход', font='Arial 15 bold', bg='black', fg='white')
        main_label.pack()
        username_label = Label(self.master7, text='Имя пользователя', font='Arial 11 bold', bg='black', fg='white',
                               padx=10, pady=8)
        username_label.pack()

        self.username_entry = Entry(self.master7, bg='black', fg='Lime', font='Arial 12')
        self.username_entry.pack()

        password_label = Label(self.master7, text='Пароль', font='Arial 11 bold', bg='black', fg='white', padx=10,
                               pady=8)
        password_label.pack()

        self.password_entry = Entry(self.master7, bg='black', show='*', fg='Lime', font='Arial 12')
        self.password_entry.pack()

        self.send_btn = Button(self.master7, text='Войти', command=self.login1)
        self.send_btn.pack(padx=10, pady=8)

        self.show_btn = Button(self.master7, text='показывать', command=self.show_password1)
        self.show_btn.place(relx=0.78, rely=0.55)

        self.send_btn = Button(self.master7, text='Зарегистрироваться', command=self.sign1)
        self.send_btn.pack(padx=10, pady=8)

    def login1(self):
        text = self.username_entry.get()
        result1 = 'Имя пользователя: ' + text
        self.username_entry['text'] = result1
        print(result1)

        text = self.password_entry.get()
        result2 = 'Пароль: ' + text
        self.password_entry['text'] = result2
        print(result2)

        self.file = open('login_information.txt', 'w')
        self.file.writelines(self.username_entry.get())
        self.file.close()

        self.file = open('password_information.txt', 'w')
        self.file.writelines(self.password_entry.get())
        self.file.close()

        log = self.username_entry.get()
        psw = self.password_entry.get()
        showinfo('Azpetrol', 'Вход успешно выполнен!  Чтобы продолжить нажмите ОК')
        self.master7.withdraw()
        self.new_window = Toplevel(self.master7)
        self.menu_window = Input_Selection(self.new_window)


    def sign1(self):
            cno = self.send_btn
            self.master7.withdraw()
            self.my_window3 = Toplevel(self.master7)
            self.sign_menu = Sign_Menu(self.my_window3)

    def show_password1(self):
            if self.password_entry['show'] == '*':
                self.password_entry['show'] = ''
            else:
                self.password_entry['show'] = '*'


class Input_Selection(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master2 = master
        self.master2.title('Выбор входа')
        self.master2.geometry('300x300+600+250')
        self.master2.resizable(width=False, height=False)
        self.master2['bg'] = 'black'
        self.create()

    def create(self):
        self.var = IntVar()

        win_label = Label(self.master2, text='Выбор входа', font='Arial 15 bold', bg='black', fg='white', padx=10,
                          pady=8)
        win_label.pack()

        self.window2_btn = Button(self.master2, text='Режим пользователя', command=self.go_menu)
        self.window2_btn.pack(padx=10, pady=8)

        self.window22_btn = Button(self.master2, text='Режим админа', command=self.get_admin_window)
        self.window22_btn.pack(padx=10, pady=8)

        self.btn_exits = Button(self.master2, text='Сменить аккаунт', command=self.return_window_log)
        self.btn_exits.pack(padx=10, pady=8)

    def get_admin_window(self):
        self.master2.withdraw()
        self.my_window2 = Toplevel(self.master2)
        self.admin_menu = Admin_Menu(self.my_window2)
        showinfo('Azpetrol',
                 'Добро пожаловать в режим админа.\nСдесь вы сможете\nменять полностью всё меню\nа так же настраивать пользователей')

    def return_window_log(self):
        self.master2.destroy()
        self.new_Login = Toplevel()
        self.login = LoginWindowSelect(self.new_Login)

    def go_menu(self):
        self.master2.withdraw()
        self.my_window3 = Toplevel(self.master2)
        self.sign_menu = Menu_User(self.my_window3)
        showinfo('Azpetrol', 'Добро пожаловать!')


class Menu_User(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master4 = master
        self.master4.title('Режим пользователя')
        self.master4.geometry('600x300+450+200')
        self.master4.resizable(width=False, height=False)
        self.create_user()

    def create_user(self):
        self.user_lbl = Label(self.master4, text='Режим пользователя', font='Arial 15 bold', padx=10, pady=8)
        self.user_lbl.pack()
        self.win_label = Label(self.master4, text='Режим пользователя', font='Arial 13 bold', padx=10, pady=8)
        self.rt_lbl = Label(self.master4, text='Разделы')
        self.rt_lbl.place(relx=0.04, rely=0.15)
        self.rl_lbl = Label(self.master4, text='Товары')
        self.rl_lbl.place(relx=0.23, rely=0.15)
        self.ry_lbl = Label(self.master4, text='Ваша корзина')
        self.ry_lbl.place(relx=0.57, rely=0.15)

        self.type_prod = {'Бензин': ['10 литров бензина\n 5$', '15 литров бензина\n10$', '20 литров бензина\n30$',
                                     '30 литров бензина\n50$', '50 литров бензина\n70$', '70 литров бензина\n90$'],
                          'Напитки': ['Кока-кола\n 2$', 'Фанта\n 2$', 'Спрайт\n 2$', 'Пепси\n 2$'],
                          'Моторное масло': ['Mobil ultra\n 10$', 'GT turbo\n 30$', 'X-clean 8100\n 70$',
                                             'Zepro\n 100$']
                          }

        self.box_1 = Listbox(self.master4, selectmode=SINGLE, exportselection=0, height=12)
        self.box_1.place(relx=0.00, rely=0.2)

        for i in list(self.type_prod.keys()):
            self.box_1.insert(END, i)

        self.box_1.bind('<<ListboxSelect>>', self.select_type)

        self.box_2 = Listbox(self.master4, selectmode=EXTENDED, height=12)
        self.box_2.insert(END, '')
        self.box_2.activate(0)
        self.box_2.place(relx=0.20, rely=0.2)

        self.box_2.bind('<<ListboxSelect>>', self.select_prod)

        self.add_btn = Button(self.master4, text='Добавить \n в корзину', width=10, command=self.add_click)
        self.add_btn.place(relx=0.41, rely=0.2)

        self.sel_btn = Button(self.master4, text='Удалить \n с корзины', width=10, command=self.del_click)
        self.sel_btn.place(relx=0.41, rely=0.34)

        self.clr_btn = Button(self.master4, text='Очистить \n корзину', width=10, command=self.clr_click)
        self.clr_btn.place(relx=0.41, rely=0.48)

        self.count_lbl = Label(self.master4, text='Товаров \nв корзине\n0')
        self.count_lbl.place(relx=0.43, rely=0.65)

        self.box_3 = Listbox(self.master4, selectmode=EXTENDED, height=12)
        self.box_3.place(relx=0.54, rely=0.2)

        self.btn = Button(self.master4, text='Купить', font='Arial 10 bold', padx=10, pady=8, command=self.pay_info)
        self.btn.place(relx=0.88, rely=0.87)

        self.settings_user_btn = Button(self.master4, text='Настройки пользователя', padx=10, pady=8,
                                        command=self.settings_get)
        self.settings_user_btn.place(relx=0.73, rely=0.00)

        self.btn_go = Button(self.master4, text='<', font='Arial 10 bold', padx=10, pady=8, command=self.return_window)
        self.btn_go.place(relx=0.00, rely=0.00)

    def pay_method(self):
        cno = self.btn
        self.master4.withdraw()
        self.my_window3 = Toplevel(self.master4)
        self.sign_menu = Menu_User(self.my_window3)
        showinfo('Azpetrol', 'Добро пожаловать!')

    def pay_info(self):
        showinfo('Azpetrol', 'Куплено удачной дороги!')

    def settings_get(self):
        cno = self.settings_user_btn
        self.master4.withdraw()
        self.my_window3 = Toplevel(self.master4)
        self.sign_menu = Settings_Menu(self.my_window3)

    def return_window(self):
        cno = self.btn_go
        self.master4.withdraw()
        self.my_window3 = Toplevel(self.master4)
        self.sign_menu = Input_Selection(self.my_window3)

    def select_type(self, event):
        i = self.box_1.get(self.box_1.curselection())
        self.box_2.delete(0, END)
        for i in self.type_prod[i]:
            self.box_2.insert(END, i)

    def select_prod(self, event):
        a = self.box_2.curselection()

    def add_click(self):
        self.select = list(self.box_2.curselection())
        for i in self.select:
            self.box_3.insert(END, self.box_2.get(i))
        self.count_lbl['text'] = f'Товары\nв Корзине\n{self.box_3.size()}'

    def del_click(self):
        select = list(self.box_3.curselection())
        select.reverse()
        for i in select:
            self.box_3.delete(i)
        self.count_lbl['text'] = f'Товары\nв Корзине\n{self.box_3.size()}'

    def clr_click(self):
        self.box_3.delete(0, END)
        self.count_lbl['text'] = f'Товары\nв Корзине\n{self.box_3.size()}'


class Settings_Menu(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master5 = master
        self.master5.title('Настройки пользователя')
        self.master5.geometry('550x300+450+200')
        self.master5['bg'] = 'black'
        self.master5.resizable(width=False, height=False)
        self.create_settings_wid()

    def return_window_user(self):
        cno = self.btn_exit
        self.master5.withdraw()
        self.my_window5 = Toplevel(self.master5)
        self.sign_menu = Menu_User(self.my_window5)

    def out_account(self):
        showinfo('Azpetrol', 'Вы успешно вышли из аккаунта')
        exit_info = self.btn_exit
        self.master5.withdraw()
        self.my_window4 = Toplevel(self.master5)
        self.widow_out = LoginWindow(self.my_window4)

    def create_settings_wid(self):
        lbl_name = Label(self.master5, text='Настройки пользователя', font='Arial 11 bold', bg='black', fg='white',
                         padx=10, pady=8)
        lbl_name.pack()

        lbl_user_1 = Label(self.master5, text='Имя пользователя:', font='Arial 10 bold', bg='black', fg='white',
                           padx=10,
                           pady=8)

        lbl_user_1.place(relx=0.30, rely=0.2)

        lbl_name_1 = Label(self.master5, text='Никита', font='Arial 10 bold', bg='black', fg='white', padx=10,
                           pady=8)
        lbl_name_1.place(relx=0.55, rely=0.2)

        lbl_surname_1 = Label(self.master5, text='Фамилия:', font='Arial 10 bold', bg='black', fg='white', padx=10,
                              pady=8)
        lbl_surname_1.place(relx=0.30, rely=0.3)

        lbl_surname_2 = Label(self.master5, text='Семёнович', font='Arial 10 bold', bg='black', fg='white',
                              padx=10, pady=8)
        lbl_surname_2.place(relx=0.45, rely=0.3)

        lbl_number_fon = Label(self.master5, text='Номер телефона:', font='Arial 10 bold', bg='black', fg='white',
                               padx=10, pady=8)
        lbl_number_fon.place(relx=0.30, rely=0.4)

        lbl_number = Label(self.master5, text='+7 279-324-321-21', font='Arial 10 bold', bg='black', fg='white',
                           padx=10, pady=8)
        lbl_number.place(relx=0.53, rely=0.4)

        lbl_email = Label(self.master5, text='email: ', font='Arial 10 bold', bg='black', fg='white', padx=10, pady=8)
        lbl_email.place(relx=0.30, rely=0.5)

        lbl_email_user = Label(self.master5, text='nikita.semenovich@gmail.com', font='Arial 10 bold', bg='black',
                               fg='white', padx=10, pady=8)
        lbl_email_user.place(relx=0.40, rely=0.5)

        self.btn_exit = Button(self.master5, text='Выйти из аккаунта', font='Arial 11 bold', bg='black', fg='white',
                               command=self.out_account)
        self.btn_exit.place(relx=0.00, rely=0.9)

        self.btn_exit_menu = Button(self.master5, text='<', font='Arial 12 bold', bg='black', fg='white',
                                    command=self.return_window_user)
        self.btn_exit_menu.place(relx=0.00, rely=0.0)

    def return_window_userd(self):
        out = self.btn_exit
        self.master5.widthdraw()
        self.my_window5 = Toplevel(self.master5)
        self.sign_menu = LoginWindow(self.my_window5)


class Admin_Menu(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master6 = master
        self.master6.title('Режим админа')
        self.master6.geometry('1200x600+200+50')
        self.master6.resizable(width=False, height=False)
        self.create_admin_widgets()

    def create_admin_widgets(self):
        self.lbl_admin = Label(self.master6, text='Режим админа', font='Arial 15 bold', padx=10, pady=8)
        self.lbl_admin.pack()

        self.lbl_benzin = Label(self.master6, text='Вариация бензина', padx=8, pady=8)
        self.lbl_benzin.place(relx=0.00, rely=0.33)

        self.lbl_price = Label(self.master6, text='Цена бензина', padx=8, pady=8)
        self.lbl_price.place(relx=0.00, rely=0.46)

        self.lbl_user = Label(self.master6, text='Пользователи', padx=8, pady=8)
        self.lbl_user.place(relx=0.00, rely=0.59)

        self.it_add = Label(self.master6, text='Еда и напитки', padx=8, pady=8)
        self.it_add.place(relx=0.0, rely=0.70)

        self.password_user_lbl = Label(self.master6, text='Пароль пользователя', padx=8, pady=8)
        self.password_user_lbl.place(relx=0.00, rely=0.90)

        self.price_eda_lbl = Label(self.master6, text='Цена на еду, напитки', padx=8, pady=8)
        self.price_eda_lbl.place(relx=0.00, rely=0.80)

        self.variable_benzin_btn = Label(self.master6, text='Вариация бензина', padx=8, pady=8)
        self.variable_benzin_btn.place(relx=0.20, rely=0.4)

        self.price_benzin_btn = Label(self.master6, text='Цена бензина', padx=8, pady=8)
        self.price_benzin_btn.place(relx=0.30, rely=0.4)

        self.user_btn = Label(self.master6, text='Пользователи', padx=8, pady=8)
        self.user_btn.place(relx=0.80, rely=0.4)

        self.menu_lbl = Label(self.master6, text='Пустое меню', padx=8, pady=8)
        self.menu_lbl.place(relx=0.60, rely=0.4)

        self.user_password_lbl = Label(self.master6, text='Пароль пол.теля', padx=8, pady=8)
        self.user_password_lbl.place(relx=0.90, rely=0.4)

        self.eda_and_napitki = Label(self.master6, text='Еда и напитки', padx=8, pady=8)
        self.eda_and_napitki.place(relx=0.50, rely=0.4)

        self.price_it_lbl = Label(self.master6, text='Цена на еду и напитки', padx=8, pady=8)
        self.price_it_lbl.place(relx=0.39, rely=0.4)

        self.menu_info_lbl = Label(self.master6, text='Стандарт.Меню', padx=8, pady=8)
        self.menu_info_lbl.place(relx=0.71, rely=0.4)

        self.btn_exit_menu = Button(self.master6, text='<', font='Arial 11 bold', padx=10, pady=8, command=self.return_window_menu)
        self.btn_exit_menu.place(relx=0.00, rely=0.0)

        self.lst_window1 = Listbox(self.master6, selectmode=EXTENDED)
        self.lst_window1.place(relx=0.20, rely=0.45)

        self.lst_window2 = Listbox(self.master6, selectmode=EXTENDED)
        self.lst_window2.place(relx=0.30, rely=0.45)

        self.lst_window3 = Listbox(self.master6, selectmode=EXTENDED)
        self.lst_window3.place(relx=0.80, rely=0.45)

        self.lst_window4 = Listbox(self.master6, selectmode=EXTENDED)
        self.lst_window4.place(relx=0.50, rely=0.45)

        self.lst_window5 = Listbox(self.master6, selectmode=EXTENDED)
        self.lst_window5.place(relx=0.40, rely=0.45)

        self.lst_window6 = Listbox(self.master6, selectmode=EXTENDED)
        self.lst_window6.place(relx=0.70, rely=0.45)
        self.lst_window6.insert(1, '15 литров бенз 10$')
        self.lst_window6.insert(2, '20 литров бенз 20$')
        self.lst_window6.insert(3, '30 литров бенз 35$')
        self.lst_window6.insert(4, '40 литров бенз 50$')
        self.lst_window6.insert(5, '60 литров бенз 80$')
        self.lst_window6.insert(6, '80 литров бенз 100$')
        self.lst_window6.insert(7, 'Кока кола 2$')
        self.lst_window6.insert(8, ' Фанта 2$')
        self.lst_window6.insert(9, ' Пепси 2$')
        self.lst_window6.insert(10, ' Спрайт 3$')
        self.lst_window6.insert(11, ' Хот Дог 5$')
        self.lst_window6.insert(12, ' Бургер 7$')

        self.lst_password_user = Listbox(self.master6, selectmode=EXTENDED)
        self.lst_password_user.place(relx=0.90, rely=0.45)

        self.lst_menu = Listbox(self.master6, selectmode=EXTENDED)
        self.lst_menu.place(relx=0.60, rely=0.45)

        self.benzin_entry = Entry(self.master6)
        self.benzin_entry.place(relx=0.00, rely=0.37)

        self.price_entry = Entry(self.master6)
        self.price_entry.place(relx=0.00, rely=0.50)

        self.user_entry = Entry(self.master6)
        self.user_entry.place(relx=0.00, rely=0.63)

        self.eda_and_napitki_ent = Entry(self.master6)
        self.eda_and_napitki_ent.place(relx=0.00, rely=0.75)

        self.price_it_ent = Entry(self.master6)
        self.price_it_ent.place(relx=0.00, rely=0.85)

        self.password_user_ent = Entry(self.master6)
        self.password_user_ent.place(relx=0.00, rely=0.95)

        self.element_add = Button(self.master6, text='Добавить', font='Arial 6 bold', padx=6, pady=6, command=self.add_elements)
        self.element_add.place(relx=0.10, rely=0.36)

        self.it_btn = Button(self.master6, text='Добавить', font='Arial 6 bold', padx=6, pady=6, command=self.add_it_and_beverages)
        self.it_btn.place(relx=0.10, rely=0.74)

        self.price_add = Button(self.master6, text='Добавить', font='Arial 6 bold', padx=6, pady=6, command=self.add_price)
        self.price_add.place(relx=0.10, rely=0.49)

        self.user_add = Button(self.master6, text='Добавить', font='Arial 6 bold', padx=6, pady=6, command=self.add_user)
        self.user_add.place(relx=0.10, rely=0.62)

        self.price_it_btn = Button(self.master6, text='Добавить', font='Arial 6 bold', padx=6, pady=6, command=self.add_it_price)
        self.price_it_btn.place(relx=0.10, rely=0.84)

        self.password_user_btn = Button(self.master6, text='Добавить', font='Arial 6 bold', padx=6, pady=6, command=self.add_password_user)
        self.password_user_btn.place(relx=0.10, rely=0.95)

        self.save_btn = Button(self.master6, text='Сохранить изменения', font='Arial 8 bold', padx=7, pady=7, command=self.save_lists)
        self.save_btn.place(relx=0.37, rely=0.85)

        self.create_menu_btn = Button(self.master6, text='Создать меню', font='Arial 8 bold', padx=7, pady=7, command=self.save_menu)
        self.create_menu_btn.place(relx=0.55, rely=0.85)

        self.get_user = Button(self.master6, text='Перейти в режим пользователя', padx=10, pady=8, command=self.switch_to_user_mode)
        self.get_user.place(relx=0.83, rely=0.00)

        self.window_delete = Button(self.master6, text='           Удалить         ', font='Arial 9 bold', command=self.del_list1)
        self.window_delete.place(relx=0.20, rely=0.72)

        self.window_delete2 = Button(self.master6, text='           Удалить         ', font='Arial 9 bold', command=self.del_list2)
        self.window_delete2.place(relx=0.30, rely=0.72)

        self.window_delete3 = Button(self.master6, text='           Удалить          ', font='Arial 9 bold', command=self.del_list3)
        self.window_delete3.place(relx=0.80, rely=0.72)

        self.window_delete4 = Button(self.master6, text='           Удалить          ', font='Arial 9 bold', command=self.del_list4)
        self.window_delete4.place(relx=0.50, rely=0.72)

        self.window_delete5 = Button(self.master6, text='           Удалить          ', font='Arial 9 bold', command=self.del_list5)
        self.window_delete5.place(relx=0.40, rely=0.72)

        self.window_delete6 = Button(self.master6, text='           Удалить          ', font='Arial 9 bold', command=self.del_element_menu)
        self.window_delete6.place(relx=0.60, rely=0.72)

        self.window_delete7 = Button(self.master6, text='           Удалить          ', font='Arial 9 bold', command=self.del_list6)
        self.window_delete7.place(relx=0.90, rely=0.72)

        self.element_add_menu = Button(self.master6, text='Добавить в меню', font='Arial 8 bold', padx=7, pady=6, command=self.add_elements_menu)
        self.element_add_menu.place(relx=0.20, rely=0.76)

        self.element_price_menu = Button(self.master6, text='Добавить в меню', font='Arial 8 bold', padx=7, pady=6, command=self.add_price_menu)
        self.element_price_menu.place(relx=0.30, rely=0.76)

        self.element_it_menu_add = Button(self.master6, text='Добавить в меню', font='Arial 8 bold', padx=7, pady=6, command=self.add_it_menu)
        self.element_it_menu_add.place(relx=0.50, rely=0.76)

        self.element_price_it_add = Button(self.master6, text='Добавить в меню', font='Arial 8 bold', padx=8, pady=6, command=self.add_it_price_menu)
        self.element_price_it_add.place(relx=0.40, rely=0.76)

    def switch_to_user_mode(self):
        user = self.get_user
        self.master6.withdraw()
        self.user_mode = Toplevel(self.master6)
        self.menu = Menu_User(self.user_mode)

    def return_window_menu(self):
        self.master6.destroy()
        self.new_Login = Toplevel()
        self.window_6 = Input_Selection(self.new_Login)

    def add_elements(self):
        self.lst_window1.insert(END, self.benzin_entry.get())
        self.benzin_entry.delete(0, END)

    def add_price(self):
        number1 = self.price_entry.get()
        number2 = self.price_entry.get()
        number3 = self.price_entry.get()
        number4 = self.price_entry.get()
        number5 = self.price_entry.get()
        number6 = self.price_entry.get()
        number7 = self.price_entry.get()
        number8 = self.price_entry.get()
        number9 = self.price_entry.get()
        number10 = self.price_entry.get()
        number11 = self.price_entry.get()
        number12 = self.price_entry.get()
        number13 = self.price_entry.get()
        number14 = self.price_entry.get()
        number15 = self.price_entry.get()
        number16 = self.price_entry.get()
        number17 = self.price_entry.get()
        number18 = self.price_entry.get()
        number19 = self.price_entry.get()
        number20 = self.price_entry.get()
        if number1 == '1$' or number2 == '2$' or number3 == '3$' or number4 == '4$' or number5 == '5$' or number6 == '6$' or number7 == '7$' or number8 == '8$' or number9 == '9$' or number10 == '10$' or number11 == '11$' or number12 == '12$'or number13 == '13$' or number14 == '14$' or number15 == '15$' or number16 == '16$' or number17 == '17$' or number18 == '18$' or number19 == '19$' or number20 == '20$':
             self.lst_window2.insert(END, self.price_entry.get())
             self.price_entry.delete(0, END)

        else:

            showerror('Azpetrol', 'Если вы ввели цену больше 20 то цена не внесётся максимальная цена у бензина 20$')

    def add_user(self):
        self.lst_window3.insert(END, self.user_entry.get())
        self.user_entry.delete(0, END)

    def add_it_and_beverages(self):
        self.lst_window4.insert(END, self.eda_and_napitki_ent.get())
        self.eda_and_napitki_ent.delete(0, END)

    def add_it_price(self):
        number_1 = self.price_it_ent.get()
        number_2 = self.price_it_ent.get()
        number_3 = self.price_it_ent.get()
        number_4 = self.price_it_ent.get()
        number_5 = self.price_it_ent.get()
        number_6 = self.price_it_ent.get()
        if number_1 == '1$' or number_2 == '2$' or number_3 == '3$' or number_4 == '4$' or number_5 == '5$' or number_6 == '6$':
            self.lst_window5.insert(END, self.price_it_ent.get())
            self.price_it_ent.delete(0, END)
        else:
            showerror('Azpetrol', 'В это поле можно вводить только числа. Если вы ввели число больше 6 то цена не добавится')

    def add_password_user(self):
        self.lst_password_user.insert(END, self.password_user_ent.get())
        self.password_user_ent.delete(0, END)

    def add_elements_menu(self):
        self.select = list(self.lst_window1.curselection())
        for i in self.select:
            self.lst_menu.insert(END, self.lst_window1.get(i))

    def add_price_menu(self):
        self.select = list(self.lst_window2.curselection())
        for i in self.select:
            self.lst_menu.insert(END, self.lst_window2.get(i))

    def add_it_menu(self):
        self.select = list(self.lst_window4.curselection())
        for i in self.select:
            self.lst_menu.insert(END, self.lst_window4.get(i))

    def add_it_price_menu(self):
        self.select = list(self.lst_window5.curselection())
        for i in self.select:
            self.lst_menu.insert(END, self.lst_window5.get(i))

    def del_list1(self):
        self.select = list(self.lst_window1.curselection())
        self.select.reverse()
        for i in self.select:
            self.lst_window1.delete(i)

    def del_list2(self):
        self.select = list(self.lst_window2.curselection())
        self.select.reverse()
        for i in self.select:
            self.lst_window2.delete(i)

    def del_list3(self):
        self.select = list(self.lst_window3.curselection())
        self.select.reverse()
        for i in self.select:
            self.lst_window3.delete(i)

    def del_list4(self):
        self.select = list(self.lst_window4.curselection())
        self.select.reverse()
        for i in self.select:
            self.lst_window4.delete(i)

    def del_list5(self):
        self.select = list(self.lst_window5.curselection())
        self.select.reverse()
        for i in self.select:
            self.lst_window5.delete(i)

    def del_list6(self):
        self.select = list(self.lst_password_user.curselection())
        self.select.reverse()
        for i in self.select:
            self.lst_password_user.delete(i)


    def del_element_menu(self):
        self.select = list(self.lst_menu.curselection())
        self.select.reverse()
        for i in self.select:
            self.lst_menu.delete(i)


    def save_lists(self):
        self.file = open('gasoline_variation.txt', 'w')
        self.file.writelines('\n'.join(self.lst_window1.get(0, END)))
        self.file.close()

        self.file = open('price_gasoline.txt', 'w')
        self.file.writelines('\n'.join(self.lst_window2.get(0, END)))
        self.file.close()

        self.file = open('user_information.txt', 'w')
        self.file.writelines('\n'.join(self.lst_window3.get(0, END)))
        self.file.close()

        self.file = open('it_information.txt', 'w')
        self.file.writelines('\n'.join(self.lst_window4.get(0, END)))
        self.file.close()

        self.file = open('price_it_information.txt', 'w')
        self.file.writelines('\n'.join(self.lst_window5.get(0, END)))
        self.file.close()

        self.file = open('user_now_password.txt', 'w')
        self.file.writelines('\n'.join(self.lst_password_user.get(0, END)))
        self.file.close()
        showinfo('Azpetrol', 'Данные успешно сохранились в ваши файлы')


    def save_menu(self):
        self.file = open('menu_information.txt', 'w')
        self.file.writelines('\n'.join(self.lst_menu.get(0, END)))
        self.file.close()
        print('\nСозданное меню')
        self.my_menu = (f'\nВ меню добавлен - {self.lst_window1.get(0)}'
              f'\nВ меню добавлен - {self.lst_window2.get(0)}'
              f'\nВ меню добавлен - {self.lst_window4.get(0)}'
              f'\nВ меню добавлен - {self.lst_window5.get(0)}')
        print(self.my_menu)

if __name__ == '__main__':
    root = Tk()
    log_window = LoginWindow(root)
    log_window.mainloop()
print('\nВы вышли из автозапрaвки')