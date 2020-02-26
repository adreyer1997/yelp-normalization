# Does the dataset need to be normalized? If so, the locations need to be 
# specified too
NORMALIZE_DATASET = True
NORMALIZE_SETTINGS = {
    "NORMALIZE_BUS": False,
    "NORMALIZE_REV": False,
    "NORMALIZE_USE": False,
    "NORMALIZE_SIM": False,
    "NORMALIZE_PHOTOS": False,
    "BUSINESS_FILE": "../yelp/yelp_dataset/business.json",
    "REVIEW_FILE": "../yelp/yelp_dataset/review.json",
    "USERS_FILE": "../yelp/yelp_dataset/user.json",
    "PHOTOS_FILE": "../yelp/yelp_photos/photo.json",
    "PHOTOS_DIR": "../yelp/yelp_photos/photos/"
}

# Generate subset of data and clean user friends that aren't in table
GEN_SUBSET = True
SUBSET_SETTINGS = {
    "SUB_BUS": False,
    "SUB_REV": False,
    "SUB_USE": False,
    "SUB_PHOTOS": False,
    "PERC": 0.01
}

# The CSV format is used for TigerGraph's offline batch loader. The dataset
# needs to be normalized to use this option and will refer to the files in
# NORMALIZE_SETTINGS.
PREPARE_CSV = True
PREPARE_SETTINGS = {
    "PREPARE_BUS": False,
    "PREPARE_REV": False,
    "PREPARE_USE": False,
    "PREPARE_PHOTOS": False
}
