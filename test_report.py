import pytest
import os

def generate_test_report(site_name):
    site_name = site_name.lower().replace(" ", "_")  # Format the site name
    test_code = f"""   
import unittest
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner

class {site_name.capitalize()}Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_product(self):
        self.driver.get('{site_name}')
        search_box = self.driver.find_element_by_id('twotabsearchtextbox')
        search_box.send_keys('Python programming')
        search_box.submit()
        search_results = self.driver.find_elements_by_class_name('a-link-normal')
        self.assertGreater(len(search_results), 0)

    def test_add_to_cart(self):
        self.driver.get('{site_name}/dp/B08N6Z2L2D')
        add_to_cart_button = self.driver.find_element_by_class_name('a-button-text')
        add_to_cart_button.click()
        cart_count = self.driver.find_element_by_class_name('nav-cart-count').text
        self.assertEqual(cart_count, '1')

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='test_reports'))
"""
    return test_code

if __name__ == "__main__":
    site_name = input("Enter the site name (e.g., 'Amazon'): ")
    site_url = input(f"Enter the URL for {site_name}: ")
    
    test_code = generate_test_report(site_name, site_name)
    print("Generated Test Report Snippet:\n")
    print(test_code)

