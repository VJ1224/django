from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from to_do.forms import toDoForm
from to_do.models import toDoItem

class ViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.user.set_password('12345')
        self.user.save()
        self.client = Client()
        logged_in = self.client.login(username='testuser', password='12345')

    def test_toDoHome(self):
        """Checks if homepage of To-Do list is loading"""
        response = self.client.get('/todo/')
        self.assertEqual(response.status_code,200)
    
class FormsTestCase(TestCase):
    def test_addItem_true(self):
        """Checks valid form"""
        form_data = {'title': 'Testing', 'category':'Work',
            'date_due':'2020-08-01', 'description':'Testing true'}
        form = toDoForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_addItem_false(self):
        """Checks invalid form"""
        form_data = {'title': 'Testing', 'category':'Work',
            'date_due':'01-08-2020', 'description':'Testing false'}
        form = toDoForm(data=form_data)
        self.assertFalse(form.is_valid())

class ModelsTestCase(TestCase):
    def test_item_create(self):
        """Checks toDoItem creation"""
        item = toDoItem.objects.create(title="Test",category="Work",date_due="2020-08-01",description="Testing testing")
        self.assertTrue(isinstance(item,toDoItem))