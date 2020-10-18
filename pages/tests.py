from django.test import TestCase

# Create your tests here.

class ViewTest(TestCase):
	
	def test_view_returns_hello_world_response(self):
		response = self.client.get('/')
		self.assertEqual(response.content.decode(), 'Hello World')
