import json
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Todos


class TodoModelTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todos.objects.create(
            title="First Todo",
            body="A body of text here"
        )

    def test_model_content(self):
        self.assertEqual(self.todo.title, "First Todo")
        self.assertEqual(self.todo.body, "A body of text here")
        self.assertEqual(str(self.todo), "First Todo")

    def test_api_list_view(self):
        response = self.client.get(reverse("todo_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todos.objects.count(), 1)
        data = json.loads(response.content)
        self.assertEqual(data[0]["title"], self.todo.title)
        self.assertEqual(data[0]["body"], self.todo.body)

    def test_api_detail_view(self):
        response = self.client.get(
            reverse("todo_detail", kwargs={"pk": self.todo.pk}),
            format="json"
        )
        data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todos.objects.count(), 1)

        self.assertEqual(data["title"], "First Todo")
        self.assertEqual(data["body"], "A body of text here")
