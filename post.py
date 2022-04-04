class Post:

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return f'Title is {self.title} and the content is {self.content}'


    def json(self):
        return {
            'title': self.title,
            'content': self.content,
        }