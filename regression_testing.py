def run_regression_tests(url):
    template = f"""
import unittest
from selenium import webdriver

class WebsiteRegressionTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_results(self):
        self.driver.get('{url}')
        search_box = self.driver.find_element_by_id('twotabsearchtextbox')
        search_box.send_keys('Python programming')
        search_box.submit()
        search_results = self.driver.find_elements_by_class_name('a-link-normal')
        for result in search_results:
            result_title = result.text
            self.assertIn('Python programming', result_title)

    def test_add_to_cart_speed(self):
        self.driver.get('{url}/dp/B08N6Z2L2D')
        add_to_cart_button = self.driver.find_element_by_class_name('a-button-text')
        add_to_cart_button.click()
        cart_count = self.driver.find_element_by_class_name('nav-cart-count').text
        self.assertEqual(cart_count, '1')
        cart_items = self.driver.find_elements_by_class_name('a-list-item')
        self.assertLess(len(cart_items), 10)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
    """
    return template.strip()

