from PyInquirer import prompt, Separator
from style.styles import style
import config

def configure_normalize():
    normalize_options = [
            {
                'type': 'checkbox',
                'message': 'Select data to be normalized',
                'name': 'normalize_data',
                'choices': [
                    Separator('= Normalize Data ='),
                    {
                        'name': 'NORMALIZE_BUS',
                    },
                    {
                        'name': 'NORMALIZE_REV',
                    },
                    {
                        'name': 'NORMALIZE_USE',
                    },
                    {
                        'name': 'NORMALIZE_PHOTOS'
                    },
                ]    
            }
        ]

    return normalize_options

def configure_subset():
    subset_options = [
        {
            'type': 'checkbox',
            'message': 'Select data to be normalized',
            'name': 'subset_data',
            'choices': [
                Separator('= Subset Data ='),
                {
                    'name': 'SUB_BUS'
                },
                {
                    'name': 'SUB_REV',
                },
                {
                    'name': 'SUB_USE',
                },
                {
                    'name': 'SUB_PHOTOS'
                },
            ]    
        }
    ]

    return subset_options

def configure_csv():
    csv_options = [
        {
            'type': 'checkbox',
            'message': 'Select data to be normalized',
            'name': 'csv_data',
            'choices': [
                Separator('= Prepare CSV Data ='),
                {
                    'name': 'PREPARE_BUS'
                },
                {
                    'name': 'PREPARE_REV',
                },
                {
                    'name': 'PREPARE_USE',
                },
                {
                    'name': 'PREPARE_PHOTOS'
                },
            ]    
        }
    ]

    return csv_options


def run_configurations():
    config_answers = dict()

    normalize_answers = prompt(configure_normalize(), style=style)
    subset_answers = prompt(configure_subset(), style=style)
    csv_answers = prompt(configure_csv(), style=style)

    for key, val in normalize_answers.items():
        if len(val) > 0:
            config.NORMALIZE_DATASET = True
        for option in val:
            config.NORMALIZE_SETTINGS[option] = True

    for key, val in subset_answers.items():
        if len(val) > 0:
            config.GEN_SUBSET = True
        for option in val:
            config.SUBSET_SETTINGS[option] = True

    for key, val in csv_answers.items():
        if len(val) > 0:
            config.PREPARE_CSV = True
        for option in val:
            config.PREPARE_SETTINGS[option] = True