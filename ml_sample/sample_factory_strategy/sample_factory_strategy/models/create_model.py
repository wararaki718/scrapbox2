from .base import BaseModel
from .lda_lr import LdaLr
from .pca_rfc import PcaRfc


class CreateModel():
    def create_model(self, model_name: str) -> BaseModel:
        return {
            'lda_lr': LdaLr(),
            'pca_rfc': PcaRfc()
        }.get(model_name)
