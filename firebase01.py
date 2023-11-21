import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate('C:/Users/AISASE/Downloads/project-5712408682829358646-firebase-adminsdk-h8sb8-334531a09b.json')
firebase_admin.initialize_app(cred,{'databaseURL' : 'https://project-5712408682829358646-default-rtdb.firebaseio.com/'})
dir = db.reference()
dir.update({'model':'KIA'})
dir = db.reference('Class')
dir.update({'TeamB':100})
