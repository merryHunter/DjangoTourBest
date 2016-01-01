from django.test import TestCase

# Create your tests here.

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000/tourbest')

assert 'Tour Best' in browser.title