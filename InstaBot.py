'''
Find out who isnt
following you back
on Instagram

Type your username
and password in their
variables at the bottom
of the script
'''

from selenium import webdriver
from time import sleep

class InstaBot:
    def __init__(self, username, password):
        # open instagram website using selenium webdriver
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        # log into instagram
        self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]").click()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(2)

    def getUnfollowers(self):
        # open users profile
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username)).click()
        sleep(2)
        # get list of names of following
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()
        following = self.getNames()
        # get list of followers
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]").click()
        followers = self.getNames()
        # compare followers to following and print results
        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)

    def getNames(self):
        # scroll through all names
        sleep(4)
        scroll_box = self.driver.find_element_by_xpath("//div[@class='isgrP']")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        # close button
        self.driver.find_element_by_css_selector('button.wpO6b').click()
        return names


# Type your information here
username = 'USERNAME HERE'
password = 'PASSWORD HERE'

bot = InstaBot(username, password)
bot.getUnfollowers()
