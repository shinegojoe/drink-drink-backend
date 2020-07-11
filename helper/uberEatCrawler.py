
from selenium import webdriver

class UberEatCralwer:
  def __init__(self):
    pass

  def run(self, url):
    option = webdriver.ChromeOptions()
    option.add_argument('headless')

    browser = webdriver.Chrome(chrome_options=option)
    # browser = webdriver.Chrome()
    browser.get("https://www.ubereats.com/tw/kaohsiung/food-delivery/%E4%B8%8D%E6%9C%BD%E8%8C%B6%E4%BA%8B%E6%9C%83%E7%A4%BE/bBoXLsMjSgOsIUxmDxqJMA")
    categrolyList = browser.find_elements_by_tag_name("h2")

    title = browser.find_element_by_tag_name('figure').find_element_by_tag_name("img")
    print(title.get_attribute('src'))
    print(title.get_attribute('alt'))


    # drinkWrapperList = browser.find_elements_by_css_selector("li ul")
    # for i, h in enumerate(categrolyList):
    #   print(h.text)
    #   # item = drinkWrapperList[i]
    #   items = drinkWrapperList[i].find_elements_by_class_name('f2')
    #   for qq in items:
    #     # qqq = qq.find_element_by_tag_name('h4').find_element_by_tag_name('div')
    #     name = qq.find_element_by_tag_name('div').find_element_by_tag_name('div')
    #     xx = name.text.split()
    #     # print('--', 'name:',xx[0], 'info:', xx[1], 'price', xx[2])
    #     # print('--', 'name:',xx)
    #     if len(xx) == 3:
    #       print('--', 'name:',xx[0], 'info:', xx[1], 'price', xx[2])
    #     else:
    #       print('--', 'name:',xx[0], 'price', xx[1])
    browser.close()