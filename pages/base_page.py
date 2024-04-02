

class BasePage:

    def __init__(self, driver,url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def get_text(self, locator):
        return self.driver.find_element(*locator).text

