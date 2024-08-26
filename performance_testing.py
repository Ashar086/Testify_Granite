def perform_performance_test(url):
    """
    Generate a performance test snippet for the given URL.
    
    Args:
        url (str): The URL to test.
        
    Returns:
        str: Performance test code snippet.
    """
    # Ensure URL is properly formatted
    if not url.startswith("http://") and not url.startswith("https://"):
        raise ValueError("Invalid URL format. URL must start with 'http://' or 'https://'.")
    
    # Extract base domain from URL
    try:
        base_domain = url.split('/')[2]
    except IndexError:
        raise ValueError("URL does not contain enough segments to extract base domain.")
    
    snippet = f"""
import unittest
from selenium import webdriver
from locust import HttpUser, TaskSet, task

class PerformanceTests(TaskSet):

    def search_product(self):
        self.client.get('{url}')
        search_box = self.client.find_element_by_id('search-box-id')  # Update with actual element id
        search_box.send_keys('Python programming')
        search_box.submit()
        search_results = self.client.find_elements_by_class_name('result-class')  # Update with actual class
        self.assertGreater(len(search_results), 0)

    def add_to_cart(self):
        self.client.get('{url}/path/to/product')  # Update with actual product path
        add_to_cart_button = self.client.find_element_by_class_name('add-to-cart-class')  # Update with actual class
        add_to_cart_button.click()
        cart_count = self.client.find_element_by_class_name('cart-count-class').text  # Update with actual class
        self.assertEqual(cart_count, '1')

class LocustTest(HttpUser):
    tasks = [PerformanceTests]
    wait_time = between(5, 15)
    """
    return snippet