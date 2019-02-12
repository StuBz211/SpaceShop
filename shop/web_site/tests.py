from django.test import TestCase

# Create your tests here.
from .models import Product, User, Order, Feedback, 


class ProductModelTestCase(TestCase):
    product_fields = ['id', 'article', 'description', 'price', 'type',
                      'tag', 'rate', 'feedback', 'static_url', 'qa', 'add_datetime', 'show_datetime',
                      'is_new', 'is_recommend','is_best_price']

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_product_fields(self):
        for field in self.product_fields:
            self.assertEqual(hasattr(Product, field), True, msg=f'Product has no attribute {field}')


class UserModelTestCase(TestCase):
    user_fields = ['id', 'login', 'email', 'name', 'password', 'score',
                   'privilege_level', 'interested_pages', 'visited_pages'
                   ]

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_product_fields(self):
        for field in self.user_fields:
            self.assertEqual(hasattr(User, field), True, msg=f'User has no attribute {field}')


class OrderModelTestCase(TestCase):
    order_fields = ['products', 'user_id', 'total_sum', 'address', 'order_datetime']

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_product_fields(self):
        for field in self.order_fields:
            self.assertEqual(hasattr(Order, field), True, msg=f'Order has no attribute {field}')


class FeedbackModelsTestCase(TestCase):
    feedback_fields = ['product_id', 'user_id', 'desctiption', 'rate']

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_product_fields(self):
        for field in self.feedback_fields:
            self.assertEqual(hasattr(Feedback, field), True, msg=f'Feedback has no attribute {field}')


class QuestionAnswerModelTestCase(TestCase):
    question_fields = []

