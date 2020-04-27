from dataclasses import dataclass

@dataclass
class News:
    url: str
    date_time: str
    title: str
    content: str
    label: str
