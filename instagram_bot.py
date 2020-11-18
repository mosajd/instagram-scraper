# version 1.0
# get followers from any user id
# implementing pep8 for function names and function arguments blank spaces
from selenium import webdriver
import time
from random import randint
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# variables
# xpath link for followers popup
followers_link = '//a[@class="-nal3 "]'
followers = []


class InstagramBot:
    def __init__(self, username, password, instagram_id):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
        self.instagram_id = instagram_id

    def login(self):
        self.driver.get('https://instagram.com')
        time.sleep(4)
        user_name = self.driver.find_element_by_xpath('//input[@name="username"]')
        user_name.clear()
        user_name.send_keys(self.username)
        pass_word = self.driver.find_element_by_xpath('//input[@name="password"]')
        pass_word.clear()
        pass_word.send_keys(self.password)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        time.sleep(5)

    def discard_popup(self):
        # for get rid off from 'turn on notification' popup we can send to the following link
        # alert = self.driver.switch_to.alert
        try:
            self.driver.get(f'https://www.instagram.com/{self.instagram_id}/')
            time.sleep(5)
        except:
            self.driver.find_element_by_xpath('//button[@class="aOOlW   HoLwm "]').click()
            time.sleep(3)

    def get_followers_number(self):
        followers_number = self.driver.find_element_by_xpath\
            ('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span').get_attribute('title')
        time.sleep(3)
        print(followers_number)
        # page_down_key_repetition = int(followers_number.replace(",", "")) // 12
        # print(page_down_key_repetition)

    def open_link(self,link):
        self.link = link
        # to open the popup of followers
        self.driver.find_element_by_xpath(self.link).click()
        time.sleep(5)

    def press_tab_key(self, repetition, time_sleep):
        self.repetition = repetition
        self.time_sleep = time_sleep
        # number of times you want to press the key
        actions = ActionChains(self.driver) 
        for _ in range(self.repetition):
            actions.send_keys(Keys.TAB).perform()
            print(_)
            time.sleep(self.time_sleep)

    def press_page_down_key(self, repetition, time_sleep):
        self.repetition = repetition
        self.time_sleep = time_sleep
        # number of times you want to press the key
        page_down_actions = ActionChains(self.driver) 
        for _ in range(self.repetition):
            page_down_actions.send_keys(Keys.PAGE_DOWN).perform()
            print(_)
            time.sleep(self.time_sleep)
        
        # down_action.send_keys(Keys.ARROW_DOWN).perform()
         # time.sleep(2)
        # down_action = ActionChains(self.driver)
        # for y in range(1):
           # down_action.send_keys(Keys.PAGE_DOWN).perform()
          # time.sleep(6)
        # actions.send_keys(Keys.TAB).perform()
        # time.sleep(5)

    def collect_followers(self):
        
        for i in range(1, 30):
            temp = self.driver.find_element_by_xpath(f'/html/body/div[4]/div/div/div[2]/ul/div/li[{i}]'
                                                     f'/div/div[1]/div[2]/div[1]/span/a').get_attribute('title')
            if temp not in followers:                 
                followers.append(temp)                 
            print('%s: %s' % (i, temp))
            time.sleep(0.01)    

    def print_results(self):
        for _ in range(0, len(followers)):
            print('%s: %s' % (_+1, followers[_]))
        print("The length of followers are: ")
        print(len(followers))
        print(followers)

    def quit(self):
        self.driver.quit()
            # self.driver.execute_script('scroll(0,400)')
            # time.sleep(3)
        # followers_id = []
        # alert = self.driver.switch_to.alert
        # followers = alert.find_elements_by_xpath('//a[@class="FPmhX notranslate  _0imsa "]')
        # for i in range(len(followers)):
            # followers_id = followers[i].get_attribute('href')
        # print(len(followers_id))


test = InstagramBot("username", "password", "instagram_id")
test.login()
test.discard_popup()
test.get_followers_number()
test.open_link(followers_link)
test.press_tab_key(2, 3)
test.press_page_down_key(4, 7)
test.press_tab_key(1, 6)
test.collect_followers()
test.print_results()
test.quit()
    