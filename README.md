-----

**携程爬虫程序**
-----

函数入口：main.py

_包说明：_

logs：记录爬取数据中的出现的错误或警告

saveToDB：对数据库进行操作

common：存放一些公共使用的信息

sql：存放数据库的结构

city：爬取城市信息

util：存放工具

scenery：爬取景点信息（有一个单线程版qunarScenery.py(默认)，一个多线程版mulQunarScenery.py）

strategy：爬取景点攻略

hotel：爬取酒店

cate：爬取美食

-----

****技术栈****
-----

python基础（python3.6-x86）：建议看官方文档或者上菜鸟将python过一遍

python多线程：https://blog.csdn.net/u012206617/article/details/85321781

python爬虫基础：https://blog.csdn.net/dhaiuda/article/details/80905434

BeautifulSoup：建议看官方文档https://www.crummy.com/software/BeautifulSoup/bs4/doc/

数据库mysql：有一定基础即可，只是目前数据库数据还不算多，多了之后要可能用到数据库优化（从索引和sql上优化）

-----
**包层次结构**
-----
python0_1 ----- qunar_crawler ----- main.py

                              ----- README.md
                      
                              ----- logs ----- data_log.log
                      
                                         ----- DB_log.log
                                 
                              ----- common ----- headMsg.py
                      
                              ----- utils ----- logUtil.py
                      
                              ----- SvaeToDB ----- DB.py
                      
                              ----- city ----- qunarCity.py
                      
                              ----- scenery ----- mulQunarScenery.py
                      
                                            ----- qunarComment.py
                                    
                                            ----- qunarScenery.py
                      
                              ----- stratery ----- qunarStrategy.py
                      
                                             ----- strategyContent.py
                      
                              ----- hotel ----- 
                      
                              ----- cate ----- 
                              
 -----
 
 -----
 **依赖包**
 -----
 
 xpinyin：汉字转拼音
 
 bs4.BeautifulSoup：将页面转为dom树
 
 pymysql：python连接数据库
 
 