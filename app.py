from unicodedata import name
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime

# Configuraciones para firebase
cred = credentials.Certificate('serviceAccountKey.json')
fire = firebase_admin.initialize_app(cred)
# Conexión a firestore DB
db = firestore.client()
# Crear referencia a la colección
tasks_ref = db.collection('tasks')

# Leer todas las tasks
def read_tasks():
    #docs = tasks_ref.stream()
    docs = tasks_ref.get()
    for task in docs:
        print(f'ID:{task.id} => DATA:{task.to_dict()}')

# Leer una sola task
def read_task(id):
    task = tasks_ref.document(id).get()
    print(task.to_dict())

def create_task(task):
    new_task = {'name':task, 
            'check':False, 
            'fecha': datetime.datetime.now()}
    tasks_ref.document().set(new_task)

def update_task(id):
    tasks_ref.document(id).update({'check':True})

def delete_task(id):
    res = tasks_ref.document(id).delete()
    print(res)

def get_task_completed():
    completed = tasks_ref.where('check', '==', False).get()
    for task in completed:
        print(f'ID:{task.id} => DATA:{task.to_dict()}')

#create_task(new_task)
#name_task = input('Ingresa nombre de la tarea:\n')
#create_task(name_task)
#update_task('XvbzbD4P5Cxkos9zq2DL')
#delete_task('yQbkpVv3hFkKLwVBPbcU')

get_task_completed()