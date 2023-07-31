from Modules.Cryptography import *
from Modules.Database import *
from Modules.GUI import *
from Modules.Hashing import *
import time


Database.init()

loginGeo = GUI._GUI__login_geometry
regGeo = GUI._GUI__register_geometry

def lgnToReg(event):
    root.geometry(f'{regGeo[0]}x{regGeo[1]}')
    upper_frame.winfo_children()[0].destroy()
    GUI.register(upper_frame,signUpFunction, regToLgn)
 
def regToLgn(event):
    root.geometry(f'{loginGeo[0]}x{loginGeo[1]}')
    upper_frame.winfo_children()[0].destroy()
    GUI.login(upper_frame, signInFunction, lgnToReg)

def signUpFunction(first_name, master_user_name, master_password):
    if not first_name=='' or not master_user_name=='' or not master_password=='' or master_user_name.count(' ')==0: 
        hashed_password = Hashing.creatingHash(master_password)
        Cryptography.generateKey()
        unique_key = Cryptography.getKey()
        Cryptography.destroyKey()
        try:
            Database.userInsertion(first_name, master_user_name, hashed_password, unique_key)
            if len(lower_frame.winfo_children()):
                lower_frame.winfo_children()[0].destroy()
            GUI.successfullMessage(lower_frame, False)
        except:
            if len(lower_frame.winfo_children()):
                lower_frame.winfo_children()[0].destroy()
            GUI.unsuccessfullMessage(lower_frame, False)



def signInFunction(master_user_name, master_password):
    print(master_user_name)
    print(master_password)

root = Tk()
GUI.init()
root.title("Password Manager")
root.config(background='#333333')
root.geometry(f'{loginGeo[0]}x{loginGeo[1]}')

upper_frame = Frame(root,bg='#333333')
lower_frame = Frame(root,bg='#333333')

GUI.login(upper_frame, signInFunction, lgnToReg)

upper_frame.pack()
lower_frame.pack()

root.mainloop()