import pytest

from test import fake_driver, fake_login_page, goto_fake_page

def test_RealEvent():
        with fake_driver() as driver:
                with fake_login_page():
                        from attendance import RealEvent
                        RealEvent(driver, 'hello', 'test')


@pytest.mark.skip(reason='No AttendanceList Page Currently.')
def test_GetAttendance():
        with fake_driver() as driver:
                goto_fake_page(driver, './test_resources/attendance_clicked.html')

                from attendance import GetAttendance
                GetAttendance(driver)
