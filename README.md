# Selenium Automation test 

This was a sample test automation project using the Page Object Model patter to model the [Conduit](https://realworld.svelte.dev/) website.

The idea of this project is to show Page Object principles and implementation. Much more can be built with this base.

I created a model for the Home Page model that returns an Article Page when the `access_article` is used.

The example test case `test_get_article_text.py` shows a test script that accesses the first article, and retrieves its texts to assert its initial content.

### How to run this test
1. Have chrome browser installed,
2. Have chrome webdriver for the browser version (you can get it at https://chromedriver.chromium.org/downloads)
2.1 If your system is Windows, move the webdriver to `C:/bin/`
2.2 If your system is Linux, move the webdriver to  `/usr/bin/google-chrome1`
2.3 If your system is Mac, move the webdriver to 	`/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome`
3. Install python packages:
- `python -m pip -r requirements.txt`
4. At the conduit_model directory run the tests:
- `pytest`
