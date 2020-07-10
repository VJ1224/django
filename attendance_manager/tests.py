from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from attendance_manager.forms import courseForm
from attendance_manager.models import Course

class ViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.user.set_password('12345')
        self.user.save()
        self.client = Client()
        logged_in = self.client.login(username='testuser', password='12345')

    def test_home(self):
        """Checks if homepage of Attendance Manager is loading"""
        response = self.client.get('/attendance/')
        self.assertEqual(response.status_code,200)
    
class FormsTestCase(TestCase):
    def test_addItem_true(self):
        """Checks valid form"""
        form_data = {'code': 'CS101', 'title':'Computer Science'}
        form = courseForm(data=form_data)
        self.assertTrue(form.is_valid())

class ModelsTestCase(TestCase):
    def test_item_create(self):
        """Checks Course creation"""
        item = Course.objects.create(code="CS101",title="Computer Science")
        self.assertTrue(isinstance(item,Course))