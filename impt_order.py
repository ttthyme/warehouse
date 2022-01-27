#店铺信息导入库
import csv
import pymssql
from itertools import islice
import os
from log import logger

#链接数据库
try: 
    conn = pymssql.connect(
        server="rm-wz916727b6414lnw4ro.sqlserver.rds.aliyuncs.com",
        port = 3977,
        user='dev_lougao',
        password='i9+53Cj6uVZ',
        database='dev_lougao'
        )
    cursor = conn.cursor()
except Exception as e:
    logger.error(e)
else:
    logger.info('链接数据库成功')

cursor.execute('delete from  [dev_lougao].[dbo].[yz_order_info] where left(order_date,10)=CAST(dateadd(day,-1,GETDATE()) AS DATE)')

class impt_db:
    def impt(impt_path):
       
        #判断是否有文件
        if len(os.listdir(impt_path))==0:
            logger.error('没有文件需要导入')
        else:
        #循环写入
            for i in range(len(os.listdir(impt_path))):
                with open(impt_path+'\\'+os.listdir(impt_path)[i],newline='',encoding='utf-8') as csvfile: 
                    customer_data = csv.reader(csvfile)
                    #从表格的第二行开始导入
                    try:
                        for row in  islice(customer_data, 1, None) : 
                            #对手机号等数据去除空格
                            row=(row[0].strip(),row[44],row[31].strip(),row[33].strip(),row[24].strip(),row[23],row[25],row[26],row[27],row[28].strip(),row[6] )
                            print(row)
                            cursor.execute(
                            '''INSERT INTO dbo.yz_order_info(
                                trade_id,
	                            fenxiaoyuan,
	                            yonghunicheng,
	                            xiadanshouji,
	                            shoujianrenshouji,
	                            shoujianrenmignc,
	                            shoujianrensheng,
	                            shi,
	                            qu,
	                            dizhi,
	                            order_date ) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',row)
                    except Exception as e:
                        logger.error(e)
                    else:
                        logger.info('第'+str(i+1)+'份数据导入数据库成功')

    ###执行存储过程
    #def exec_db():
    #    try:
    #        cursor.execute(f"exec fill_in_db.[dbo].[yz_order_info]")
    #    except Exception as e:
    #        logger.error(e)
    #    else:
    #        logger.info('导入目标表成功')

        #关闭流
        conn.commit()
        cursor.close()
        conn.close()

impt_db.impt('D:\python\yz_order_download')
