from PIL import Image
import os

def getThumbnail(path, isPath=True):
    filename_path, filename = os.path.split(path)
    filename_split = filename.split('.')
    filename = '.'.join(filename_split[0: len(filename_split)-1])
    ext = filename_split[len(filename_split)-1]
    filename_path = os.path.join(filename_path, 'thumbnails')
    if isPath and not os.path.exists(filename_path):
        os.mkdir(filename_path)
    return '%s.thumbnail.%s' %(os.path.join(filename_path, filename), ext)

def make_thumbnail(path, size=(200,200)):
    thumbnail_path = getThumbnail(path)
    img = Image.open(path)
    img.thumbnail(size)
    img.save(thumbnail_path)


def delete_thumbnail(path):
    thumbnail_path = getThumbnail(path)
    if os.path.exists(thumbnail_path):
        os.remove(thumbnail_path)

