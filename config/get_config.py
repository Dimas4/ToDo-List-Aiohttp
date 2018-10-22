import yaml
import os


def get_config():
    with open(os.path.join("config", "config.yaml"), 'r') as file:
        config = yaml.load(file)
    return config
