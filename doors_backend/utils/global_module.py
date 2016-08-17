from django.conf import settings
import os
from zipfile import ZipFile
from doors_goods_service.models import Goods, TypesOfGoods, Properties, GoodsProperties, Values
import codecs

def uploaded_file(f):
    print(settings.MEDIA_ROOT + str(f))
    with open(os.path.join(settings.MEDIA_ROOT, str(f)), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def extract_files(f, del_file=True):
    filename = os.path.join(settings.MEDIA_ROOT, str(f))
    zf = ZipFile(filename)
    zf.extractall(settings.MEDIA_ROOT)
    zf.close()
    if del_file:
        os.remove(filename)

def load_files(f):
    foto_folder = os.path.join(settings.MEDIA_ROOT, str(f).split('.')[0])
    import_file = os.path.join(foto_folder, 'import.txt')
    with open(import_file) as import_data:
        for line in import_data:
            door_name, fotos_list, door_params = line.split(';')
            for foto in fotos_list.split(','):
                try:
                    add_new_door(door_name+'_'+foto, os.path.join(str(f).split('.')[0], foto+'.jpg'), door_params)
                except:
                    pass

def add_new_door(door_name,foto,door_params):
    type = TypesOfGoods.objects.get(id=1)
    door = Goods.objects.create(article = door_name, name = door_name, type = type, foto = foto)
    add_door_params(door, door_params)

def add_door_params(door, door_params):
    for param in door_params.split(','):
        param_name, param_value= param.split(':')
        obj_param, created = Properties.objects.get_or_create(name=param_name)
        obj_param_value, created  = Values.objects.get_or_create(good_property=obj_param, value=param_value)
        door_param = GoodsProperties.objects.get_or_create(good=door, value=obj_param_value)