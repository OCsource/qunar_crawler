import requests,time,random
from bs4 import BeautifulSoup
from python0_1.qunar_crawler.cate import qunarCateComment
from python0_1.qunar_crawler.saveToDB import DB
from python0_1.qunar_crawler.common import headMsg,allMaxPage
from python0_1.qunar_crawler.utils import logUtil

User_Agent = headMsg.UA
logger = logUtil.getLogger(1)

# 获取美食信息
# 参数：美食首页url，城市编号
def getCate(tup):
    url, city_number = tup[0], tup[1]
    operate = DB.operateDB()
    Hostreferer = {
        'User-Agent': random.choice(User_Agent),
        'Referer': 'https://www.qunar.com'
    }
    startNum = int(operate.countCate(city_number) / 10) if int(operate.countCate(city_number) / 10) != 0 else 1
    maxPage = int(allMaxPage.getMaxPage(url))
    print("以跳过" + str(startNum - 1) + "页,现在从第" + str(startNum) + "页开始")
    if maxPage:
        for num in range(startNum, maxPage + 1):
            page_url = url[:55] + str(num)
            print(page_url)
            try:
                html = requests.get(url=page_url, headers=Hostreferer, timeout=5).text
                soup = BeautifulSoup(html, "html.parser")
                all_cate = soup.find('ul', class_='list_item clrfix').find_all('li', class_='item')
                i = 0
                # 遍历一个页面内的所有美食
                for one_cate in all_cate:
                    # 处理数据
                    cate_name = one_cate.find('span', class_='cn_tit')
                    cate_name = cate_name.string if cate_name else '无'
                    star = one_cate.find('span', class_='cur_score')
                    star = star.string if star else '0'
                    # 函数处理pay,address与recommendation
                    sublistbox = one_cate.find('div', class_='sublistbox')
                    if sublistbox:
                        modules = sublistbox.find_all('dl')
                        pay,address,recommendation = getMsg(modules)
                    else:
                        pay = '无'
                        address = '无'
                        recommendation = '无'
                    # print(one_cate)
                    website = one_cate.find('a', class_='titlink')['href']
                    cate_number = website.split('-')[1][2:]
                    rank = str((num - 1) * 10 + i)
                    if not operate.findCate(cate_number):
                        operate.insertCate(city_number, cate_name, cate_number, star, rank, pay, address,recommendation)
                        qunarCateComment.getConCate(website,cate_number)
                        # 每爬完一个景点休眠一分钟以内，避免被反爬拦住
                        print("美食" + cate_number + "以爬取完毕")
                        # print("睡眠中...")
                        # time.sleep(random.random() * 30)
                        # print("睡醒了，精力充沛...")
                    else :
                        print(cate_number + " : " + "该美食已有记录")
                    i += 1
                print('第%s页已爬完，休息一下'%str(num))
                time.sleep(random.random() * 30)
                print('睡醒了继续吧')
            except:
                logger.error("爬取" + url + "失败")
            break

# 处理地址与推荐菜
# 参数：一个BeautifulSoup解析的一个小dom树
# 返回：元组，包括：人均需支付，地址，推荐菜
def getMsg(modules):
    pay = '无'
    address = '无'
    recommendation = '无'
    dictTemp = {'人　均':pay,'地　址': address, '推荐菜': recommendation}
    for module in modules:
        tempKey = module.find('dt').string
        tempVal = module.find('dd').string
        # print(tempKey,tempVal)
        dictTemp[tempKey] = tempVal
    return (dictTemp['人　均'], dictTemp['地　址'],dictTemp['推荐菜'])


