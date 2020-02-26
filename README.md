# normalize-dataset

The following script preprocesses the dataset and performs feature selection. This has three functionalities which are configurable by executing `main.py`. This will bring up a CLI program where the datasets that need to be preprocessed can be selected.

## Installation
These scripts have a dependency on `PyInquirer` and `tqdm`. Run
```
    conda env create -f conda_env.yml
```
to create the conda environemnt required. This will install some other packages as well such as PyTorch. A separate environment for the scripts only will be created at a later stage.

## Feature Selection and Normalization

This takes the raw Yelp Challenge Dataset and converts it to conventional JSON while discarding unnecessary features.

## Generating a Subset

Given a percentage of the dataset, a subset of the dataset will be generated. This percentage applies to the businesses and users. The reviews which are present and connect users and businesses in the given subset are then added.

## Converting to CSV

Since TigerGraph's bulk offline loader uses CSV, is it necessary to convert the data to CSV. This is to be done before uploading the data to TigerGraph.

### Credits for base scripts to David Baker Effendi