import json
import config

from tqdm import tqdm

SUB_FILE = "./out/photos_subset_{}.json".format(config.SUBSET_SETTINGS['PERC'])

def generate_subset(f_dir, perc):
    fr = open(f_dir, 'r')
    fw = open(SUB_FILE, 'w')
    num_lines = sum(1 for _ in fr)
    sub_num = int(perc * num_lines)

    fr.seek(0)
    with tqdm(total=sub_num) as pbar:
        for line in fr:
            data = json.loads(line)
            if data["caption"] != "":
                fw.write(line)
                pbar.update(1)

            if pbar.n == sub_num - 1:
                break
    fr.close()
    fw.close()
