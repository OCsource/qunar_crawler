import random,requests
from bs4 import BeautifulSoup
from python0_1.qunar_crawler.common import headMsg
from python0_1.qunar_crawler.utils import logUtil

User_Agent = headMsg.UA
logger = logUtil.getLogger(1)

# 获取最大页面数
# 参数：对应的攻略url
# 返回：最大页面数
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