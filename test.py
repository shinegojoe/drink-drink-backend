
from selenium import webdriver

from helper.uberEatCrawler import UberEatCralwer
from helper.pondaCrawler import PondaCralwer
import re


def main():
  uber = UberEatCralwer()
  uber = PondaCralwer()

  # url = 'https://www.ubereats.com/tw/kaohsiung/food-delivery/%E7%8F%8D%E7%85%AE%E4%B8%B9-%E9%AB%98%E9%9B%84%E6%96%B0%E5%A0%80%E6%B1%9F%E5%BA%97/XNI2HgNAThyum5hb-JnmuQ'
  # url = 'https://www.ubereats.com/tw/kaohsiung/food-delivery/%E4%B8%8D%E6%9C%BD%E8%8C%B6%E4%BA%8B%E6%9C%83%E7%A4%BE/bBoXLsMjSgOsIUxmDxqJMA'
  url = 'https://www.foodpanda.com.tw/en/restaurant/q4ev/cha-xian-tai-bei-nan-jing-dian'
  url = 'https://www.foodpanda.com.tw/en/restaurant/c9rz/he-bi-wen-bing-sha-ge-shi-yin-pin-gao-xiong-re-he-dian'
  url = 'https://www.foodpanda.com.tw/en/restaurant/b8qd/yday-#'
  uber.run(url)
  # browser = webdriver.Chrome()
  # browser.get("https://www.ubereats.com/tw/kaohsiung/food-delivery/%E4%B8%8D%E6%9C%BD%E8%8C%B6%E4%BA%8B%E6%9C%83%E7%A4%BE/bBoXLsMjSgOsIUxmDxqJMA")
  # categrolyList = browser.find_elements_by_tag_name("h2")

  # drinkWrapperList = browser.find_elements_by_css_selector("li ul")
  # # print('xx',xx)
  # for i, h in enumerate(categrolyList):
  #   # h2 = h.get_attribute('class')
  #   # qq = h.find_elements_by_css_selector('ul')
  #   # qqq = h.find_element_by_tag_name('h4').find_element_by_tag_name('div')
  #   # print(qqq.text)
  #   print(h.text)
  #   # item = drinkWrapperList[i]
  #   items = drinkWrapperList[i].find_elements_by_class_name('f2')
  #   for qq in items:
  #     # qqq = qq.find_element_by_tag_name('h4').find_element_by_tag_name('div')
  #     name = qq.find_element_by_tag_name('div').find_element_by_tag_name('div')
  #     xx = name.text.split()
  #     print('--', xx)


    # drinkList = item.find_elements_by_tag_name('h4')
    # for d in drinkList:
    #   name = d.find_element_by_tag_name('div')
    #   print('--' + name.text)
    
  # qqq = xx[0].find_element_by_tag_name('h4').find_element_by_tag_name('div')
  # print(qqq.text)
  # zz = browser.find_element_by_id('wrapper')
  # print(zz.get_attribute('class'))
  # browser.close()

def xx():
  p = '從 NT$125.00'
  res = re.search('\d.*', p)
  price = res.group().split('.')
  return int(price[0])

if __name__ == "__main__":
  main()
  xx()
