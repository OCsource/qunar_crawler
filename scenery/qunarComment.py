import requests,random,time
from bs4 import BeautifulSoup
from python0_1.qunar_crawler.saveToDB import DB
from python0_1.qunar_crawler.common import headMsg
from python0_1.qunar_crawler.utils import logUtil

User_Agent = headMsg.UA
logger = logUtil.getLogger(1)

# 获取景点内的最大页数和地址
# 参数：list 包括：一个景点的url，景点的编码，以及上一页面的部分景点信息
def getPageURL(li): # 我妥协了，因为线程池的参数只能为一个，只好将本来的三个参数放到一个list里了
    url = li[0]
    scenery_number = li[1]
    l = li[2]
    operate = DB.operateDB()
    Hostreferer = {
        'User-Agent': random.choice(User_Agent),
        'Referer': 'https://www.qunar.com'
    }
    # proxies = {"http": "http://" + IP, "https": "http://" + IP}  # 代理ip
    rank = '?rank=0'
    try:
        html = requests.get(url=url, headers=Hostreferer,timeout=5).text
        soup = BeautifulSoup(html, "html.parser")
        msgsURL = soup.find('div', class_='b_paging').find_all('a', class_='page')
        suggestTime = soup.find('div', class_='e_focus_txtbox').find('div', class_='time')
        suggestTime = suggestTime.string if suggestTime else '没有建议游玩时间'
        suggestTime = (suggestTime.split('：')[1]).replace('小时', '')
        suggestTime = suggestTime.replace('天', ' * 24')
        l.append(suggestTime)
        operate.insertScenery(l)
        if msgsURL:
            maxPage = msgsURL[-2].string
            msgURL = msgsURL[0]['href'][:-13]
        else:
            msgURL = None
            maxPage = None
        if msgURL:
            for num in range(1, int(maxPage) + 1):
                comment_url = msgURL + str(num) + rank
                getComment(comment_url,scenery_number)
    except:
        logger.error('爬取' + url + '失败')

# 将景点评论爬取
def getComment(url,scenery_number):
    operate = DB.operateDB()
    Hostreferer = {
        'User-Agent': random.choice(User_Agent),
        'Referer': 'https://www.qunar.com'
    }
    html = requests.get(url=url,headers=Hostreferer,timeout=5).text
    soup = BeautifulSoup(html, "html.parser")
    try:
        box = soup.find('div', class_='b_detail_section b_detail_comment')
        msgs = box.find_all('li', class_='e_comment_item clrfix')
        if msgs:
            for msg in msgs:
                # ll 存储景点评论信息
                ll = []
                # 查看相应的元素，经数据获取
                username = msg.find('div', class_='e_comment_usr_name').find('a', target='_blank')
                username = username.string if username else "携程用户"   #你没有看错，就是携程用户
                star = msg.find('div', class_='e_comment_star_box').find('span', class_='total_star').find('span')
                star = star['class'][1].split('_')[1] if star else "没有评星"
                suggestion = msg.find('div', class_='e_comment_title').find('a', target='_blank')
                suggestion = suggestion.string if suggestion else "没有建议"
                comment = msg.find('div', class_='e_comment_content')
                commentFlag = 1 if comment.find('a', class_='seeMore') else 0
                if commentFlag == 1:
                    commentURL = comment.find('a', class_='seeMore')['href']
                    comment = getOneAll(commentURL)
                else:
                    comment = list(comment.stripped_strings) if comment else "没有评论"
                    comment = "".join(comment)
                commentTime = msg.find('div', class_='e_comment_add_info').find('li')
                commentTime = list(commentTime.stripped_strings)[0] if commentTime else "没有注明时间"
                # 拼接景点评论信息，存入数据库
                ll.append(scenery_number)
                ll.append(username)
                ll.append(comment)
                ll.append(star)
                ll.append(suggestion)
                ll.append(commentTime)
                operate.insertComment(ll)
                time.sleep(1 * random.random())
        else:
            print('没有评论')
    except:
        logger.error('城市代码' + scenery_number + '估计爬太多了，要求验证，跳过')

# 当爬取评论时有获取所有评论时进去个人空间爬取所有评论
def getOneAll(url):
    Hostreferer = {
        'User-Agent': random.choice(User_Agent),
        'Referer': 'https://www.qunar.com'
    }
    try:
        html = requests.get(url=url, headers=Hostreferer, timeout=5).text
        soup = BeautifulSoup(html, "html.parser")
        comment = soup.find('div', class_='e_comment_content_box').find('div', class_='comment_content')
        comment = list(comment.stripped_strings) if comment else "没有评论"
        comment = "".join(comment)
        return comment
    except:
        logger.error(url + '进入个人空间爬取失败！')
