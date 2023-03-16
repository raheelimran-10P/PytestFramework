import time


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_web_element_from_dict_if_it_is(self, element_to_check_for_dict):
        if type(element_to_check_for_dict) is dict:
            first_element_value = list(element_to_check_for_dict.values())[0]
            element_to_check_for_dict = self.driver.create_web_element(element_id=first_element_value)
        return element_to_check_for_dict

    def do_click(self, by, value):
        self.get_web_element_from_dict_if_it_is(self.driver.find_element(by=by, value=value)).click()

    def wait(self, number_of_seconds=3):
        time.sleep(number_of_seconds)
