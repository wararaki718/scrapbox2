from dataclasses import dataclass

@dataclass
class News:
    url: str
    date_time: str
    title: str
    content: str
    label: str

    def to_dict(self):
        return {
            'url': self.url,
            'datetime': self.date_time,
            'title': self.title,
            'content': self.content,
            'label': self.label
        }
