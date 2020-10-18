from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time

class FunctionalTests(StaticLiveServerTestCase):
	
	def setUp(self):
		self.browser = webdriver.Firefox()
		
	def tearDown(self):
		self.browser.quit()

	def test_home_page_diplays_hello_world(self):
		# jack goes to this new site
		self.browser.get(self.live_server_url)
		
		# he sees a big 'Hello World' in it's title
		time.sleep(5)
		self.assertIn('Hello World', self.browser.title)
