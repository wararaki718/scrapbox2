from dataclasses import dataclass

@dataclass
class News:
    url: str
    date_time: str
    title: str
    content: str
    content_vector: list
    label: str

    def to_dict(self):
        return {
            'url': self.url,
            'datetime': self.date_time,
            'title': self.title,
            'content': self.content,
            'content_vector': self.content_vector,
            'label': self.label
        }
