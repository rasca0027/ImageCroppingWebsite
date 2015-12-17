import cPickle as pickle
from .models import Image

def init_data():
    results = pickle.load(open('database.pkl', 'rb'))

    for photo_id, user_id, url, category, isdeleted in results:
        if not isdeleted:
            obj = Image.objects.update_or_create(photo_id=photo_id, 
                    defaults={'user_id':user_id, 'url':url, 'category':category})

def load_data():
    results = pickle.load(open('database.pkl', 'rb'))

    for photo_id, user_id, url, category, isdeleted in results:
        if not isdeleted:
            obj = Image.objects.get_or_create(photo_id=photo_id, 
                    defaults={'user_id':user_id, 'url':url, 'category':category})
