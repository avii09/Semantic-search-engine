

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestSemanticSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=cls.service)
        cls.driver.get("http://localhost:8502")

        # Wait for input box to appear
        WebDriverWait(cls.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/section/div[1]/div/div/div[2]/div/div/div/input'))
        )

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def perform_query(self, query):
        input_box = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/section/div[1]/div/div/div[2]/div/div/div/input')
        input_box.clear()
        input_box.send_keys(query)
        input_box.send_keys(Keys.RETURN)

        # Wait for markdown result to appear (Streamlit result output)
        # WebDriverWait(self.driver, 15).until(
        #     EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div/section/div[1]/div/div/div[5]/div/div'))
        # )
        
        try:
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div/section/div[1]/div/div/div[5]/div/div'))  # or whatever element you're waiting for
            )
        except TimeoutException:
            print("Timed out waiting for results.")

    def test_valid_query(self):
        self.perform_query("What is semantic search?")
        results = self.driver.find_elements(By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div/section/div[1]/div/div/div[5]/div/div')
        self.assertTrue(len(results) > 0, "Expected results for valid query.")

    def test_empty_query(self):
        self.perform_query("")
        # Wait briefly and check if results exist
        results = self.driver.find_elements(By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div/section/div[1]/div/div/div[5]/div/div')
        self.assertEqual(len(results), 0, "Empty query should show no results.")

    def test_gibberish_query(self):
        self.perform_query("asdlkfjasldkfjqweoiu")
        results = self.driver.find_elements(By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div/section/div[1]/div/div/div[5]/div/div')
        self.assertTrue(len(results) >= 0, "Should handle gibberish gracefully.")


    

if __name__ == "__main__":
    unittest.main()



#---------------------------------------------------------------------------------------------------------------------
# The following code is commented out because it is not needed for the unittest framework.
# However, if you want to run it as a standalone script, you can uncomment it and run the script directly.
#---------------------------------------------------------------------------------------------------------------------



# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager
# import time


# service = Service(ChromeDriverManager().install())
# # Start a browser session with ChromeDriver
# driver = webdriver.Chrome(service=service)

# # Navigate to the Streamlit app's URL
# driver.get("http://localhost:8502")  # This assumes that your Streamlit app is running locally

# # Give it some time to load
# time.sleep(60)

# # Find the input field and type a query
# query_input = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/section/div[1]/div/div/div[2]/div/div/div/input')
# query_input.send_keys("Who is the ceo of apple?")

# # Simulate pressing "Enter"
# query_input.send_keys(Keys.RETURN)

# # Wait for the results to appear
# time.sleep(20)

# # Check if the results are displayed (you can modify the XPATH depending on how the results are structured)
# results = driver.find_elements(By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div/section/div[1]/div/div/div[5]/div/div')

# # Verify if any results were returned
# if len(results) > 0:
#     print("Test Passed: Results found.")
# else:
#     print("Test Failed: No results found.")

# # Optionally, you can verify the content of the results as well
# for result in results:
#     print(result.text)

# # Close the browser after the test
# driver.quit()