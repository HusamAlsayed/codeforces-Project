import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class Codeforces:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome('chromedriver',options=chrome_options)
        driver.get('https://codeforces.com/register')
        self.driver = driver
        self.endpoint = 'https://codeforces.com/api/'

    def get_user_status(self, user_handle, from_=1, count=1000000):

        url = self.endpoint + 'user.status?handle={}&from={}&count={}'
        url = url.format(user_handle, from_, count)
        data = requests.get(url)
        return data.json()

    def get_user_history_rating(self, user_handle):

        url = self.endpoint + 'user.rating?handle={}'
        url = url.format(user_handle)
        data = requests.get(url)
        return data.json()

    def get_user_information(self, user_handle):

        url = self.endpoint + 'user.info?handles={}'
        url = url.format(user_handle)
        data = requests.get(url)
        return data.json()

    def get_user_blog_entries(self, user_handle):

        url = self.endpoint + 'user.blogEntries?handle={}'
        url = url.format(user_handle)
        data = requests.get(url)
        return data.json()

    def get_problemset(self):

        url = self.endpoint + 'problemset.problems'
        data = requests.get(url)
        return data.json()

    def get_contest_submission(self, contest_id, from_=1, count=1000000):

        url = self.endpoint + 'contest.status?contestId={}&from={}&count={}'
        url = url.format(contest_id, from_, count)
        data = requests.get(url)
        return data.json()

    def get_contest_standing(self, contest_id, from_, count, un_official):

        url = self.endpoint + 'contest.standings?contestId={}&from={}&count={}&showUnofficial={}'
        url = url.format(contest_id, from_, count, un_official)
        data = requests.get(url)
        return data.json()

    def get_contet_ratingchanges(self,contest_id):

        url = self.endpoint + 'contest.ratingChanges?contestId={}'
        url = url.format(contest_id)
        data = requests.get(url)
        return data.json()

    def get_contest_list(self,gym):

        url = self.endpoint + 'contest.list?gym={}'
        url = url.format(gym)
        data = requests.get(url)
        return data.json()

    def get_contest_hack(self, contest_id):

        url = self.endpoint + 'contest.hacks?contestId={}'
        url = url.format(contest_id)
        data = requests.get(url)
        return data.json()


    def register_account(self,email):
      
      all_fields = self.find_inputs()
      name = generateNewName(random.choice(names))
      print('the name', name)
      self.fields_fill(name,email,all_fields)
      self.driver.save_screenshot('beforeSubmission.png')
      register_button = self.find_registers()
      register_button.click()
      time.sleep(3)
      self.driver.save_screenshot('afterSubmission.png')
      return name


    def fill_login_data(self,username,password):
      handle_field = self.driver.find_element_by_id("handleOrEmail")
      handle_field.send_keys(username)
      password_field = self.driver.find_element_by_id("password")
      password_field.send_keys(password)
      submit = self.driver.find_element_by_class_name('submit')
      submit.click()

    
    def login_account(self,username = 'mazenalsayed',password = 'ho1234554321'):
        try:
          self.driver.get('https://codeforces.com/enter')
          self.driver.save_screenshot('log.png')
          self.fill_login_data(username,password)
          cnt = 0
          while not self.driver.get_cookie('X-User-Sha1'):
            if cnt == 10:
              break
            time.sleep(1)
            cnt += 1
        except Exception as err:
          raise NameError("Error During Login")
        self.driver.save_screenshot('after-login.png')
        user_info = {}
        try:
          x_csrf_token = Codeforces.getCsrfToken(self.driver.page_source)
          user_info['x-csrf-token'] = x_csrf_token
        except Exception as err:
          raise NameError("Error During extracting x-csrf-token")
        for i in self.driver.get_cookies():
          user_info[i['name']] = i['value']
        
        user_info['user-agent'] = self.driver.execute_script("return navigator.userAgent;")
        return user_info



    @staticmethod
    def getCsrfToken(page):
      x = re.findall(r'data-csrf=\"[a-zA-Z0-9]+\"', page)
      x_csrf_token = x[0].split("\"")[1]
      return x_csrf_token

    
    def fields_fill(self,name,email,all_fields):
      handle = name
      password = 'ho1234554321'
      confirmPassword = 'ho1234554321'
      all_fields[0].clear()
      all_fields[0].send_keys(handle)
      all_fields[1].send_keys(email)
      all_fields[2].send_keys(password)
      all_fields[3].send_keys(confirmPassword)


    def find_inputs(self):

      all_fields = []
      fields_index = [1,5,6,8]
      for index in fields_index:
        selector = '#registerForm > table > tbody > tr:nth-child(' + str(index) + ') > td:nth-child(2) > input'
        val = self.driver.find_element_by_css_selector(selector)
        all_fields.append(val)
      return all_fields


    def find_registers(self):
      register_button = self.driver.find_element_by_css_selector('#registerForm > table > tbody > tr:nth-child(9) > td > div:nth-child(1) > input')
      return register_button
