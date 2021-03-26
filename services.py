class Service:
  def __init__(self):
    user_handles = self.readJson('/content/drive/MyDrive/dataset/codeforces/users.json')
    self.user_handles = user_handles['users']
    self.names = self.convertNamesToList('/content/drive/MyDrive/dataset/ENGivenFemale.json')
    print('here am i ')

  
  def convertNamesToList(self,url):
    data = readJson(url)
    names = []
    for name in data:
      names.append(name['name'])
    return names

  def generateNewName(self,name):
    seed = random.randint(1,4)
    added = ''
    for i in range(seed):
      added+=str(random.randint(1,9))
    return name + added
  

  def writeJson(self,data, filename='data.json'): 
    with open(filename,'w') as f: 
        json.dump(data, f, indent=4) 
      

  def readJson(self,filename):
    f = open(filename,)
    data = json.load(f)
    return data

  
  def createUsers(self,numberOfUser):
    for i in range(numberOfUser):
      mohaml = Mohmal()
      codeforces_driver = Codeforces()
      email = mohaml.get_email()
      name = codeforces_driver.register_account(email)
      time.sleep(10)
      mohaml.refresh_page()
      time.sleep(3)
      unseenTable = mohaml.get_unseen_messages()
      mohaml.switch_to_content(unseenTable,0)
      codeforcesLink = mohaml.driver.find_element_by_partial_link_text('codeforces')
      codeforcesLink.click()

