#! /usr/bin/python
import time
import selenium.webdriver.support.ui as ui

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Crawler:

	def __init__(self):
		
		#####################################
		#           CONFIGURATION           #
		#####################################
		
		self._target = "person name"
		self._broadcast = "broadcast list name"
		
		#####################################
		#                END                #
		#####################################
		self._driver = None
		self._wait = None
		self._headers = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'

	def initialize_webdriver(self):
		profile = webdriver.FirefoxProfile()
		profile.set_preference("general.useragent.override", self._headers)
		
		self._driver = webdriver.Firefox(profile)
		self._driver.implicitly_wait(30)
		self._driver.set_window_size(1180, 980)

		self._wait = ui.WebDriverWait(self._driver,3)

	def wait_connection(self):
		self._wait.until(
			EC.presence_of_element_located((By.CLASS_NAME, "intro-title"))
		)

	def forward_video(self):
		search = self._driver.find_element_by_xpath('//input[@class="input-search"]')
		search.send_keys(self._broadcast)

		time.sleep(3)
		self._driver.find_element_by_xpath('//span[contains(text(),"{}")]'.format(self._broadcast)).click()
		
		time.sleep(1)
		self._driver.find_element_by_xpath('//button[@class="btn btn-round btn-l btn-action"]').click()

	def start_service(self):
		target = self._driver.find_element_by_xpath('//span[contains(text(),"{}")]'.format(self._target))
		target.click()

		older = ''
		while True:
			last_time = self._driver.find_elements_by_xpath('//span[@class="message-datetime"]')
			new_time = last_time[-1].text
			if new_time in older:
				time.sleep(1)
			else: 
				older = new_time 
				videos = self._driver.find_elements_by_xpath('//div[@class="icon icon-forward-chat btn-forward-chat"]')
				videos[-1].click()
				time.sleep(3)
				self.forward_video()
				time.sleep(1)
				target.click()

	def crawl(self, url):
		self.initialize_webdriver()
		self._driver.get(url)
		self.wait_connection()
		self.start_service()


if __name__ == '__main__':
	crawler = Crawler()
	crawler.crawl("https://web.whatsapp.com/")