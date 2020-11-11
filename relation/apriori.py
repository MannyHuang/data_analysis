from efficient_apriori import apriori
from lxml import etree
import time
from selenium import webdriver
import csv
import pandas as pd

# driver = webdriver.Chrome()

director = u'管虎'
file_name = './' + director + '.csv'
# base_url = 'https://movie.douban.com/subject_search?search_text='+director+'&cat=1002&start='
# out = open(file_name, 'w', newline='', encoding='utf-8-sig')
# csv_write = csv.writer(out, dialect='excel')
# flags = []

# def download(required_url):
#   driver.get(required_url)
#   time.sleep(1)
#   ## 获得整个文档的html
#   html = driver.find_element_by_xpath('//*').get_attribute('outerHTML')
#   ## 解析网页结构
#   html = etree.HTML(html)

#  # 设置电影名称，导演演员 的XPATH
#   movie_lists = html.xpath("/html/body/div[@id='wrapper']/div[@id='root']/div[1]//div[@class='item-root']/div[@class='detail']/div[@class='title']/a[@class='title-text']")
#   name_lists = html.xpath("/html/body/div[@id='wrapper']/div[@id='root']/div[1]//div[@class='item-root']/div[@class='detail']/div[@class='meta abstract_2']")
#   num = len(movie_lists)
#   if num > 15:
#     movie_lists = movie_lists[1:]
#     name_lists = name_lists[1:]

#   for (movie, name_list) in zip(movie_lists, name_lists):
#     if name_list.text is None:
#       continue
#     print(name_list.text)
#     names = name_list.text.split('/')

#     if names[0].strip() == director and movie.text not in flags:
#       names[0] = movie.text
#       flags.append(movie.text)
#       csv_write.writerow(names)

#   print('ok')
#   print(num)

#   if num >= 14:
#     return True
#   else:
#     return False

# start = 0
# while start < 10000:
#   request_url = base_url + str(start)
#   flag = download(request_url)
#   if flag:
#     start = start + 15
#   else:
#     break
# out.close()
# print('finished')


lists = pd.read_csv(director+'.csv', encoding='utf-8-sig')

data = lists.values.tolist()


itemsets, rules = apriori(data, min_support=0.5, min_confidence=0.1)
print(itemsets)
print(rules)