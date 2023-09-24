from fastapi import FastAPI
import psycopg2

conn = psycopg2.connect(dbname="verceldb",host="ep-tight-math-26832109-pooler.us-east-1.postgres.vercel-storage.com", port="5432", user="default", password="rwRX5KiB4MDk")

print("Database connected successfully")

cur = conn.cursor()

app = FastAPI()

@app.get("/todos")

def refresh():

    cur.execute("SELECT * FROM todo")
    res = cur.fetchall()

    return res


@app.post("/add/{desc}")

def addTodo(desc):
    
    cur.execute("INSERT INTO todo (Description) VALUES(%s)", (desc,))

    return refresh()


@app.delete("/delete/{id}")

def deleteTodo(id):
    cur.execute("DELETE FROM todo WHERE Todo_id = %s", (id,))

    return refresh()


@app.put("/update/{id}/{newDesc}")

def updateTodo(id, newDesc):
    cur.execute("UPDATE todo SET Description= %s where Todo_id=%s", (newDesc, id))

    return refresh()