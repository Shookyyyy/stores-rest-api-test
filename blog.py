from post import Post


class Blog:
    def __init__(self, title, author):
        self.author = author
        self.title = title
        self.posts = []

    def __repr__(self):
        return '{} by {} ({} post{})'.format(self.title,
                                             self.author,
                                             len(self.posts),
                                             's' if len(self.posts) != 1 else '')

    def create_post(self, title, author):
        self.posts.append(Post(title, author))

    def json(self):
        return {'title': self.title, 'author': self.author, 'posts': [post.json() for post in self.posts]}
