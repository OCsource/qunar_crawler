import requests,random,time,re
from bs4 import BeautifulSoup
from python0_1.qunar_crawler.saveToDB import DB
from python0_1.qunar_crawler.common import headMsg
from python0_1.qunar_crawler.utils import logUtil

User_Agent = headMsg.UA
logger = logUtil.getLogger(1)

# 将攻略内容爬取
# 参数：相应的攻略url，攻略编号
def getStrategyContent(url,strategy_number):
    operate = DB.operateDB()
    Hostreferer = {
        'User-Agent': random.choice(User_Agent),
        'Referer': 'https://www.qunar.com'
    }
    html = requests.get(url=url,headers=Hostreferer,timeout=5).text
    soup = BeautifulSoup(html, "html.parser")
    try:
        # print(url)
        # 爬取每个攻略页面的内容
        box = soup.find('div', class_='container main-container')
        strategy_att = box.find('ul', class_='foreword_list')
        playTime = strategy_att.find('li', class_='f_item howlong')
        playTime = playTime.find('span', class_='data') if playTime != None else None
        playTime = playTime.string if playTime != None else 0
        cost = strategy_att.find('li', class_='f_item howmuch')
        cost = cost.find('span', class_='data').string if cost != None else 0
        theme = strategy_att.find('li', class_='f_item how')
        theme = theme.find('span', class_='data') if theme != None else None
        theme = list(theme.stripped_strings) if theme != None else '没有玩法'
        theme = " ".join(theme)
        # print(strategy_number,playTime, cost, theme)
        operate.insertStrategy(strategy_number,playTime, cost, theme)
        content = box.find('div', class_='b_panel_schedule')
        cd = re.compile('day-\d+')
        others = content.find_all('div', id=cd)
        # print(others)
        if others:
            for other in others:   # 对每一个大标题循环
                otherText = other.find('div', class_='text')
                otherText = otherText.string if otherText != None else '没有特别介绍'
                allRound = other.find_all('div', class_='b_poi_info b_poi_item')
                if allRound == None:
                    continue
                for roud in allRound:  # 对每一个小标题循环
                    thisTitle = roud.find('div',class_='b_poi_title_box')
                    thisTitle = thisTitle.string if thisTitle != None else '没有标题'
                    thisContent = roud.find('div', class_='text js_memo_node')
                    thisContent = list(thisContent.stripped_strings) if thisContent != None else []
                    thisContent = '，'.join(thisContent)
                    # print(strategy_number, thisTitle, thisContent,otherText)
                    operate.insertContent(strategy_number, thisTitle, thisContent,otherText)
        else:
            print('不存在这个攻略！')
    except:
        logger.error("攻略代码" + strategy_number + "估计爬太多了，要求验证了,跳过")

# 新建一个只爬取攻略景点的函数
# 参数：相应的攻略url，攻略编号
def getSceneryOnly(url,strategy_number):
    operate = DB.operateDB()
    Hostreferer = {
        'User-Agent': random.choice(User_Agent),
        'Referer': 'https://www.qunar.com'
    }
    html = requests.get(url=url, headers=Hostreferer, timeout=5).text
    soup = BeautifulSoup(html, "html.parser")
    try:
        allTitle = soup.find_all('div', class_='b_poi_info b_poi_item')
        for title in allTitle:
            titleBox = title.find('div', class_='b_poi_title_box')
            scenery = titleBox.find('a') if titleBox else None
            if scenery == None: continue
            scenery_name = titleBox.string if titleBox else None
            if scenery_name == None: continue
            operate.insertSScenery(strategy_number, scenery_name)
    except:
        print("攻略编码" + strategy_number + "估计爬太多了，要求验证了,跳过\t" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

# if __name__ == '__main__':
    #     url = 'https://travel.qunar.com/youji/7070721'
#     num = '7070721'
#     get_Comment(url, num)