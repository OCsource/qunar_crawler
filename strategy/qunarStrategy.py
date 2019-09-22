import requests,random,time,sys
from bs4 import BeautifulSoup
from python0_1.qunar_crawler.strategy import strategyContent
from python0_1.qunar_crawler.saveToDB import DB
from python0_1.qunar_crawler.common import headMsg
from python0_1.qunar_crawler.utils import logUtil

User_Agent = headMsg.UA
logger = logUtil.getLogger(1)

# 获取最大页面数
# 参数：对应的攻略url
def getMaxPage(url):
    Hostreferer = {
        'User-Agent': random.choice(User_Agent),
        'Referer': 'https://www.qunar.com'
    }
    try:
        html = requests.get(url=url,headers=Hostreferer,timeout=5).text
        soup = BeautifulSoup(html, "html.parser")
        maxPage = soup.find('div', class_='b_paging').find_all('a')
        maxPage = maxPage[-2].string if maxPage else 0
        return maxPage
    except:
        logger.error("爬取攻略" + url + "失败")

# 获取景点页面
# 参数：攻略页面url， 城市名称
def getStrategy(url,name):
    operate = DB.operateDB()
    Hostreferer = {
        'User-Agent': random.choice(User_Agent),
        'Referer': 'https://www.qunar.com'
    }
    maxPage = getMaxPage(url)
    # startNum = 1
    startNum = int(operate.getStrategyPage() / 10) if operate.getStrategyPage() else 1
    print('从第%s页开始'%startNum)
    if maxPage:
        # 遍历攻略所有页面
        for num in range(startNum, int(maxPage) + 1):
            page_url = url[:-5] + str(num) + '.htm'
            try:
                if num % 8 == 0:
                    print("睡眠中...")
                    time.sleep(random.random() * 100)
                    print("睡醒了，精力充沛...")
                html = requests.get(url=page_url,headers=Hostreferer,timeout=5).text
                soup = BeautifulSoup(html, "html.parser")
                all_strategy = soup.find('ul', class_='b_strategy_list ').find_all('li', class_='list_item ')
                # 遍历一个页面内的所有攻略
                for one_strategy in all_strategy:
                    # 爬取攻略景点内容
                    strategy_number = one_strategy['data-url'][7:]
                    if operate.searchSScenery(strategy_number):
                        print('攻略编号为%s的攻略以爬取，跳过'%strategy_number)
                        continue
                    place = one_strategy.find('p',class_='places')
                    places = list(place.stripped_strings)
                    place = True if place != None and name == places[-1] else False
                    if place == False:
                        continue
                    strategyContentURL = 'https://travel.qunar.com' + one_strategy['data-url']
                    strategyContent.getSceneryOnly(strategyContentURL, strategy_number)

                    # 爬取攻略所有内容
                    # strategy_number = one_strategy['data-url'][7:]
                    # if operate.SreachStrategy(strategy_number):
                    #     print('攻略编号%s的攻略以爬取，跳过'%strategy_number)
                    #     continue
                    # place = one_strategy.find('p',class_='places')
                    # places = list(place.stripped_strings)
                    # place = True if place != None and name == places[-1] else False
                    # if place == False:
                    #     continue
                    # strategyContentURL = 'https://travel.qunar.com' + one_strategy['data-url']
                    #  # print(strategyContentURL,strategyID)
                    # strategyContent.getStrategyContent(strategyContentURL,strategy_number)
                    # print('攻略%s爬取完毕'%(strategy_number))
            except:
                logger.error("攻略爬取" + page_url + "失败")