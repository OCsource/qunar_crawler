import requests,time,random
from bs4 import BeautifulSoup
from python0_1.qunar_crawler.saveToDB import DB
from python0_1.qunar_crawler.common import headMsg,allMaxPage
from python0_1.qunar_crawler.utils import logUtil

User_Agent = headMsg.UA
logger = logUtil.getLogger(1)

# 获取美食评论
# 参数，每个美食对应的url，美食编号
def getConCate(url,cate_number):
    operate = DB.operateDB()
    Hostreferer = {
        'User-Agent': random.choice(User_Agent),
        'Referer': 'https://www.qunar.com'
    }
    try:
        maxPage = allMaxPage.getMaxPage(url)
        for num in range(1, maxPage + 1):
            website = url + '-1-' + str(num)
            print(website)
            html = requests.get(url=website, headers=Hostreferer, timeout=5).text
            soup2 = BeautifulSoup(html, "html.parser")
            comment_place = soup2.find('div', class_='b_detail_section b_detail_comment')
            if comment_place:
                comment_all = comment_place.find_all('li', class_='e_comment_item clrfix')
                # print(comment_all)
                for comment_one in comment_all:
                    # print(comment_one)
                    username = comment_one.find('div', class_='e_comment_usr_name').find('a')
                    username = username.string if username else '无'
                    title = comment_one.find('div', class_='e_comment_title').find('a')
                    title = title.string if title else '无'
                    star = comment_one.find('span', class_='total_star').find('span')
                    star = star['class'][1][5:] if star else 0
                    comment_pre = comment_one.find('div', class_='e_comment_content')
                    # print(comment_pre)
                    if comment_pre:
                        if comment_pre.find('a', class_='seeMore'):
                            # 进入个人页面爬取评论
                            presonUrl = comment_pre.find('a', class_='seeMore')['href']
                            comment = getComment(presonUrl)
                        else:
                            comment = list(comment_pre.stripped_strings)
                            comment = ','.join(comment)
                    else:
                        comment = '无'
                    operate.insertConCate(cate_number, username,star, title, comment)
            else:
                print('该美食店没有评论！，跳过')
                return -2
    except:
        logger.error("爬取" + url + "失败")

# 获取个人页面内的评论
# 个人页面对应的url
# 成功：返回评论内容，失败''
def getComment(url):
    Hostreferer = {
        'User-Agent': random.choice(User_Agent),
        'Referer': 'https://www.qunar.com'
    }
    try:
        html = requests.get(url=url, headers=Hostreferer, timeout=5).text
        soup = BeautifulSoup(html, "html.parser")
        comment = soup.find('div', class_='e_comment_content_box').find('div', class_='comment_content')
        comment = list(comment.stripped_strings) if comment else '无'
        comment = ','.join(comment)
        return comment
    except:
        logger.error(url + '个人页面的美食评论爬取错误')
        return ''
