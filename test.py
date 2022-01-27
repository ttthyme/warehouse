from playwright.sync_api import Playwright, sync_playwright 
import time
import datetime
import calendar
import impt_order
from log import logger


# 判断输入日期是否为月末
def is_month_lastday(anyday):
    # 获得当月1号的日期
    start_date = anyday.replace(day=1)
    # 获得当月一共有多少天（也就是最后一天的日期）
    #(a,b)格式 _, 是占位符
    _,days_in_month = calendar.monthrange(start_date.year, start_date.month)
    # 如果输入日期是月末，返回True
    if anyday.day == days_in_month:
        return True
    else:
        return False


class mainSpider:
    def run(playwright: Playwright) -> None:
        try:
            browser = playwright.chromium.launch(headless=False)
            # browser = playwright.chromium.launch_persistent_context(user_data_dir='D:\cache',headless=False,accept_downloads=True )
            context = browser.new_context(accept_downloads=True)
        except Exception as e:
            # logger.error(e)
            print(e)
        else:
            # logger.info('创建页面成功')
            pass

        # Open new page
        # page = browser.new_page()
        page = context.new_page()
        # Go to https://account.youzan.com/login 
        #第一次登录界面
        try:
            page.goto("https://account.youzan.com/login")
            #第二次登录直接跳到后台界面

            #page.goto("https://www.youzan.com/v4/shop/shop-list#/")
            # Click text=帐号登录
            page.click("text=帐号登录")

            # Click [placeholder="请输入手机号"]
            page.click("[placeholder=\"请输入手机号\"]")

            # Fill [placeholder="请输入手机号"]
            page.fill("[placeholder=\"请输入手机号\"]", "17634443739")

            # Click [placeholder="输入登录密码"]
            page.click("[placeholder=\"输入登录密码\"]")

            # Fill [placeholder="输入登录密码"]
            page.fill("[placeholder=\"输入登录密码\"]", "7ujm8ik,9ol.")
            #等待5秒
            page.wait_for_timeout(5000)

            # Check input[type="checkbox"]
            page.check("input[type=\"checkbox\"]")

            # Check :nth-match(input[type="checkbox"], 2)
            page.check(":nth-match(input[type=\"checkbox\"], 2)")

            # Click button:has-text("登 录")
            # with page.expect_navigation(url="https://www.youzan.com/v4/shop/shop-list?#/"):
            with page.expect_navigation():
                page.click("button:has-text(\"登 录\")")
        except Exception as e:
                # logger.error(e)
                print(e)
        else :
                #logger.info('登录后台成功')
                pass
        # Click text=谭飞自用好物馆总店
        #page.click("text=谭飞自用好物馆总店")
        #assert page.url == "https://www.youzan.com/v4/shop/select-store?hqKdtId=42561193&redirect=https%3A%2F%2Fstore.youzan.com%2Fv2%2Fdashboard%2Findex"

        # Click text=谭飞自用好物馆总店
        
        with page.expect_navigation(url="https://store.youzan.com/v4/dashboard"):
            with page.expect_navigation():
              page.click("text=谭飞自用好物馆总店")
        
     
        












        i=0
        for i in(0,1):
            #进入订单页面
            # Click text=订单
            # with page.expect_navigation(url="https://store.youzan.com/v2/order/query#/"):
            with page.expect_navigation():
                page.click("text=订单")
            # assert page.url == "https://store.youzan.com/v2/order/query"

            '''
            日期从当日 倒序取数
            '''

            #2020-01-01
            # time_curt=datetime.datetime.strptime('2022-02-01', '%Y-%m-%d').date()-datetime.timedelta(days=1)  # yyyy-MM-dd
            # time_curt=datetime.date.today()  # yyyy-MM-dd
            time_curt=datetime.date.today() - datetime.timedelta(days=1) #前一天的数据


       #    倒序需要先前日期框 正序需要先点击后日期框
            page.click(".zent-datepicker-trigger") #前日期框
            # page.click("div:nth-child(3) div .zent-datepicker-trigger") #后日期框
            #第一次点击需要 点击当前日期年份+月份
            page.click("text="+str(datetime.date.today().year)+"年")
            page.click("text="+str(time_curt.year)+"年")

            page.click("text="+str(datetime.date.today().month)+"月")
            page.click("text="+str(time_curt.month)+"月")

            #while True:

            # page.click(".zent-datepicker-trigger")  
            # page.click("div:nth-child(3) div .zent-datepicker-trigger")
            #如果是年末 则需要先点击今年,再点上年,再点1月,再点12月
            #if time_curt.month==12 and time_curt.day==31:
               #page.click("text="+str(datetime.date.today().year)+"年")
               #page.wait_for_timeout(1000)
               #page.click("text="+str(time_curt.year)+"年")
               #page.wait_for_timeout(1000)
               #page.click("text=1月")
               #page.wait_for_timeout(1000)
               #page.click("text=12月")
               #page.click('li[class=\"zent-datepicker-panel-body-cells_item zent-datepicker-panel-body-cells_available\"]>>div[class=\"zent-datepicker-cell-inner\"]>>text=\"'+str(time_curt.day)+'\"')   
               #page.wait_for_timeout(1000)

            #elif time_curt.month==12 :
            #    page.click('li[class=\"zent-datepicker-panel-body-cells_item zent-datepicker-panel-body-cells_available\"]>>div[class=\"zent-datepicker-cell-inner\"]>>text=\"'+str(time_curt.day)+'\"')    
            ##如果是月初 则先点击本月 再点击下月
            #elif time_curt.month>1 and time_curt.day==1:
            #    page.click("text="+str(time_curt.month-1)+"月")
            #    page.wait_for_timeout(1000)
            #    page.click("text="+str(time_curt.month)+"月")
            #    page.wait_for_timeout(1000)
            #    page.click('li[class=\"zent-datepicker-panel-body-cells_item zent-datepicker-panel-body-cells_available\"]>>div[class=\"zent-datepicker-cell-inner\"]>>text=\"'+str(time_curt.day)+'\"')
            #    page.wait_for_timeout(1000)


            ##如果是月末 则先点击本月 再点击上月
            #elif is_month_lastday(time_curt):
            #    #page.click("text="+str(datetime.date.today().month)+"月")
            #    #page.wait_for_timeout(1000)
            #    #page.click("text="+str(time_curt.month)+"月")
            #    #page.wait_for_timeout(1000)
            #    page.click('li[class=\"zent-datepicker-panel-body-cells_item zent-datepicker-panel-body-cells_available\"]>>div[class=\"zent-datepicker-cell-inner\"]>>text=\"'+str(time_curt.day)+'\"')
            #    page.wait_for_timeout(1000)

            #else :
            #    #用链式选择器选出下拉日期框的各个日期
            #    #try:
            #    #    page.click('li[class=\"zent-datepicker-panel-body-cells_item zent-datepicker-panel-body-cells_available\"]>>div[class=\"zent-datepicker-cell-inner\"]>>text=\"'+str(time_curt.day)+'\"')
            #    #except Exception as e:
            #    #    page.click('li[class=\"zent-datepicker-panel-body-cells_item zent-datepicker-panel-body-cells_available zent-datepicker-panel-body-cells_current\"]>>div[class=\"zent-datepicker-cell-inner\"]>>text=\"'+str(time_curt.day)+'\"')    
            try:
                page.click('li[class=\"zent-datepicker-panel-body-cells_item zent-datepicker-panel-body-cells_available\"]>>div[class=\"zent-datepicker-cell-inner\"]>>text=\"'+str(time_curt.day)+'\"')
            except Exception as e:
                page.click('li[class=\"zent-datepicker-panel-body-cells_item zent-datepicker-panel-body-cells_available zent-datepicker-panel-body-cells_current\"]>>div[class=\"zent-datepicker-cell-inner\"]>>text=\"'+str(time_curt.day)+'\"')    

            page.click("button:has-text(\"确定\")")

            ###################后日期框##########################################################
            page.click("div:nth-child(3) div .zent-datepicker-trigger")  #后日期框
            # page.click(".zent-datepicker-trigger")   #前日期框
            ##如果是年末 则需要先点击今年,再点上年,再点1月,再点12月
            #if time_curt.month==12 and time_curt.day==1:
                #page.click("text="+str(datetime.date.today().year)+"年")
                #page.wait_for_timeout(1000)
                #page.click("text="+str(time_curt.year)+"年")
                #page.wait_for_timeout(1000)
                #page.click("text=1月")
                #page.wait_for_timeout(1000)
                #page.click("text=12月")
                #page.wait_for_timeout(1000)
                #page.click('li[class=\"zent-datepicker-panel-body-cells_item zent-datepicker-panel-body-cells_available\"]>>div[class=\"zent-datepicker-cell-inner\"]>>text=\"'+str(time_curt.day)+'\"')
                #page.wait_for_timeout(1000)
            #elif time_curt.month==12 :
            #    page.click('div[class=\"zent-datepicker-cell-inner\"]>>text=\"'+str(time_curt.day)+'\"')           
            ##如果是月初 则先点击上月 再点击本月  
            # elif time_curt.month>1 and time_curt.day==1:
            #     page.click("text="+str(time_curt.month-1)+"月")
            #     page.wait_for_timeout(1000)
            #     page.click("text="+str(time_curt.month)+"月")
            #     page.wait_for_timeout(1000)

            ##如果是月末 则先点击本月 再点击上月
            #elif is_month_lastday(time_curt):
                #page.click("text="+str(datetime.date.today().month)+"月")
                #page.wait_for_timeout(1000)
                #page.click("text="+str(time_curt.month)+"月")
                #page.wait_for_timeout(1000)
                #page.click('li[class=\"zent-datepicker-panel-body-cells_item zent-datepicker-panel-body-cells_available\"]>>div[class=\"zent-datepicker-cell-inner\"]>>text=\"'+str(time_curt.day)+'\"')
                #page.wait_for_timeout(1000)    
    
            #else :
                #用链式选择器选出下拉日期框的各个日期
                #try:
                #    page.click('li[class=\"zent-datepicker-panel-body-cells_item zent-datepicker-panel-body-cells_available\"]>>div[class=\"zent-datepicker-cell-inner\"]>>text=\"'+str(time_curt.day)+'\"')
                #except Exception as e:
                #    page.click('li[class=\"zent-datepicker-panel-body-cells_item zent-datepicker-panel-body-cells_available zent-datepicker-panel-body-cells_current\"]>>div[class=\"zent-datepicker-cell-inner\"]>>text=\"'+str(time_curt.day)+'\"')    

            try:
                page.click('li[class=\"zent-datepicker-panel-body-cells_item zent-datepicker-panel-body-cells_available\"]>>div[class=\"zent-datepicker-cell-inner\"]>>text=\"'+str(time_curt.day)+'\"')
            except Exception as e:
                page.click('li[class=\"zent-datepicker-panel-body-cells_item zent-datepicker-panel-body-cells_available zent-datepicker-panel-body-cells_current\"]>>div[class=\"zent-datepicker-cell-inner\"]>>text=\"'+str(time_curt.day)+'\"')                
                page.wait_for_timeout(1000)
            page.click("button:has-text(\"确定\")")


            #  #导出报表
            #  page.click("button:has-text(\"导出\")")
            #  page.click("button:has-text(\"确定导出\")")
            #  #等待 30秒
            #  page.wait_for_timeout(30000)
  
            #  with page.expect_popup() as popup_info:
            #      page.click("button:has-text(\"查看报表\")")
            #  page1 = popup_info.value
  
            #  with page1.expect_download() as download_info:
            #      page1.click("button:has-text(\"下载订单报表\")")
 
            #  download = download_info.value
            #  download.save_as(r'D:\\python\\yz_order_download\\'+time_curt.strftime("%Y%m%d")+'.xlsx') 
            #  page1.wait_for_timeout(3000)
            #  page1.close()
            #  page.goto("https://store.youzan.com/v2/order/query#/")

            if i==1:
                break
            else:
                try:
                    page.goto("https://www.youzan.com/v4/shop/shop-list#/")
                except Exception as e:
                    logger.error(e)
                else:
                    logger.info('跳转到后台页面成功')    

                try:
                    with page.expect_navigation(url="https://store.youzan.com/v4/dashboard"):
                        with page.expect_navigation():
                          page.click("text=谭飞舒适职场时装总店")
                    # Click text=谭飞舒适职场时装总店
                    page.click("text=谭飞舒适职场时装总店")
                except Exception as e:
                    logger.error(e)
                else :
                    logger.info('进入谭飞舒适职场时装总店成功')
            
            #循环一次取数
            i+=1


                





if __name__ == "__main__":  
#    try:
#下载
    with sync_playwright() as playwright:
        mainSpider.run(playwright)
##解压
#        un_zip('D:\python\yz_download','D:\python\yz_extract')
##入库
    #impt_order.impt_db.impt('D:\python\yz_order_download')
#    except Exception as e:
#        logger.error(e)
#        pass
##输出日志
#    log_impt('D:\work\pyfile')
##入库完成后删除文件
    #del_file('D:\python\yz_order_download')







