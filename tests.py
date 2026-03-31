from django.test import TestCase, Client
from django.urls import reverse
from .models import Task

class TaskModelTest(TestCase):
    def test_create_task(self):
        task = Task.objects.create(title='Buy milk')
        self.assertEqual(str(task), 'Buy milk')
        self.assertFalse(task.done)

    def test_toggle_done(self):
        task = Task.objects.create(title='Test task')
        task.done = True
        task.save()
        self.assertTrue(Task.objects.get(pk=task.pk).done)


class TaskViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_get(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_add_task(self):
        response = self.client.post(reverse('index'), {'title': 'New task'})
        self.assertRedirects(response, reverse('index'))
        self.assertEqual(Task.objects.count(), 1)

    def test_add_empty_task_ignored(self):
        self.client.post(reverse('index'), {'title': '   '})
        self.assertEqual(Task.objects.count(), 0)

    def test_toggle_task(self):
        task = Task.objects.create(title='Toggle me')
        self.client.get(reverse('toggle', args=[task.pk]))
        self.assertTrue(Task.objects.get(pk=task.pk).done)

    def test_delete_task(self):
        task = Task.objects.create(title='Delete me')
        self.client.get(reverse('delete', args=[task.pk]))
        self.assertEqual(Task.objects.count(), 0)
