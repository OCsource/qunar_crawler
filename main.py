from python0_1.qunar_crawler.city import qunarCity as qc

if __name__ == '__main__':
    city_name = input("请输入要爬取的城市名：")
    qc.getScenery(city_name)
