import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path="D:\\chromedriver\\chromedriver.exe")
    driver.get("https://www.facebook.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()