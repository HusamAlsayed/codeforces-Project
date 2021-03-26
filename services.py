import requests
from bs4 import BeautifulSoup
import json
import random
import time
import re
import glob
import concurrent.futures
import os
import mohmal
import codeforces
def convert_names_tolist(url):
  data = read_json(url)
  names = []
  for name in data:
    names.append(name['name'])
  return names


def generate_new_name():
  name = random.choice(names)
  seed = random.randint(1,4)
  added = ''
  for i in range(seed):
    added+=str(random.randint(1,9))
  return name + added


def write_json(data, filename='data.json'): 
    with open(filename,'w') as f: 
        json.dump(data, f, indent=4) 
      

def read_json(filename):
  f = open(filename,)
  data = json.load(f)
  return data

def createUsers(number_of_users):
  for i in range(number_of_users):
    mohaml = mohmal.Mohmal()
    codeforces_driver = codeforces.Codeforces()
    email = mohaml.get_email()
    name = codeforces_driver.register_account(email)
    time.sleep(10)
    mohaml.refresh_page()
    time.sleep(3)
    unseenTable = mohaml.get_unseen_messages()
    mohaml.switch_to_content(unseenTable,0)
    codeforcesLink = mohaml.driver.find_element_by_partial_link_text('codeforces')
    codeforcesLink.click()



names = convert_names_tolist('/content/drive/MyDrive/dataset/ENGivenFemale.json')

user_handles = read_json('/content/drive/MyDrive/dataset/codeforces/users.json')

user_handles = user_handles['users']


