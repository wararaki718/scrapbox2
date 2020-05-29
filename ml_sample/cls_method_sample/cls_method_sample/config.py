from dataclasses import dataclass

import yaml

@dataclass
class Config:
    model_path: str

    @classmethod
    def load(cls, config_path: str):
        with open(config_path, 'rt') as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
        return Config(**config)
