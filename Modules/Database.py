import os
import sqlite3

class Database:

    app_data = os.getenv('LOCALAPPDATA')

    # * Function to Establish SQLite Connection
    # * No Parameters
    # * Return Value: Connection
    @classmethod
    def _sqliteConnection(cls):
        conn = sqlite3.connect(cls.app_data+r'/zAsh7/Password Manager/.database/database.db')
        return conn

    # * Function to Create userTable
    # * No Parameters
    # * No Return Value
    @classmethod
    def init(cls) -> None:
        if not os.path.exists(cls.app_data+r'/zAsh7'):

            os.mkdir(cls.app_data+r'/zAsh7')
            os.mkdir(cls.app_data+r'/zAsh7'+r'/Password Manager')
            os.mkdir(cls.app_data+r'/zAsh7'+r'/Password Manager'+r'/.database')

            conn = Database._sqliteConnection()
            c = conn.cursor()
            c.execute('''
                        create table userTable (
                            first_name varchar(255),
                            master_user_name varchar(255),
                            hashed_password varchar(255),
                            unique_key varchar(255)
                        );
                ''')
            conn.close()

    # * Function to insert User and create a Account Table
    # * Parameters: First Name, Master Username, Hashed Password, Unique Key
    # * No Return Value
    @classmethod
    def userInsertion(cls, first_name: str, master_user_name: str, hashed_password: str, unique_key: str) -> None:
        conn = Database._sqliteConnection()
        c = conn.cursor()
        c.execute(f'''
                    insert into userTable values ("{first_name}", "{master_user_name}", "{hashed_password}", "{unique_key}");
                ''')
        conn.commit()

        c.execute(f'''
                    create table {master_user_name} (
                        platform varchar(255),
                        url varchar(255),
                        email varchar(255),
                        user_name varchar(255),
                        encryted_password varchar(255)
                    );
            ''')
        conn.close()

    # * Function to insert Account
    # * Parameters: Master Username, Platform, URL, Email, Username, Encrypted Password
    # * No Return Value
    @classmethod
    def accountInsertion(cls, master_user_name: str, platform: str, url: str, email: str, user_name: str, encrypted_password: str) -> None:
        conn = Database._sqliteConnection()
        c = conn.cursor()
        c.execute(f'''
                    insert into {master_user_name} values ("{platform}", "{url}", "{email}", "{user_name}", "{encrypted_password}");
            ''')
        conn.commit()
        conn.close()

    # * Function to get User Passowrd
    # * Parameters: Master Username
    # * Return Value: Hashed Password -> String
    @classmethod
    def getUserHashedPassword(cls, master_user_name: str) -> str:
        conn = Database._sqliteConnection()
        c = conn.cursor()
        data = list(c.execute(
            f'''select hashed_password from userTable where master_user_name="{master_user_name}"''').fetchall()[0])
        conn.commit()
        conn.close()
        return data.pop()
    
    # * Function to get User Key
    # * Parameters: Master Username
    # * Return Value: Unique Key -> String
    @classmethod
    def getUserUniqueKey(cls, master_user_name: str) -> str:
        conn = Database._sqliteConnection()
        c = conn.cursor()
        data = list(c.execute(
            f'''select unique_key from userTable where master_user_name="{master_user_name}"''').fetchall()[0])
        conn.commit()
        conn.close()
        return data.pop()
    
    # * Function to get User First Name
    # * Parameters: Master Username
    # * Return Value: First Name -> String
    @classmethod
    def getUserFirstName(cls, master_user_name: str) -> str:
        conn = Database._sqliteConnection()
        c = conn.cursor()
        data = list(c.execute(
            f'''select first_name from userTable where master_user_name="{master_user_name}"''').fetchall()[0])
        conn.commit()
        conn.close()
        return data.pop()

    # * Function to get Account List
    # * Parameters: Master Username
    # * Return Value: All Account List -> List
    @classmethod
    def getAccountTable(cls, master_user_name: str) ->list[list[str]]:
        conn = Database._sqliteConnection()
        c = conn.cursor()
        data = c.execute(f'''select * from {master_user_name}''').fetchall()
        
        for i in range(len(data)):
            list_cell = list(data[i])
            data.pop(i)
            data.insert(i,list_cell)

        conn.commit()
        conn.close()
        return data