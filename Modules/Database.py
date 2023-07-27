import os
import sqlite3

class Database:

    @classmethod
    def sqliteConnection(cls):
        conn = sqlite3.connect('.database/database.db')
        return conn
    
    @classmethod
    def init(cls):
        if not os.path.exists('.database'):
            os.mkdir('.database')
            conn = Database.sqliteConnection()
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

    @classmethod
    def userInsertion(cls,first_name,master_user_name,hashed_password,unique_key):
        conn = Database.sqliteConnection()
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
    
    @classmethod
    def accountInsertion(cls,master_user_name,platform,url,email,user_name,encrypted_password):
        conn = Database.sqliteConnection()
        c = conn.cursor()
        c.execute(f'''
                    insert into {master_user_name} values ("{platform}", "{url}", "{email}", "{user_name}", "{encrypted_password}");
            ''')
        conn.commit()
        conn.close()
