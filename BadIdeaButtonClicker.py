#!/usr/bin/env python3
'''
BadIdeaButtonClicker.py

Author:
  Joel Goodman
Description:
  Fuck the police
'''

from selenium import webdriver
from time import sleep
from datetime import datetime


class ButtonClicker:
  click_count = 0
  url = "https://www.servethebutton.com/"
  def __init__(self):
    print("ButtonClicker instance created...")

  def printUrl(self):
    print(self.url);

  def clickTheButton(self):
    # This should be headless, but fuck it.
    wd = webdriver.Firefox()
    wd.get(self.url)
    the_button = wd.find_element_by_id("redButton") 
    while(True):
      try:
        the_button.click()
        self.click_count += 1
        sleep(0.000250) # Is this even necessary?
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

