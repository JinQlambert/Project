import os
import pathlib
import contextlib

from selenium import webdriver


def fake_url(file_location):
        return pathlib.Path(
                os.path.abspath(file_location)
        ).as_uri()


@contextlib.contextmanager
def fake_login_page():
        import login
        original = login.url  # backup

        login.url = fake = fake_url('./test_resources/login.html')  # fake it!
        yield  # test run at here!
        login.url = original  # restore


@contextlib.contextmanager
def fake_driver():
        driver = webdriver.Chrome('Chromedriver')
        try:
                yield driver
        finally:
                driver.quit()  # gracefully dead


def goto_fake_page(driver, file_url):
        driver.get(fake_url(file_url))


if __name__ == "__main__":
        try:
                import pytest
        except ImportError:
                print('Install pytest: $ pip install pytest')
        else:
                pytest.main(["--no-print-logs", "--verbose"])
