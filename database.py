import sqlite3

DB_NAME = "users.db"


# ---------------- CREATE TABLE (run once) ----------------
def init_db():# this first to run and it not connected in python but users.db i t s connected
    conn = sqlite3.connect(DB_NAME) 
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)
    c.execute("""
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        content TEXT,
        author TEXT
    )
    """)

    conn.commit()
    conn.close()


# ---------------- GET USER (LOGIN) ----------------
def get_user(username, password):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = c.fetchone()
    conn.close()
    return user


# ---------------- CREATE USER (REGISTER) ----------------
def create_user(username, password):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        (username, password)
    )

    conn.commit()
    conn.close()
def create_post(title,content,author):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute(
        "INSERT INTO posts (title, content,author) VALUES (?, ?,?)",
        (title, content,author)
    )

    conn.commit() # it save data that are created,delete,update 
    conn.close()
def get_posts():
    conn = sqlite3.connect(DB_NAME) #opens connection to the database, conn opens,saves and close database
    c = conn.cursor() # send sql commands helps connect to python

    c.execute("SELECT title, content, author FROM posts ORDER BY id DESC")
    posts = c.fetchall() # post becomes python list give all title,content and author form c.fetchall

    conn.close() # close database 
    return posts
def delete_post(title,author):
    conn = sqlite3.connect(DB_NAME)
    c= conn.cursor()

    c.execute(
        "DELETE FROM posts WHERE title = ? AND author = ?",
        (title, author)
    )
    conn.commit()
    conn.close()
