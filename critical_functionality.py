def test_critical_functionality(url):
    """
    Generate Selenium test code snippets for a given URL.
    Args:
        url (str): The URL to be tested.
    Returns:
        str: The generated test code as a string.
    """
    site_name = url.split("//")[-1].split("/")[0]  # Extract the domain name
    test_code = f"""
import unittest
from selenium import webdriver

class {site_name.capitalize()}Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_product(self):
        self.driver.get('{url}')
        search_box = self.driver.find_element_by_id('twotabsearchtextbox')
        search_box.send_keys('Python programming')
        search_box.submit()
        search_results = self.driver.find_elements_by_class_name('a-link-normal')
        self.assertGreater(len(search_results), 0)

    def test_add_to_cart(self):
        self.driver.get('{url}/dp/B08N6Z2L2D')
        add_to_cart_button = self.driver.find_element_by_class_name('a-button-text')
        add_to_cart_button.click()
        cart_count = self.driver.find_element_by_class_name('nav-cart-count').text
        self.assertEqual(cart_count, '1')

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
"""
    return test_code


