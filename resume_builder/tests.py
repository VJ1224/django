from django.test import TestCase
from django.test import Client
from .forms import resumeForm
from .models import resume

class ViewsTestCase(TestCase):
    def test_(self):
        """Checks if homepage of Resume Builder is loading"""
        response = self.client.get('/resume/')
        self.assertEqual(response.status_code,200)
    
class FormsTestCase(TestCase):
    def test_addItem_true(self):
        """Checks valid form"""
        form_data = {'name': 'Test', 'email':'test@gmail.com', 'number':'123456890'}
        form = resumeForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_addItem_false(self):
        """Checks invalid form"""
        form_data = {'name': 'Test', 'email':'test@gmail.com', 'work':'Work experience'}
        form = resumeForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_addItem_email(self):
        """Checks invalid email"""
        form_data = {'name': 'Test', 'email':'test.com', 'number':'123456890'}
        form = resumeForm(data=form_data)
        self.assertFalse(form.is_valid())

class ModelsTestCase(TestCase):
    def test_item_create(self):
        """Checks resume creation"""
        item = resume.objects.create(name="Test",email="test@gmail.com",number="123456890")
        self.assertTrue(isinstance(item,resume))