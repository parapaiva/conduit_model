#! /usr/bin/env python3.9
"""
    This script test the New Profile page of BCC Web
"""
from model import HomePage
from driver import WebDriver
import pytest


def test_get_text():
    # Access Home Page
    driver = WebDriver(
        address="https://realworld.svelte.dev/",
        path="C:/bin/chromedriver.exe",
        maximize_window=False)
    home = HomePage(driver)

    # Access first article
    article = home.access_article(1)

    # Get text
    article_text = article.get_text()
    assert article_text.startswith("Sunt excepturi")
