import pymysql
from python0_1.qunar_crawler.utils import logUtil

class operateDB():
    # 初始化,构造函数
    def __init__(self):
        self.__dbName = 'qunar'
        self.__user = 'root'
        self.__password = '123456'
        self.__host = 'localhost'
        self.__char = 'utf8'
        self.logger = logUtil.getLogger(0)

# 城市区
    # 将城市信息插入数据库
    # 参数：城市名称和城市编号
    # 返回：无
    def insertCity(self, city_name, city_number):
        db = pymysql.connect(self.__host, self.__user, self.__password, self.__dbName, charset=self.__char)
        cs = db.cursor()
        sql = "INSERT INTO city_table(city_id, city_name, city_number) VALUES('%d', '%s', '%s');" % (0, city_name, city_number)
        try:
            cs.execute(sql)
            db.commit()
        except:
            db.rollback()
            self.logger.error(city_name + ":城市插入失败！")
        finally:
            db.close()

    # 查找数据库中的城市信息
    # 参数：城市名称
    # 返回：成功：返回一个二维元组，失败：返回false
    def searchCity(self, city_name):
        db = pymysql.connect(self.__host, self.__user, self.__password, self.__dbName, charset=self.__char)
        cs = db.cursor()
        # sql = "SELECT city_number FROM city_table WHERE city_name like '%%%s%%';"%(city_name)
        sql = "SELECT * FROM city_table WHERE city_name = '%s';"%(city_name)
        try:
            cs.execute(sql)
            result = cs.fetchall()
            return  result
        except:
            db.rollback()
            self.logger.error(city_name + ":城市查找失败")
            return False
        finally:
            db.close()

    # 查询已有城市数量
    # 参数：城市编号
    # 返回：成功：一个数字，失败：false
    def countCity(self):
        db = pymysql.connect(self.__host, self.__user, self.__password, self.__dbName, charset=self.__char)
        cs = db.cursor()
        sql = "SELECT COUNT(*) FROM city_table WHERE 1;"
        try:
            cs.execute(sql)
            result = cs.fetchall()[0][0]
            return result
        except:
            db.rollback()
            self.logger.error("数据库出错了")
            return False
        finally:
            db.close()

# 景点区
    # 将景点信息插入数据库
    # 参数：list包括城市编码（int），景点编码，景点名称，排名，评分，简介，经度，维度，建议游玩时间（除第一个为int,统一str）
    # 返回：无
    def insertScenery(self, l):
        db = pymysql.connect(self.__host, self.__user, self.__password, self.__dbName, charset=self.__char)
        cs = db.cursor()
        sql = "INSERT INTO scenery_table(city_number,scenery_number,scenery_name,ranking,grade,intro,longitude,latitude,suggest_time) VALUES('%d', '%s', '%s','%s', '%s', '%s', '%s', '%s', '%s');"\
              %(l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7], l[8])
        try:
            cs.execute(sql)
            db.commit()
        except:
            db.rollback()
            self.logger.error(l[2] + ":景点插入失败,sql语句：" + sql)
        finally:
            db.close()

    # 查询景点数据
    # 参数：景点编号
    # 返回：成功：二元元组，失败false
    def searchScenery(self, scenery_number):
        db = pymysql.connect(self.__host, self.__user, self.__password, self.__dbName, charset=self.__char)
        cs = db.cursor()
        sql = "SELECT * FROM scenery_table WHERE scenery_number = '%s';"%(scenery_number)
        try:
            cs.execute(sql)
            result = cs.fetchall()
            return result
        except:
            db.rollback()
            self.logger.error(scenery_number + ":景点查找失败")
            return False
        finally:
            db.close()

    # 查询已有景点数量
    # 参数：城市编号
    # 返回：成功：一个数字，失败：false
    def countScenery(self,city_number):
        db = pymysql.connect(self.__host, self.__user, self.__password, self.__dbName, charset=self.__char)
        cs = db.cursor()
        sql = "SELECT COUNT(*) FROM scenery_table WHERE city_number = '%d';"%(city_number)
        try:
            cs.execute(sql)
            result = cs.fetchall()[0][0]
            return result
        except:
            db.rollback()
            self.logger.error("数据库出错了")
            return False
        finally:
            db.close()

    # 添加景点评论
    # 参数：一个list，包括（景点编号，用户名，评论，评分，建议，评论时间）(str)
    # 返回：无
    def insertComment(self, l):
        db = pymysql.connect(self.__host, self.__user, self.__password, self.__dbName, charset=self.__char)
        cs = db.cursor()
        sql = "INSERT INTO scenery_comment(scenery_number,username,comment,star,suggestion,commentTime) VALUES('%s', '%s', '%s', '%s', '%s', '%s');"\
              %(l[0], l[1], l[2], l[3], l[4], l[5])
        try:
            cs.execute(sql)
            db.commit()
        except:
            db.rollback()
            self.logger.error("该语句:" + sql + "的评论插入失败")
        finally:
            db.close()

    # 获取景点评论信息
    # 参数：景点编号
    # 返回：成功：一个二元元组，失败：false
    def searchComment(self,scenery_number):
        db = pymysql.connect(self.__host, self.__user, self.__password, self.__dbName, charset=self.__char)
        cs = db.cursor()
        sql = "SELECT comment FROM scenery_comment WHERE scenery_number = '%s';" % (scenery_number)
        try:
            cs.execute(sql)
            result = cs.fetchall()
            return result
        except:
            db.rollback()
            self.logger.error("评论查找失败")
            return False
        finally:
            db.close()

