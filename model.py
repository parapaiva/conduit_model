import logging
from typing import Union

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

from driver import WebDriver


class WebPage():
    """
    Base class for web pages in the application
    """

    def __init__(self, web_driver: WebDriver):
        self.xpath = {}
        self.driver = web_driver

    def click(self, web_element: WebElement):
        """
        Clicks the page element provided

        Args:
            web_element: Object corresponding to the page element to be clicked, usually a
                Button or ComboBox
        """
        web_element.click()

    def _send_text_to_input(self, field: Union[str, WebElement], value: str):
        """
        Sets the value of an input or select field

        Args:
            element (WebElement, str): Field itself or Field's xpath
            value (str): Value to be defined on the field
        """
        if isinstance(field, str):
            field = self.driver.find_element(By.XPATH, field)
        tag = field.tag_name
        if tag == 'input' or tag == "textarea":
            field.clear()
            field.send_keys(value)
        elif tag == 'select':
            valid_keys = self._get_select_options(field)

            if len(valid_keys) == 0:
                logging.warning(f"Select element '{field.get_attribute('name')}' "
                                "has no option!")
            else:
                try:
                    select = Select(field)
                    select.select_by_value(value)
                except NoSuchElementException:
                    logging.error("Tried to select an inexistent option!")
        else:
            raise Exception(f"Element informed correspond to a {tag} element. "
                            "It must to be a input or a select.")


class HomePage(WebPage):
    """
        Class for the Home Page

        Args:
            - web_driver (WebDriver):
                web driver to manipulate the web pages
    """

    def __init__(self, web_driver: WebDriver):
        super().__init__(web_driver)
        self.xpath = {
            'home': "/html/body/div/nav/div/a",
            'sign_in': "/html/body/div/nav/div/ul/li[2]/a",
            'sing_up': "/html/body/div/nav/div/ul/li[3]/a",
            'feed': {
                'title': ("/html/body/div/main/div/div[2]/div/div[1]/div[2]/div[{index}]/a/"
                          "h1"),
                'author': ("/html/body/div/main/div/div[2]/div/div[1]/div[2]/div[{index}]/d"
                           "iv/div/a"),
                'tags': ("/html/body/div/main/div/div[2]/div/div[1]/div[2]/div[{index}]/a/u"
                         "l/li[{tag_index}]/a"),
                'text': "/html/body/div/main/div/div[2]/div/div[1]/div[2]/div[{index}]/a/p",
                'read_more': ("/html/body/div/main/div/div[2]/div/div[1]/div[2]/div"
                              "[{index}]/a/span"),
                'date': ("/html/body/div/main/div/div[2]/div/div[1]/div[2]/div[{index}]/div"
                         "/div/span")
            },
            'page_number': "/html/body/div/main/div/div[2]/div/div[1]/nav/ul/li[{index}]/a"
        }

    def access_article(self, position: int):
        """
            Access article by position in the list

            Args:
                - position (int): article's position in the list
        """
        article_xpath = self.xpath['feed']['title'].format(index=str(position))
        try:
            self.driver.find_element(By.XPATH, article_xpath).click()
        except NoSuchElementException as e:
            logging.error(f"Couldn't find article at position {position}. "
                          f"Error: {e.msg}")
        return ArticlePage(self.driver)


class ArticlePage(WebPage):
    """
        Class for the Article Page

        Args:
            - web_driver (WebDriver):
                web driver to manipulate the web pages
    """

    def __init__(self, web_driver: WebDriver):
        super().__init__(web_driver)
        self.xpath = {
            'home': "/html/body/div/nav/div/a",
            'sign_in': "/html/body/div/nav/div/ul/li[2]/a",
            'sing_up': "/html/body/div/nav/div/ul/li[3]/a",
            'title': "/html/body/div/main/div/div[1]/div/h1",
            'author': "/html/body/div/main/div/div[1]/div/div/div/a",
            'tags': "/html/body/div/main/div/div[2]/div[1]/div/ul/li[{index}]",
            'text': "/html/body/div/main/div/div[2]/div[1]/div/div/p",
            'date': "/html/body/div/main/div/div[1]/div/div/div/span"
        }
        self.css_selector = {
            'text': ("div.row:nth-child(1) > div:nth-child(1) > div:nth-child(1) > "
                     "p:nth-child(1)")
        }

    def get_text(self) -> str:
        """
            Returns a tag from tag list

        Returns: (str) whole article text
        """
        try:
            return self.driver.find_element(By.CSS_SELECTOR, self.css_selector['text']).text
        except NoSuchElementException as e:
            logging.error(f"Couldn't find text. Error: {e}")
