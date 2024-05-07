# Todo-FastAPI
| Endpoint | Method | Description | Body Request | Body Response | Error Response |
| -------- | ------ | ----------- | ------------ | ------------- | ----------- |
| /createTodo | POST | Create a Todo. | `{ "id": {id}, "title": "{title}", "completed": false }` | `{ "id": {id}, "title": "{title}", "completed": false }` | `{"error": "Todo not found"}` |
| /getTodoById/{todo_id} | GET | Get a todo by ID. | - | `{ "id": {id}, "title": "{title}", "completed": {completed} }` | `{"error": "Todo not found"}` |
| /getTodoByTitle/{title} | GET | Get a todo by title. | - | `{ "id": {id}, "title": "{title}", "completed": {completed} }` | `{"error": "No todos found with title '{title}'"}` |
| /deleteById/{todo_id} | DELETE | Delete a todo by ID. | - | `{"message": "Todo deleted successfully"}` | `{"error": "Todo not found"}` |
| /deleteByTitle/{title} | DELETE | Delete a todo by Title. | - | `{"message": "All todos with title '{title}' deleted successfully"}` | - |
| /deleteAll | DELETE | Delete every todo. | - | `{"message": "All todos deleted successfully"}` | - |
| /getAllTodos | GET | Get every todo. | - | `[{ "id": {id}, "title": "{title}", "completed": {completed} }]` | - |
| /updateTodo/{todo_id} | PUT | Update a todo. | `{ "id": {id}, "title": "{title}", "completed": {completed} }` | `{"message": "Todo updated successfully"}