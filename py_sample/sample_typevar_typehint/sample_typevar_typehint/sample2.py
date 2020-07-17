from base import Base

class Sample2(Base):
    def __init__(self):
        self._item = 'sample2'

    def get_item(self):
        return self._item
