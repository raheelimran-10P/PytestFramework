from Window.Tests.test_base import BaseTest


class TestAwsDashboardPage(BaseTest):

    def test_01(self):
        self.driver.find_element_by_name("One").click()
        self.driver.find_element_by_name("Plus").click()
        self.driver.find_element_by_name("Seven").click()
        self.driver.find_element_by_name("Equals").click()
        self.assertEqual(self.getresults(), "8")

    def test_02(self):
        pass
