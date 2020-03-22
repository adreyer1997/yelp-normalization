import json
import config

from tqdm import tqdm
from subset import sub_businesses
from nltk import word_tokenize
from nltk.corpus import stopwords
import string

SUB_FILE = "./out/photos_subset_{}.json".format(config.SUBSET_SETTINGS['PERC'])

def generate_subset(f_dir, perc):
    fr = open(f_dir, 'r')
    fw = open(SUB_FILE, 'w')

    n_business_f = open(sub_businesses.SUB_FILE, 'r')
    businesses = set([json.loads(d)['business_id'] for d in n_business_f])
    n_business_f.close()

    num_lines = sum(1 for _ in fr)
    sub_num = int(perc * num_lines)

    fr.seek(0)
    with tqdm(total=sub_num) as pbar:
        for line in fr:
            data = json.loads(line)
            if process_caption(data['caption']) and data["business_id"] in businesses:
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
