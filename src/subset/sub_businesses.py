from tqdm import tqdm
import config
import json

from norm import normalize_photos
from nltk import word_tokenize
from nltk.corpus import stopwords
import string

SUB_FILE = "./out/business_subset_{}.json".format(config.SUBSET_SETTINGS['PERC'])


def generate_subset(f_dir, perc):
    fr = open(f_dir, 'r')
    fw = open(SUB_FILE, 'w')
    num_lines = sum(1 for _ in fr)
    sub_num = int(perc * num_lines)

    n_photos_f = open(normalize_photos.NORM_FILE, 'r')
    
    photo_info = []

    for line in n_photos_f:
        json_info = json.loads(line)
        if process_caption(json_info['caption']):
            photo_info.append((json_info['business_id']))

    fr.seek(0)
    with tqdm(total=sub_num) as pbar:
        for line in fr:
            data = json.loads(line)
            if data['business_id'] in photo_info:
                fw.write(line)
                pbar.update(1)

            if pbar.n == sub_num - 1:
                break
    fr.close()
    fw.close()


def process_caption(caption):
    table = str.maketrans('', '', string.punctuation)

    tokens = word_tokenize(caption)
    tokens = [w.lower() for w in tokens]
    stripped = [w.translate(table) for w in tokens]

    words = [word for word in stripped if word.isalpha()]

    stop_words = set(stopwords.words('english'))

    words = [w for w in words if not w in stop_words]

    if len(words) > 2:
        return True

    return False
