from Modules.Cryptography import *
from Modules.Database import *
from Modules.GUI import *
from Modules.Hashing import *
from Modules.Regex import *


Database.init()

loginGeo = GUI._GUI__login_geometry
regGeo = GUI._GUI__register_geometry


def lgnToReg(event):
    lrWindow.geometry(f'{regGeo[0]}x{regGeo[1]}')
    upper_frame.winfo_children()[0].destroy()
    GUI.register(upper_frame, signUpFunction, regToLgn)


def regToLgn(event):
    lrWindow.geometry(f'{loginGeo[0]}x{loginGeo[1]}')
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
            GUI.successfullMessage(lower_frame, False)
            lower_frame.after(
                2000, lambda: lower_frame.winfo_children()[0].destroy())
            lower_frame.after(2000, lambda: regToLgn(None))

        except:
            if len(lower_frame.winfo_children()):
                lower_frame.winfo_children()[0].destroy()
            GUI.unsuccessfullMessage(lower_frame, False)


def signInFunction(master_user_name, master_password):

    try:
        stored_password_hash = Database.getUserHashedPassword(master_user_name)
        if Hashing.verifyingHash(master_password, stored_password_hash):
            if len(lower_frame.winfo_children()):
                lower_frame.winfo_children()[0].destroy()
            GUI.successfullMessage(lower_frame)
            lower_frame.after(2000, lambda: lrWindow.destroy())

    except:
        if len(lower_frame.winfo_children()):
            lower_frame.winfo_children()[0].destroy()
        GUI.unsuccessfullMessage(lower_frame)


def loginRegister():

    global lrWindow
    lrWindow = Tk()
    GUI.lgnRegInit()
    lrWindow.title("Password Manager")
    lrWindow.config(background='#333333')
    lrWindow.geometry(f'{loginGeo[0]}x{loginGeo[1]}')

    global upper_frame, lower_frame
    upper_frame = Frame(lrWindow, bg='#333333')
    lower_frame = Frame(lrWindow, bg='#333333')

    GUI.login(upper_frame, signInFunction, lgnToReg)

    upper_frame.pack()
    lower_frame.pack()

    lrWindow.mainloop()
