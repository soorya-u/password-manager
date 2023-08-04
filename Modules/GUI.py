from tkinter import *
from PIL import Image, ImageTk


class GUI:

    login_geometry = [500, 300]
    register_geometry = [500, 335]
    form_geometry = [650, 400]
    __images = []

    # * Function to Fetch Images for Account Form and Account List
    # * No Parameters
    # * No Return Value
    @classmethod
    def frmLstInit(cls):
        pass

    # * Function to Fetch Images for Login and Register
    # * No Parameters
    # * No Return Value
    @classmethod
    def lgnRegInit(cls):
        import_tick_image = Image.open(r".\Images\tick_image.png")
        import_cross_image = Image.open(r".\Images\cross_image.png")
        resized_tick_image = import_tick_image.resize(
            (40, 40), Image.LANCZOS)
        resized_cross_image = import_cross_image.resize(
            (25, 25), Image.LANCZOS)
        cls.__images.append(ImageTk.PhotoImage(resized_tick_image))
        cls.__images.append(ImageTk.PhotoImage(resized_cross_image))

    # * Login Page Screen
    # * Parameters: root, SignIn Function and Login to Register Function
    # * No Return Value
    @classmethod
    def login(cls, root, signInFunction, lgnToRegShifter):

        master_user_name = StringVar()
        master_password = StringVar()
        f = Frame(root, width=500, height=195, bg='#333333')

        Label(
            f,
            text="Sign In",
            font=('Kamerik 105 W00 Bold', 24),
            bg='#333333',
            fg='#75E6DA'
        ).grid(
            row=0,
            column=0,
            columnspan=2,
            pady=(15, 0)
        )
        Label(
            f,
            text="Username: ",
            font=('JetBrains Mono Medium', 12),
            bg='#333333',
            fg='white'
        ).grid(
            row=1,
            column=0,
            pady=(25, 5)
        )
        Entry(
            f,
            font=('JetBrains Mono Medium', 12),
            bg='#595959',
            fg='white',
            relief=SOLID,
            textvariable=master_user_name
        ).grid(
            row=1,
            column=1,
            pady=(25, 10)
        )
        Label(
            f,
            text="Password: ",
            font=('JetBrains Mono Medium', 12),
            bg='#333333',
            fg='white'
        ).grid(
            row=2,
            column=0,
        )
        Entry(
            f,
            textvariable=master_password,
            font=('JetBrains Mono Medium', 12),
            bg='#595959',
            fg='white',
            relief=SOLID,
        ).grid(
            row=2,
            column=1
        )
        Button(
            f,
            width=7,
            height=1,
            relief=SOLID,
            borderwidth=2,
            command=lambda: signInFunction(
                master_user_name.get(), master_password.get()),
            text="Sign In",
            font=('Kamerik 105 W00 Bold', 10),
            bg='#454545',
            highlightcolor="white",
            highlightbackground="white",
            highlightthickness=4,
            fg='#75E6DA'
        ).grid(
            row=4,
            column=0,
            columnspan=2,
            pady=(20, 0)
        )

        Label(
            f,
            text="Dont Have an Account?",
            font=('JetBrains Mono Medium', 9),
            bg='#333333',
            fg='white'
        ).grid(
            row=5,
            column=0,
            columnspan=2,
            pady=(12, 0)
        )

        l = Label(
            f,
            text="Register",
            font=('Kamerik 105 W00 Bold', 12),
            bg='#333333',
            fg='#75E6DA',
            cursor='hand2'
        )
        l.bind("<Button-1>", lgnToRegShifter)
        l.grid(row=6, column=0, columnspan=2)

        f.pack()

    # * Function to Display Login Successfull
    # * Parameters: root and Login/Registration -> Boolean
    # * No Return Value
    @classmethod
    def successfullMessage(cls, root, loginBoolean=True):

        if (loginBoolean == True):
            action = 'Login'
        else:
            action = 'Registration'

        f = Frame(root, width=500, height=55, bg='#333333')

        Label(
            f,
            image=cls.__images[0],
            bg='#333333'
        ).grid(
            row=0,
            column=0,
            pady=(0, 5)
        )

        Label(
            f,
            text=f"{action} Successfull",
            fg="#59d400",
            bg="#333333",
            font=('Kamerik 105 W00 Bold', 12),
        ).grid(
            row=0,
            column=1,
            pady=(0, 5)
        )

        f.pack(side='bottom', anchor='center', fill='both')

    # * Function to Display Login Unsuccessfull
    # * Parameters: root and Login/Registration -> Boolean
    # * No Return Value
    @classmethod
    def unsuccessfullMessage(cls, root, loginBoolean=True):

        if (loginBoolean == True):
            action = 'Login'
        else:
            action = 'Registration'

        f2 = Frame(root, width=500, height=55, bg='#333333')

        Label(
            f2,
            image=cls.__images[1],
            bg='#333333'
        ).grid(
            row=0,
            column=0,
            pady=(5, 0)
        )
        Label(
            f2,
            text=f"{action} Unsuccessfull",
            fg="#de151f",
            bg="#333333",
            font=('Kamerik 105 W00 Bold', 12),
        ).grid(
            row=0,
            column=1,
            pady=(5, 0)
        )

        f2.pack(side='bottom', anchor='s', fill='both')

    # * Register Page Screen
    # * Parameters: root, SignUp Function and Register to Login Function
    # * No Return Value
    @classmethod
    def register(cls, root, signUpFunction, regToLgnShifter):
        first_name = StringVar()
        master_user_name = StringVar()
        master_password = StringVar()

        f = Frame(root, width=500, height=305, bg='#333333')

        Label(
            f,
            text="Sign Up",
            font=('Kamerik 105 W00 Bold', 24),
            bg='#333333',
            fg='#75E6DA'
        ).grid(row=0,
               column=0,
               columnspan=2,
               pady=(15, 0)
               )

        Label(
            f,
            text="First Name: ",
            font=('JetBrains Mono Medium', 12),
            bg='#333333',
            fg='white'
        ).grid(
            row=1,
            column=0,
            pady=(25, 5)
        )

        Entry(
            f,
            font=('JetBrains Mono Medium', 12),
            bg='#595959',
            fg='white',
            relief=SOLID,
            textvariable=first_name
        ).grid(
            row=1,
            column=1,
            pady=(25, 10)
        )

        Label(
            f,
            text="Username: ",
            font=('JetBrains Mono Medium', 12),
            bg='#333333',
            fg='white'
        ).grid(
            row=2,
            column=0,
            pady=(0, 5)
        )

        Entry(
            f,
            font=('JetBrains Mono Medium', 12),
            bg='#595959',
            fg='white',
            relief=SOLID,
            textvariable=master_user_name
        ).grid(
            row=2,
            column=1,
            pady=(0, 10)
        )

        Label(
            f,
            text="Password: ",
            font=('JetBrains Mono Medium', 12),
            bg='#333333',
            fg='white'
        ).grid(
            row=3,
            column=0,
        )

        Entry(
            f,
            textvariable=master_password,
            font=('JetBrains Mono Medium', 12),
            bg='#595959',
            fg='white',
            relief=SOLID,
        ).grid(
            row=3,
            column=1
        )

        b = Button(
            f,
            width=7,
            height=1,
            relief=SOLID,
            borderwidth=2,
            command=lambda: signUpFunction(
                first_name.get(), master_user_name.get(), master_password.get()),
            text="Sign Up",
            font=('Kamerik 105 W00 Bold', 10),
            bg='#454545',
            highlightcolor="white",
            highlightbackground="white",
            highlightthickness=4,
            fg='#75E6DA'
        ).grid(
            row=4,
            column=0,
            columnspan=2,
            pady=(20, 0)
        )

        Label(
            f,
            text="Already Have an Account?",
            font=('JetBrains Mono Medium', 9),
            bg='#333333',
            fg='white'
        ).grid(
            row=5,
            column=0,
            columnspan=2,
            pady=(12, 0)
        )

        l = Label(
            f,
            text="Login",
            font=('Kamerik 105 W00 Bold', 12),
            bg='#333333',
            fg='#75E6DA',
            cursor='hand2'
        )
        l.bind("<Button-1>", regToLgnShifter)
        l.grid(row=6, column=0, columnspan=2)

        f.pack()

    # * Account Form Screen
    @classmethod
    def accountForm(cls):
        pass

    # * Account Added to Database Message
    @classmethod
    def accountAddedMessage(cls):
        pass

    # * All Accounts List Sub Screen
    @classmethod
    def subWindow(cls):
        pass
