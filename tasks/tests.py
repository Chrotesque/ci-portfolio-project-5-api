from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Task


class TaskListViewTests(APITestCase):
    """
    Tests for task list view
    """
    def setUp(self):
        """
        Setup class to create test user
        """
        self.username = "Test User"
        self.password = "testpass"
        User.objects.create_user(username=self.username,
                                 password=self.password)

    def test_can_list_tasks(self):
        """
        Tests if a user can see all listed tasks
        """
        test_user = User.objects.get(username=self.username)
        Task.objects.create(owner=test_user,
                            title='This is a test')
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_loggedin_can_create_tasks(self):
        """
        Tests if a logged in user can create a task
        """
        self.client.login(username=self.username, password=self.password)
        response = self.client.post('/tasks/',
                                    {'title': 'Test Title',
                                     'body': 'Test Body'})

        count = Task.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_not_loggedin_can_create_tasks(self):
        """
        Tests if a user that is not logged in can create a task
        """
        response = self.client.post('/tasks/',
                                    {'title': 'Test Title',
                                     'body': 'Test Body'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class TaskDetailViewTests(APITestCase):
    """
    Tests for task detail view
    """
    def setUp(self):
        """
        Setup class to create test user
        """
        self.nameone = "Test User"
        self.passone = "testpass"
        self.nametwo = "Test User 2"
        self.passtwo = "testpass2"
        self.userone = User.objects.create_user(username=self.nameone,
                                                password=self.passone)
        self.usertwo = User.objects.create_user(username=self.nametwo,
                                                password=self.passtwo)
        Task.objects.create(owner=self.userone,
                            title="Test Title 1",
                            body="Test Body 1")
        Task.objects.create(owner=self.usertwo,
                            title="Test Title 2",
                            body="Test Body 2")

    def test_can_retrieve_task_using_valid_id(self):
        """
        Tests if a user can see task details with valid id
        """
        response = self.client.get('/tasks/1')
        self.assertEqual(response.data['title'], 'Test Title 1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_retrieve_task_using_invalid_id(self):
        """
        Tests if a user can see task details without valid id
        """
        response = self.client.get('/tasks/1000')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_can_update_own_task(self):
        """
        Tests if a user can update their own task
        """
        self.client.login(username=self.nameone, password=self.passone)
        response = self.client.put('/tasks/1',
                                   {'title': 'Test Title',
                                    'body': 'Test Body'})
        task = Task.objects.filter(pk=1).first()
        self.assertEqual(task.title, 'Test Title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_update_foreign_task(self):
        """
        Tests if a user can update another users task
        """
        self.client.login(username=self.nameone, password=self.passone)
        response = self.client.put('/tasks/2',
                                   {'title': 'Test Title',
                                    'body': 'Test Body'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
