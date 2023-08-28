import logging
from selenium import webdriver


class WebDriver(webdriver.Chrome):
    """
    Driver class that implements simple settings, methods and attributes, for a
    web driver

    Args:
        webdriver (webdriver.Chrome): Base class from Selenium library
    """
    def __init__(self, address="https://realworld.svelte.dev/",
                 path="C:/bin/chromedriver.exe", maximize_window: bool = True):
        """
        Constructor for the WebDriver class that inherits from webdriver.Chrome

        Args:
            address (str, optional): Web address to which the driver will be sent after
                starting. Defaults to "https://realworld.svelte.dev/".
            path (str, optional): Path to the driver executable. Defaults to
                "C:/bin/chromedriver.exe".
        """
        self.address = address
        super().__init__(executable_path=path)
        logging.info(f"Chrome driver successfully started using '{path}'")
        self.start(maximize_window)

    def start(self, maximize_window: bool = True):
        """
        Maximizes window and sends driver to the address passed when creating the object
        """
        if maximize_window:
            self.maximize_window()
        self.implicitly_wait(5)
        self.get(self.address)
        logging.info(f"Chrome driver successfully sent to '{self.address}'")
