#!/usr/bin/env python3
'''
BadIdeaButtonClicker.py

Joel Goodman, 2020

@brief:
Dear Bad Idea,

Release your comics already!

Sincerely,
  a rule breaker/problem causer
'''

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep
from datetime import datetime


class ButtonClicker:
  click_count = 0
  url = "https://www.servethebutton.com/"

  def __init__(self):
    print("ButtonClicker instance created...")

  def clickTheButton(self):
    options = Options()
    options.add_argument('-headless')
    wd = webdriver.Firefox(executable_path='GeckoDriver', options=options)
    wd.get(self.url)
    the_button = wd.find_element_by_id("redButton") 
    while(True):
      try:
        the_button.click()
        self.click_count += 1
      except:
        break


def main():
  bad_idea = ButtonClicker()
  
  start_time = datetime.now()
  print(f'Bad idea button clicker STARTED at {start_time}')

  bad_idea.clickTheButton()

  stop_time = datetime.now()
  print(f'Bad Idea Button Clicker STOPPED at {stop_time}')
  print(f'Total duration = {stop_time - start_time}')
  print(f'Total clicks   = {bad_idea.click_count}')


if __name__ == "__main__":
  main()

