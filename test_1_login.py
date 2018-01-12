import pytest

from test import fake_driver, fake_login_page


def test_loginsequence_id_pw():
        with fake_driver() as driver:
                with fake_login_page():
                        from login import loginsequence
                        loginsequence(driver, 'hello', 'world')
                        assert 'attendance' in driver.current_url

def test_loginsequence_no_id_pw():
        with fake_driver() as driver:
                with fake_login_page():
                        from login import loginsequence
                        loginsequence(driver, '', '')
                        assert 'attendance' not in driver.current_url
