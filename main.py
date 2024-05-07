from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

class Todo(BaseModel):
    id: int
    title: str
    completed: bool = False  

todo_id_count = 0

todos = {}

@app.post("/createTodo")
def create_todo(todo: Todo):
    global todo_id_count
    todo_id = todo_id_count
    todo.id = todo_id
    todos[todo_id] = todo
    todo_id_count += 1 
    return todo

@app.get("/getTodoById/{todo_id}")
def get_todo_by_id(todo_id: int):
    if todo_id in todos:
        return todos[todo_id]
    else:
        return {"error": "Todo not found"}

@app.get("/getTodoByTitle/{title}")
def get_todo_by_title(title: str):
    filtered_todos = [todo for todo in todos.values() if todo.title == title]
    if filtered_todos:
        return filtered_todos
    else:
        return {"error": f"No todos found with title '{title}'"}

@app.delete("/deleteById/{todo_id}")
def delete_todo_by_id(todo_id: int):
    if todo_id in todos:
        del todos[todo_id]
        return {"message": "Todo deleted successfully"}
    else:
        return {"error": "Todo not found"}

@app.delete("/deleteByTitle/{title}")
def delete_todo_by_title(title: str):
    todos_to_delete = [todo_id for todo_id, todo in todos.items() if todo.title == title]
    if todos_to_delete:
        for todo_id in todos_to_delete:
            del todos[todo_id]
        return {"message": f"All todos with title '{title}' deleted successfully"}
    else:
        return {"error": f"No todos found with title '{title}'"}

@app.delete("/deleteAll")
def delete_all_todos():
    todos.clear()
    return {"message": "All todos deleted successfully"}

@app.get("/getAllTodos")
def get_all_todos():
    return list(todos.values())

@app.put("/updateTodo/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    if todo_id in todos:
        todos[todo_id] = updated_todo
        return {"message": "Todo updated successfully"}
    else:
        return {"error": "Todo not found"}