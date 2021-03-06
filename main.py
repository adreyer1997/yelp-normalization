import sys
from pprint import pprint

sys.path.append('/home/andrei-ubuntu/Documents/University/2020/Honours Project/yelp-normalization')
sys.path.append('/home/andrei-ubuntu/Documents/University/2020/Honours Project/yelp-normalization/src')

from style.styles import style

import os

from tqdm import tqdm

def normalize(file_dir, out_dir, process_line):
    fr = open(file_dir, 'r')
    fw = open(out_dir, 'a')
    num_lines = sum(1 for _ in open(file_dir, 'r'))

    fr.seek(0)
    with tqdm(total=num_lines) as pbar:
        for line in fr:
            process_line(fw, line)
            pbar.update(1)
    fr.close()
    fw.close()

def normalize_file(norm_setting_file, norm_module):
    if not os.path.isfile(norm_setting_file) is True:
        print('[WARN]', norm_setting_file, ' is not a file! Skipping...')
    else:
        print("[INFO] Normalizing {}".format(norm_setting_file))
        normalize(file_dir=norm_setting_file,
                  out_dir=norm_module.NORM_FILE,
                  process_line=norm_module.process_line)


if __name__ == "__main__":
    import config

    from configure_settings import run_configurations
    from norm import normalize_businesses, normalize_reviews, normalize_users, normalize_photos
    from subset import sub_businesses, sub_reviews, sub_users, sub_photos, sub_photo
    from prep_csv import csv_businesses, csv_reviews, csv_users, csv_photos

    run_configurations()

    if os.path.exists("./out") is False:
        os.mkdir("./out")


    print("<--- Yelp Normalizer --->")

    if config.NORMALIZE_DATASET is True:
        print("|--- Normalizing Original Data --|")
        # Normalize businesses
        if config.NORMALIZE_SETTINGS["NORMALIZE_BUS"] is True:
            print("[INFO] Normalizing businesses...")
            normalize_file(norm_setting_file=config.NORMALIZE_SETTINGS["BUSINESS_FILE"],
                           norm_module=normalize_businesses)
        # Normalize users
        if config.NORMALIZE_SETTINGS["NORMALIZE_USE"] is True:
            print("[INFO] Normalizing users...")
            normalize_file(norm_setting_file=config.NORMALIZE_SETTINGS["USERS_FILE"],
                           norm_module=normalize_users)
        # Normalize reviews
        if config.NORMALIZE_SETTINGS["NORMALIZE_REV"] is True:
            print("[INFO] Normalizing reviews...")
            normalize_file(norm_setting_file=config.NORMALIZE_SETTINGS["REVIEW_FILE"],
                           norm_module=normalize_reviews)

        # Normalize photos
        if config.NORMALIZE_SETTINGS["NORMALIZE_PHOTOS"] is True:
            print("[INFO] Normalizing photos...")
            normalize_file(norm_setting_file=config.NORMALIZE_SETTINGS["PHOTOS_FILE"],
                           norm_module=normalize_photos)

    if config.GEN_SUBSET is True:
        print("|--- Generating Subset of Data --|")
        # Subset businesses
        if config.SUBSET_SETTINGS["SUB_BUS"] is True:
            print("[INFO] Generating subset of businesses...")
            sub_businesses.generate_subset(f_dir=normalize_businesses.NORM_FILE,
                                           perc=config.SUBSET_SETTINGS["PERC"])

        # Subset users
        if config.SUBSET_SETTINGS["SUB_USE"] is True:
            print("[INFO] Generating subset of users...")
            sub_users.generate_subset(f_dir=normalize_users.NORM_FILE,
                                      perc=config.SUBSET_SETTINGS["PERC"])

        # Subset reviews
        if config.SUBSET_SETTINGS["SUB_REV"] is True:
            print("[INFO] Generating subset of reviews...")
            sub_reviews.generate_subset(f_dir=normalize_reviews.NORM_FILE,
                                        perc=config.SUBSET_SETTINGS["PERC"])

        # Subset Photo images
        if config.SUBSET_SETTINGS["SUB_PHOTOS"] is True:
            print("[INFO] Generating subset of photos information...")
            sub_photos.generate_subset(f_dir=normalize_photos.NORM_FILE,
                                       perc=config.SUBSET_SETTINGS["PERC"])

            print("[INFO] Generating subset of photo")
            sub_photo.generate_subset(f_dir=sub_photos.SUB_FILE, 
                                      photos_dir=config.NORMALIZE_SETTINGS["PHOTOS_DIR"],
                                      training_dir='./out/training_photos')

    if config.PREPARE_CSV is True:
        print("|--- Generating CSV from Data Subsets --|")
        # CSV businesses
        if config.PREPARE_SETTINGS["PREPARE_BUS"] is True:
            print("[INFO] Preparing businesses as CSV...")
            csv_businesses.write_csv(sub_businesses.SUB_FILE)

        # CSV reviews
        if config.PREPARE_SETTINGS["PREPARE_REV"] is True:
            print("[INFO] Preparing reviews as CSV...")
            csv_reviews.write_csv(sub_reviews.SUB_FILE)

        # CSV users
        if config.PREPARE_SETTINGS["PREPARE_USE"] is True:
            print("[INFO] Preparing users as CSV...")
            csv_users.write_csv(sub_users.SUB_FILE)

        # CSV Photos
        if config.PREPARE_SETTINGS["PREPARE_PHOTOS"] is True:
            print("[INFO] Preparing photos as CSV")
            csv_photos.write_csv(sub_photos.SUB_FILE)
