from unittest import TestCase
from blog import Blog
class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual('Test',b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b = Blog('Test', 'Test Author')

        expected1 = 'Test by Test Author (0 posts)'
        self.assertEqual(expected1, b.__repr__())

    def test_repr_multiple_posts(self):
        b2 = Blog('My Day', 'Rolf')
        b2.posts = ['test1', 'test2']

        self.assertEqual(b2.__repr__(), 'My Day by Rolf (2 posts)')


