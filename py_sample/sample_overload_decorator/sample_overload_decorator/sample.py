from typing import overload


class Sample:
    def __init__(self):
        pass

    @overload
    def call(self, v: int) -> int: ...
    @overload
    def call(self, v: str) -> int: ...
    @overload
    def call(self, v: float) -> int: ...

    def call(self, v):
        if isinstance(v, float):
            return str(v)
        return int(v)
