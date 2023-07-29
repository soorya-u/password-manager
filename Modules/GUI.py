from tkinter import *
from PIL import Image, ImageTk


class GUI:

    __login_geometry="500x250"
    __images = None

    # * Function to Fetch Images
    # * No Parameters
    # * No Return Value
    @classmethod
    def init(cls):
        import_tick_image = Image.open(r"..\Images\tick_image.png")
        import_cross_image = Image.open(r"..\Images\cross_image.png")
        resized_tick_image = import_tick_image.resize(
            (40, 40), Image.LANCZOS)
        resized_cross_image = import_cross_image.resize(
            (25, 25), Image.LANCZOS)
        cls.__images.append(ImageTk.PhotoImage(resized_tick_image))
        cls.__images.append(ImageTk.PhotoImage(resized_cross_image))

    # * Login Page Screen
    # * Parameters: root
    # * Return Value: Master User Name, Master Password
    @classmethod
    def login(cls, root):

        master_user_name = StringVar()
        master_password = StringVar()

        def getInfo():
            return [master_user_name, master_password]

        f = Frame(root, width=500, height=195, bg='#333333')

        Label(
            f,
            text="Login Form",
            font=('Kamerik 105 W00 Bold', 24),
            bg='#333333',
            fg='white'
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
            textvariable=master_user_name,
            font=('JetBrains Mono Medium', 12),
            bg='#595959',
            fg='white',
            relief=SOLID,
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
            text="Login",
            font=('Kamerik 105 W00 Bold', 10),
            command=getInfo,
            bg='#454545',
            highlightcolor="white",
            highlightbackground="white",
            highlightthickness=4,
            fg='white'
        ).grid(
            row=3,
            column=0,
            columnspan=2,
            pady=(20, 0)
        )

        f.pack()

    # * Function to Display Login Successfull
    # * Parameters: root and Login/Registration -> String
    # * No Return Value
    @classmethod
    def successfullMessage(cls, root, action):

        f = Frame(root, width=500, height=55, bg='#333333')

        Label(
            f,
            image=cls.__images[0],
            bg='#333333'
        ).grid(
            row=0,
            column=0,
            padx=(145, 0),
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
    # * Parameters: root
    # * No Return Value
    @classmethod
    def unsuccessfullMessage(cls, root, action):

        f2 = Frame(root, width=500, height=55, bg='#333333')

        Label(
            f2,
            image=cls.__images[1],
            bg='#333333'
        ).grid(
            row=0,
            column=0,
            padx=(151, 10),
            pady=(0, 5)
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
            pady=(0, 5)
        )

        f2.pack(side='bottom', anchor='center', fill='both')

    # * Register Page Screen
    @classmethod
    def register():
        pass

    # * Register Page Screen
    @classmethod
    def accountForm():
        pass

    # * Account Added to Database Message
    @classmethod
    def accountAddedMessage():
        pass

    # * All Accounts List Sub Screen
    @classmethod
    def subWindow():
        pass
