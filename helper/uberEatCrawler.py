import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from sqllite_helper import SqlLiteHelper



class UberEatCralwer:
  def __init__(self):
    pass

  def saveImg(self, path, url):
    with open(path, 'wb') as handle:
      response = requests.get(url, stream=True)

      if not response.ok:
          print(response)

      for block in response.iter_content(1024):
        if not block:
            break
        handle.write(block)

  def insertDB(self, data):
    cmd = '''INSERT INTO SHOPS (name, imgUrl) VALUES ('{}', '{}')'''.format(
      data['name'], data['imgUrl'])



    res =  self.sqlHelper.execute(cmd)


    self.sqlHelper.commit()


  def run(self, url):
    # option = webdriver.ChromeOptions()
    # option.add_argument('headless')

    # browser = webdriver.Chrome(chrome_options=option)
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')


    browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver', chrome_options=chrome_options)

    browser.get(url)
    categrolyList = browser.find_elements_by_tag_name("h2")

    title = browser.find_element_by_tag_name('figure').find_element_by_tag_name("img")
    # print(title.get_attribute('src'))
    shopName = title.get_attribute('alt')

    imgUrl = title.get_attribute('src')
    path = 'images/{}.jpg'.format(shopName)
    self.saveImg(path=path, url=imgUrl)
    # print(title.get_attribute('alt'))


    drinkWrapperList = browser.find_elements_by_css_selector("li ul")
    for i, h in enumerate(categrolyList):
      print(h.text)
      # item = drinkWrapperList[i]
      items = drinkWrapperList[i].find_elements_by_class_name('f9')
      # print(items)
      for qq in items:
        # print(qq)
        # qqq = qq.find_element_by_tag_name('h4').find_element_by_tag_name('div')
        name = qq.find_element_by_tag_name('div').find_element_by_tag_name('div')
        xx = name.text.split()
        print('--', 'name:',xx)
        # if len(xx) == 3:
        #   print('--', 'name:',xx[0], 'info:', xx[1], 'price', xx[2])
        # else:
        #   print('--', 'name:',xx[0], 'price', xx[1])
    browser.close()
