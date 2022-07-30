import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

project_id = 'flask-platzi-357902'

cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': project_id,
})

db = firestore.client()
# users
def get_users():
    return db.collection('users').get()

def get_user_id(user_id):
    return db.collection("users").document(user_id).get()

def user_put(user_data):
    user_ref = db.collection('users').document(user_data.username)
    user_ref.set({'password': user_data.password})

# todos --------------------------------------------
def get_todos(user_id):
    return db.collection("users").document(user_id).collection("todos").get()

def put_todos(user_id, descrition):
    todos_collection_ref = db.collection("users").document(user_id).collection("todos")
    todos_collection_ref.add({"descripcion": descrition, "done": False})


def delete_todo(user_id, todo_id):
    todo_ref = db.document('users/{}/todos/{}'.format(user_id, todo_id))
    todo_ref.delete()
