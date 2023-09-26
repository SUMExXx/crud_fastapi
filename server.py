from fastapi import FastAPI
import psycopg2
from fastapi.middleware.cors import CORSMiddleware
import json

conn = psycopg2.connect(dbname="verceldb",host="ep-tight-math-26832109-pooler.us-east-1.postgres.vercel-storage.com", port="5432", user="default", password="rwRX5KiB4MDk")

print("Database connected successfully")

cur = conn.cursor()

app = FastAPI()

origins = [
    "https://crud-fastapi.onrender.com",
    "https://todofastapi.netlify.app",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "http://localhost:5173",
    "http://localhost:5000",
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/todos")

def refresh():

    cur.execute("SELECT * FROM todo")
    res = cur.fetchall()

    dict = {}

    for i in res:
        dict[i[0]] = i[1]

    return json.dumps(dict)


@app.post("/add/{desc}")

def addTodo(desc):
    
    cur.execute("INSERT INTO todo (Description) VALUES(%s)", (desc,))

    return {'status': 'success'}


@app.delete("/delete/{id}")

def deleteTodo(id):
    cur.execute("DELETE FROM todo WHERE Todo_id = %s", (id,))

    return {'status': 'success'}


@app.put("/update/{id}/{newDesc}")

def updateTodo(id, newDesc):
    cur.execute("UPDATE todo SET Description= %s where Todo_id=%s", (newDesc, id))

    return {'status': 'success'}