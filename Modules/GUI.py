from tkinter import *

class GUI:
    
    # * Login Page Screen
    # * Parameters: root
    # * Return Value: Master User Name, Master Password
    @classmethod
    def login(root):
        
        master_user_name = StringVar()
        master_password = StringVar()
        
        def getInfo():
            return [master_user_name,master_password]
        
        f = Frame(root,width=500,height=195,bg='#333333')
        
        Label(
                f,
                text="Login Form",
                font=('Kamerik 105 W00 Bold',24),
                bg='#333333',
                fg='white'
            ).grid(
                    row=0,
                    column=0,
                    columnspan=2,
                    pady=(15,0)
                )

        Label(
                f,
                text = "Username: ",
                font=('JetBrains Mono Medium',12),
                bg='#333333',
                fg='white'
            ).grid(
                    row=1,
                    column=0,
                    pady=(25,5)
                )

        Entry(
                f,
                textvariable=master_user_name,
                font=('JetBrains Mono Medium',12),
                bg='#595959',
                fg='white',
                relief=SOLID,
            ).grid(
                    row=1,
                    column=1,
                    pady=(25,10)
                )

        Label(
                f,
                text = "Password: ",
                font=('JetBrains Mono Medium',12),
                bg='#333333',
                fg='white'
            ).grid(
                    row=2,
                    column=0,
                )

        Entry(
                f,
                textvariable=master_password,
                font=('JetBrains Mono Medium',12),
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
                font=('Kamerik 105 W00 Bold',10),
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
                    pady=(20,0)
                )
        
        f.pack()

    # * Account Not Found in Database Message
    @classmethod
    def accountNotFoundMessage():
        pass

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

    