import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re

from sqllite_helper import SqlLiteHelper



class PondaCralwer:
  def __init__(self):
    self.sqlHelper = SqlLiteHelper()

  def saveImg(self, path, url):
    with open(path, 'wb') as handle:
      response = requests.get(url, stream=True)

      if not response.ok:
          print(response)

      for block in response.iter_content(1024):
        if not block:
            break
        handle.write(block)

  def insertShop(self, data):
    cmd = '''INSERT INTO SHOPS (name, imgUrl) VALUES ('{}', '{}')'''.format(
      data['name'], data['imgUrl'])

    res =  self.sqlHelper.execute(cmd)
    self.sqlHelper.commit()
    return self.sqlHelper.getLastId()

  def insertDrinkTitle(self, data):
    cmd = '''INSERT INTO DRINKTITLES (name, shopId) VALUES ('{}', '{}')'''.format(
      data['name'], data['shopId'])

    res =  self.sqlHelper.execute(cmd)
    self.sqlHelper.commit()
    return self.sqlHelper.getLastId()

  def inserDrink(self, data):
    cmd = '''INSERT INTO DRINKS (name, info, drinkTitleId, price) VALUES ('{}', '{}', '{}', '{}')'''.format(
      data['name'], data['info'], data['drinkTitleId'], data['price'])

    res =  self.sqlHelper.execute(cmd)
    self.sqlHelper.commit()

  def parseImg(self, url):
    data = url.split('|')
    data = data[0].split('?')
    query = '?width=400&height=300'
    res = data[0] + query
    return res

  def parsePrice(self, priceString):
    res = re.search('\d.*', priceString)
    price = res.group().split('.')
    return int(price[0])


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

    img = browser.find_element_by_class_name(
      "vendor-header").find_element_by_tag_name(
        'div').get_attribute('data-src-bp_400')
    # print('ii', self.parseImg(url=img))
    imgUrl = self.parseImg(url=img)

    shopName = browser.find_element_by_class_name('fn')
    print(shopName.text)
    path = 'images/{}.jpg'.format(shopName.text)
    self.saveImg(path=path, url=imgUrl)
    shopData = {
      'name': shopName.text,
      'imgUrl': path
    }
    shopId = self.insertShop(data=shopData)
    print('shopId', shopId)





    categrolyList = browser.find_elements_by_tag_name("h2")

    title = browser.find_element_by_class_name(
      'menu__list').find_elements_by_class_name(
        'dish-category-section__inner-wrapper')
    # print(title)
    for item in title:
      name = item.find_element_by_tag_name('h2')
      print(name.text)
      drinkTitleData = {
        'name': name.text,
        'shopId': shopId
      }
      print('drinkTitleData', drinkTitleData)
      drinkTitleId = self.insertDrinkTitle(data=drinkTitleData)

      xx = item.find_elements_by_class_name('item-react-root')
      for x in xx:
        price = x.find_element_by_class_name('price-tags-container').find_element_by_tag_name('span')
        priceInt = self.parsePrice(price.text)
        drinkName = x.find_element_by_tag_name('span')
        drinkInfo = x.find_element_by_class_name('dish-info').find_elements_by_css_selector('.dish-description.e-description.ingredients')
        # print('--', drinkName.text, ' ', drinkInfo.text)
        info = ''
        if len(drinkInfo) == 1:
          info = drinkInfo[0].text
        print('--', drinkName.text, ' ', info, '$$', priceInt)
        drinkData = {
          'name': drinkName.text,
          'info': info,
          'drinkTitleId': drinkTitleId,
          'price': priceInt
        }
        self.inserDrink(data=drinkData)
    self.sqlHelper.close()

        

    # print(title.get_attribute('src'))
    # shopName = title.get_attribute('alt')

   


   
    browser.close()
