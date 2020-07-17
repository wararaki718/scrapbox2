from base import Base

class Sample(Base):
    def __init__(self):
        self._item = 'sample'

    def get_item(self):
        return self._item
