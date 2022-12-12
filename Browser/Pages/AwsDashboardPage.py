from Browser.Pages.BasePage import BasePage


class AwsDashboardPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_aws_page_title(self, title):
        return self.get_title(title)

