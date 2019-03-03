class HomePage:
    def __init__(self,driver):
        self.driver=driver
        self.logout_link_xpath="//*[text()='Logout']"

    def click_on_logout(self):
        self.driver.find_element_by_xpath(self.logout_link_xpath).click()