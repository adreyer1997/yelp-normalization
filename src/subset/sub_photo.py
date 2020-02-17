import sys
sys.path.append('/home/andrei/Documents/University/2020/Honours Project/yelp-normalization')
sys.path.append('/home/andrei/Documents/University/2020/Honours Project/yelp-normalization/src')

from tqdm import tqdm
import config
from subset import sub_photos
import os
import json
import shutil

def generate_subset(f_dir, photos_dir, training_dir):
    fr = open(f_dir, 'r')
    num_lines = sum(1 for _ in fr)
    photos = os.listdir(photos_dir)

    if os.path.exists(training_dir) is False:
        os.mkdir(training_dir)

    fr.seek(0)
    with tqdm(total=num_lines) as pbar:
        for line in fr:
            data = json.loads(line)
            try:
                file_name = photos[photos.index('{}.jpg'.format(data['photo_id']))]
                shutil.copyfile('{}/{}'.format(photos_dir, file_name), '{}/{}'.format(training_dir, file_name))
                pbar.update(1)
            except ValueError:
                print('Not Found')
                continue

    fr.close()
