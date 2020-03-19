import json
import config

from tqdm import tqdm
from subset import sub_businesses

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
            if data["caption"] != "" and data["business_id"] in businesses:
                fw.write(line)
                pbar.update(1)

            if pbar.n == sub_num - 1:
                break
    fr.close()
    fw.close()
