from Modules.Cryptography import *
from Modules.Database import *
from Modules.GUI import *
from Modules.Hashing import *
from Modules.Regex import *


Database.init()

loginGeo = GUI.login_geometry
regGeo = GUI.register_geometry
frmGeo = GUI.form_geometry

def lgnToReg(event):
    lgnRegWindow.geometry(f'{regGeo[0]}x{regGeo[1]}')
    upper_frame.winfo_children()[0].destroy()
    GUI.register(upper_frame, signUpFunction, regToLgn)

def regToLgn(event):
    lgnRegWindow.geometry(f'{loginGeo[0]}x{loginGeo[1]}')
    upper_frame.winfo_children()[0].destroy()
    GUI.login(upper_frame, signInFunction, lgnToReg)

def signUpFunction(first_name, master_user_name, master_password):

    if Regex.verifyMasterUserName(master_user_name) and Regex.verifyPassword(master_password):
        hashed_password = Hashing.creatingHash(master_password)
        Cryptography.generateKey()
        unique_key = Cryptography.getKey().decode()
        Cryptography.destroyKey()

        try:
            Database.userInsertion(
                first_name, master_user_name, hashed_password, unique_key)
            if len(lower_frame.winfo_children()):
                lower_frame.winfo_children()[0].destroy()
            GUI.successfullMessage(lower_frame, Action.Register)
            lower_frame.after(
                2000, lambda: lower_frame.winfo_children()[0].destroy())
            lower_frame.after(2000, lambda: regToLgn(None))

        except:
            if len(lower_frame.winfo_children()):
                lower_frame.winfo_children()[0].destroy()
            GUI.unsuccessfullMessage(lower_frame, Action.Register)

def signInFunction(master_user_name, master_password):

    try:
        stored_password_hash = Database.getUserHashedPassword(master_user_name)
        if Hashing.verifyingHash(master_password, stored_password_hash):
            if len(lower_frame.winfo_children()):
                lower_frame.winfo_children()[0].destroy()
            global userData
            first_name = Database.getUserFirstName()
            userData.append(master_user_name)
            userData.append(first_name)
            GUI.successfullMessage(lower_frame, Action.LogIn)
            lower_frame.after(1000, lambda: GUI.clearImg())
            lower_frame.after(2000, lambda: lgnRegWindow.destroy())

    except:
        if len(lower_frame.winfo_children()):
            lower_frame.winfo_children()[0].destroy()
        GUI.unsuccessfullMessage(lower_frame, Action.LogIn)

def loginAndRegister():

    global lgnRegWindow
    lgnRegWindow = Tk()
    GUI.lgnRegInit()
    lgnRegWindow.title("Password Manager")
    lgnRegWindow.config(background='#333333')
    lgnRegWindow.geometry(f'{loginGeo[0]}x{loginGeo[1]}')

    global upper_frame, lower_frame
    upper_frame = Frame(lgnRegWindow, bg='#333333')
    lower_frame = Frame(lgnRegWindow, bg='#333333')

    GUI.login(upper_frame, signInFunction, lgnToReg)

    upper_frame.pack()
    lower_frame.pack()

    lgnRegWindow.mainloop()

def formAndList():

    global frmLstWindow
    frmLstWindow = Tk()
    GUI.frmLstInit()
    frmLstWindow.title("Password Manager")
    frmLstWindow.config(background='#333333')
    frmLstWindow.geometry(f'{frmGeo[0]}x{frmGeo[1]}')

    global main_frame
    main_frame = Frame(frmLstWindow, bg='#333333')

    GUI.accountForm()

    main_frame.pack()

    frmLstWindow.mainloop()


loginAndRegister()

formAndList()