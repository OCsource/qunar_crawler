import requests,random,time
from bs4 import BeautifulSoup
from python0_1.qunar_crawler.scenery import qunarComment
from python0_1.qunar_crawler.saveToDB import DB
from python0_1.qunar_crawler.common import headMsg,allMaxPage
from python0_1.qunar_crawler.utils import logUtil

User_Agent = headMsg.UA
logger = logUtil.getLogger(1)

# 获取景点页面
# 参数：城市景点的url
def getScenery(tup):
    url, city_number = tup[0], tup[1]
    operate = DB.operateDB()
    Hostreferer = {
        'User-Agent': random.choice(User_Agent),
        'Referer': 'https://www.qunar.com'
    }
    startNum = int(operate.countScenery(city_number) / 10) if int(operate.countScenery(city_number) / 10) != 0 else 1
    maxPage = int(allMaxPage.getMaxPage(url))
    print("以跳过" + str(startNum - 1) + "页,现在从第" + str(startNum) + "页开始")
    if maxPage:
        # 遍历景点所有页面
        for num in range(startNum, int(maxPage) + 1):
            page_url = url + "-1-" + str(num)
            try:
                html = requests.get(url=page_url,headers=Hostreferer,timeout=5).text
                soup = BeautifulSoup(html, "html.parser")
                all_scenery = soup.find('ul', class_='list_item clrfix').find_all('li', class_='item')
                # 遍历一个页面内的所有景点
                for one_scenery in all_scenery:
                    # l 存入景点信息
                    l = []
                    # 查看相应的元素，经数据获取
                    longitude = one_scenery['data-lng'] if one_scenery['data-lng'] else 0
                    latitude = one_scenery['data-lat'] if one_scenery['data-lat'] else 0
                    title = one_scenery.find('a', class_='titlink').find('span', class_='cn_tit')
                    title = list(title.stripped_strings)[0] if title else "没有景点名"
                    website = one_scenery.find('a', class_='titlink')['href']
                    scenery_number = website.split('-')[1][2:]
                    ranking = one_scenery.find('span', class_='ranking_sum').find('span', class_='sum')
                    ranking = ranking.string if ranking != None else "没有排名"
                    grade = one_scenery.find('span', class_='total_star').find('span', class_='cur_star')['style'][6:]
                    intro = one_scenery.find('div', class_='desbox')
                    intro = intro.string if intro else "没有简介"
                    if not operate.searchScenery(scenery_number):
                        l.append(city_number)
                        l.append(scenery_number)
                        l.append(title)
                        l.append(ranking)
                        l.append(grade)
                        l.append(intro)
                        l.append(longitude)
                        l.append(latitude)
                        qunarComment.getPageURL([website, scenery_number, l])
                        # 每爬完一个景点休眠一分钟以内，避免被反爬拦住
                        print("景点" + scenery_number + "以爬取完毕")
                        print("睡眠中...")
                        time.sleep(random.random() * 60)
                        print("睡醒了，精力充沛...")
                    else :
                        print(title + " : " + "该景点已有记录")
            except:
                logger.error('content爬取' + url + '失败')