# 攻略区
    # 攻略插入
    # 参数：攻略编号，计划游玩时间，花费，主题（类型都为str）
    def insertStrategy(self,strategy_number,playTime, cost, theme):
        db = pymysql.connect(self.__host, self.__user, self.__password, self.__dbName, charset=self.__char)
        cs = db.cursor()
        sql = "INSERT INTO scenery_strategy(strategy_number,playTime, cost, theme) VALUES('%s', '%s', '%s', '%s');"%(strategy_number,playTime, cost, theme)
        try:
            cs.execute(sql)
            db.commit()
        except:
            db.rollback()
            self.logger.error("该语句:" + sql + "的攻略信息插入失败")
        finally:
            db.close()

    # 查询攻略景点数
    # 返回：成功一个数字，失败false
    def getStrategyPage(self):
        db = pymysql.connect(self.__host, self.__user, self.__password, self.__dbName, charset=self.__char)
        cs = db.cursor()
        sql = "SELECT distinct strategy_number FROM strategy_scenery WHERE 1;"
        try:
            cs.execute(sql)
            result = len(cs.fetchall())
            return result
        except:
            db.rollback()
            self.logger.error("数据库出错了")
            return False
        finally:
            db.close()

    # 攻略数量查询
    # 参数:攻略编号
    # 返回：成功一个数字（统计所有攻略数），失败false
    def searchSScenery(self, strategy_number):
        db = pymysql.connect(self.__host, self.__user, self.__password, self.__dbName, charset=self.__char)
        cs = db.cursor()
        sql = "SELECT COUNT(*) FROM strategy_scenery WHERE strategy_number = '%s';" % (strategy_number)
        try:
            cs.execute(sql)
            result = cs.fetchall()[0][0]
            return result
        except:
            db.rollback()
            self.logger.error("数据库出错")
            return False
        finally:
            db.close()

    # 攻略内容插入
    # 参数：攻略编号，标题，内容，其他消息
    def insertContent(self,strategy_number, thisTitle, thisContent,otherText):
        db = pymysql.connect(self.__host, self.__user, self.__password, self.__dbName, charset=self.__char)
        cs = db.cursor()
        sql = "INSERT INTO strategy_content(strategy_number, title, content,other) VALUES('%s', '%s', '%s', '%s');" % (strategy_number, thisTitle, thisContent,otherText)
        try:
            cs.execute(sql)
            db.commit()
        except:
            db.rollback()
            self.logger.error( "该语句:" + sql + "的攻略内容插入失败")
        finally:
            db.close()

    # 攻略景点插入
    # 参数：攻略编号，景点名称
    def insertSScenery(self,strategy_number, scenery_name):
        db = pymysql.connect(self.__host, self.__user, self.__password, self.__dbName, charset=self.__char)
        cs = db.cursor()
        sql = "INSERT INTO strategy_scenery(strategy_number, scenery_name) VALUES('%s', '%s');" % (strategy_number, scenery_name)
        try:
            cs.execute(sql)
            db.commit()
        except:
            db.rollback()
            self.logger.error("该语句:" + sql + "的攻略内容插入失败")
        finally:
            db.close()

    # 查找攻略
    # 参数：攻略编号
    # 返回：成功二维元组，失败false
    def SreachStrategy(self,num):
        db = pymysql.connect(self.__host, self.__user, self.__password, self.__dbName, charset=self.__char)
        cs = db.cursor()
        sql = "SELECT COUNT(*) FROM scenery_strategy WHERE strategy_number = '%s';" % (num)
        try:
            cs.execute(sql)
            result = cs.fetchall()[0][0]
            return result
        except:
            db.rollback()
            self.logger.error("数据库出错了")
            return False
        finally:
            db.close()