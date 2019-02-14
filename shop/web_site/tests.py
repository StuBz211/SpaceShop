from django.test import TestCase

# Create your tests here.
from .models import Product, User, Order, Review


class ProductModelTestCase(TestCase):
    product_fields = ['id', 'article', 'description', 'price', 'category',
                      'tags', 'rate', 'reviews', 'add_datetime', 'show_datetime',  #'image',
                      'is_new', 'is_recommend', 'is_best_price']
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_product_fields(self):
        for field in self.product_fields:
            self.assertEqual(hasattr(Product, field), True, msg=f'Product has no attribute {field}')


class UserModelTestCase(TestCase):
    user_fields = ['id', 'login', 'email', 'name', 'password', 'score',
                   'privilege_level', 'visited_pages'
                   ]

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_product_fields(self):
        for field in self.user_fields:
            self.assertEqual(hasattr(User, field), True, msg=f'User has no attribute {field}')


class OrderModelTestCase(TestCase):
    order_fields = ['products', 'total_sum', 'address', 'order_datetime', 'note', 'status']

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_product_fields(self):
        for field in self.order_fields:
            self.assertEqual(hasattr(Order, field), True, msg=f'Order has no attribute {field}')


class ReviewModelsTestCase(TestCase):
    feedback_fields = ['title', 'user', 'description', 'rate', 'date']
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_product_fields(self):
        for field in self.feedback_fields:
            self.assertEqual(hasattr(Review, field), True, msg=f'Review has no attribute {field}')


class QuestionAnswerModelTestCase(TestCase):
    question_fields = []

