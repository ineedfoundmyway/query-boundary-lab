import json
import sqlite3

def database():
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE accounts (username TEXT, password TEXT)")
    db.execute("INSERT INTO accounts VALUES (?, ?)", ("student", "lab-secret"))
    return db

def authenticate(db, username, password, secure=True):
    if secure:
        return db.execute("SELECT username FROM accounts WHERE username=? AND password=?", (username, password)).fetchone() is not None
    query = f"SELECT username FROM accounts WHERE username='{username}' AND password='{password}'"
    return db.execute(query).fetchone() is not None

def experiment():
    with database() as db:
        payload = "' OR 1=1 -- "
        return {"fixture": "in-memory SQLite only", "normal_login": authenticate(db, "student", "lab-secret"), "wrong_password": authenticate(db, "student", "wrong"), "vulnerable_bypass": authenticate(db, payload, "wrong", False), "parameterized_bypass": authenticate(db, payload, "wrong", True), "mitigation": "Bind values separately from SQL syntax"}

if __name__ == "__main__":
    print(json.dumps(experiment(), indent=2))
