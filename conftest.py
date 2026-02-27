import pytest
import allure

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.failed:
        page = item.funcargs.get("page")
        if page:
            allure.attach(
                page.screenshot(),
                name="failure",
                attachment_type=allure.attachment_type.PNG
            )