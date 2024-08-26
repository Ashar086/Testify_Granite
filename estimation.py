import random

def estimate_testing_resources(url):
    """
    Estimate testing resources for the given URL with random percentages.
    Args:
        url (str): The URL for which to estimate testing resources.
    Returns:
        str: A string describing the estimated testing resources.
    """
    # Generate random percentages for manual and automation testing
    manual_percentage = random.randint(50, 80)  # Random percentage between 50% and 80%
    automation_percentage = 100 - manual_percentage  # The rest is automation

    return f"Estimated testing resources for {url}: {manual_percentage}% manual, {automation_percentage}% automation."

# Example usage
if __name__ == "__main__":
    url = "http://example.com"  # Replace with the actual URL
    print(estimate_testing_resources(url))
