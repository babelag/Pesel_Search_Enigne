import sqlite3

def connect():
    conn=sqlite3.connect("pesel_numbers.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS pesel_number(id INTEGER PRIMARY KEY, name TEXT, surname TEXT, year INTEGER, pesel INTEGER)")
    conn.commit()
    conn.close()

def insert(name, surname, year, pesel):
    conn = sqlite3.connect("pesel_numbers.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO pesel_number VALUES (NULL, ?, ?, ?, ?)", (name,surname,year,pesel))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("pesel_numbers.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM pesel_number")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(name="", surname="", year="", pesel=""):
    conn = sqlite3.connect("pesel_numbers.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM pesel_number WHERE name=? OR surname=? OR year=? OR pesel=?", (name, surname, year, pesel))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("pesel_numbers.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM pesel_number WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id, name, surname, year, pesel):
    conn = sqlite3.connect("pesel_numbers.db")
    cur = conn.cursor()
    cur.execute("UPDATE pesel_number SET name=?, surname=?, year=?, pesel=? WHERE id=?", (name, surname, year, pesel, id,))
    conn.commit()
    conn.close()


connect()
#insert("Yomsdx", "Folkdshle", 1993, 93091389999)
#delete(3)
update(4, "Monk", "Sref", 1992, 92012304343)
print(view())
print(search(surname="Folkdshle"))