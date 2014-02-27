import sqlite3

DB = None
CONN = None

ADMIN_USER="hackbright"
ADMIN_PASSWORD=5980025637247534551

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("thewall.db")
    DB = CONN.cursor()

def get_user_by_name(username):
    query = """SELECT user_id FROM Users WHERE username = ?"""
    DB.execute(query, (username,))
    user_id = DB.fetchone()
    return user_id

def authenticate(username, password):
    connect_to_db()
    query = """SELECT password FROM Users WHERE username = ?"""
    DB.execute(query, (username,))
    DBpassword = DB.fetchone()



    if DBpassword == None:
        print "no_user" 
        return "no_user"
    elif int(DBpassword[0]) == hash(password):
        return "SUCCESS"
    else:
        print "you suck"
        return "incorrect"



