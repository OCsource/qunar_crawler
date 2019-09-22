import requests,random,time
from xpinyin import Pinyin
from bs4 import BeautifulSoup
from python0_1.qunar_crawler.saveToDB import DB
from python0_1.qunar_crawler.common import headMsg
from python0_1.qunar_crawler.utils import logUtil
from python0_1.qunar_crawler.scenery import qunarScenery    # 单线程版本
from python0_1.qunar_crawler.scenery import mulQunarScenery # 多线程版本
from python0_1.qunar_crawler.strategy import qunarStrategy

# 得到中国所有景点信息
# 参数：去哪了游玩景点url
def getCityURL(url):
    operate = DB.operateDB()
    Hostreferer = {
        'User-Agent': random.choice(headMsg.UA),
        'Referer': 'https://www.qunar.com'
    }
    html = requests.get(url, headers=Hostreferer,timeout=5)
    soup = BeautifulSoup(html.text, 'html.parser')
    cities = soup.find('div', class_='contbox current').find_all('dl', class_='listbox')
    for cis in cities:
        cs = cis.find_all('li')
        for c in cs:
            city_detail = c.find('a', target='_blank')
            city_name = city_detail.string
            city_number = city_detail['href'].split('-')[1][2:]
            operate.insertCity(city_name, city_number)
    print('城市信息数据库创建成功' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

# 得到中国所有景点信息
# 参数：要爬取的城市名称
def getScenery(city_name):
    operate = DB.operateDB()
    result = operate.searchCity(city_name)
    if operate.countCity() and not result:
        print('没有这个城市！')
        return
    if not result:
        url = 'http://travel.qunar.com/place'
        getCityURL(url)
        result = operate.searchCity(city_name)
    city_id = result[0][0]
    city_number = result[0][2]
    if not city_number:
        logUtil.getLogger(1).error(city_name + ':没有该旅游城市信息')
    else:
        cityPinYin = "".join(Pinyin().get_pinyin(city_name).split('-'))
        # 景点网页拼接
        scnery_website = 'https://travel.qunar.com/p-cs' + city_number + "-" + cityPinYin + '-jingdian'
        qunarScenery.getScenery(scnery_website, city_id)      # 单线程版本
        # mulQunarScenery.getScenery(scnery_website, city_id)   # 多线程版本

        # 攻略网页拼接
        strategy_website = 'https://travel.qunar.com/travelbook/list/22-' + cityPinYin + '-' + str(city_number) + '/hot_heat/1.htm'
        qunarStrategy.getStrategy(strategy_website, city_name)
