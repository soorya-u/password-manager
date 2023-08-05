import os
import sqlite3


class Database:

    # * Function to Establish SQLite Connection
    # * No Parameters
    # * Return Value: Connection
    @classmethod
    def _sqliteConnection(cls):
        conn = sqlite3.connect('.database/database.db')
        return conn

    # * Function to Create userTable
    # * No Parameters
    # * No Return Value
    @classmethod
    def init(cls):
        if not os.path.exists('.database'):
            os.mkdir('.database')
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
    def userInsertion(cls, first_name, master_user_name, hashed_password, unique_key):
        conn = Database._sqliteConnection()
        c = conn.cursor()
        c.execute(f'''
                    insert into userTable values ("{first_name}", "{master_user_name}", "{hashed_password}", "{unique_key}");
                ''')
        conn.commit()

        c.execute(f'''
                    create table {master_user_name} (
                        website varchar(255),
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
    def accountInsertion(cls, master_user_name, platform, url, email, user_name, encrypted_password):
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
    def getUserHashedPassword(cls, master_user_name):
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
    def getUserUniqueKey(cls, master_user_name):
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
    def getUserFirstName(cls, master_user_name):
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
    def getAccountTable(cls, master_user_name):
        conn = Database._sqliteConnection()
        c = conn.cursor()
        data = c.execute(f'''select * from {master_user_name}''').fetchall()
        conn.commit()
        conn.close()
        return data
