from django.test import TestCase, RequestFactory
from .views import MostWantedView, WordView

import json


# Create your tests here.
class MainTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def setup_view(self, view, request, *args, **kwargs):
        view.request = request
        view.args = args
        view.kwargs = kwargs
        return view

    def test_api_most_wanted(self):
        request = self.factory.get('/api/v1/most_wanted')
        view = self.setup_view(MostWantedView(), request)
        response = view.get(request)

        # Valida que se retorne 200
        self.assertEqual(response.status_code, 200)

        # Valida el formato de la respuesta
        self.assertJSONEqual(response.content, {'status': 'success', 'result': {'count': 0, 'word_list': []}})

    def test_api_word_search(self):
        request = self.factory.get('/api/v1/word_search/?word=hello')
        view = self.setup_view(WordView(), request)
        response = view.get(request)

        # Valida que se retorne 200
        self.assertEqual(response.status_code, 200)

        # Valida el formato de la respuesta
        self.assertJSONEqual(response.content, {"status": "success", "result": "27"})
