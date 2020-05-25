import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials

cred = credentials.Certificate("service credential file ")  # credentials file link
firebase_admin.initialize_app(cred)
user = auth.create_user(
    uid='S57004',
    password='secret'
)
print('Sucessfully created new user')