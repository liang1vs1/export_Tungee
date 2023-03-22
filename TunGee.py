from operator import imod
from matplotlib.pyplot import get
import pandas as pd
from selenium import webdriver
# from bs4 import BeautifulSoup
from time import sleep
import csv
from sqlalchemy import false
import wx
from wxFormCode import noname
from FileWordReplace import replace
from selenium.webdriver.chrome.options import Options
import sys
import os
import time 
from config import Graber_list,driver_path

class TG(noname.MyFrame1):
    
    def __init__(self,parent) :
        noname.MyFrame1.__init__(self,parent)
        writeTime = time.strftime("%Y%m%d", time.localtime()) 
        self.GraberList.SetItems(Graber_list)
        self.csvFilePath = f'./探迹客户{writeTime}.csv'
        self.GraberList.Selection = 0
        self.Isdone = False
        self.RerunTime = 2
        self.Rerun = False
        self.PageRuning = 1
        
    def Close(self):
        self.log('exit')
        wx.App().ExitMainLoop()
        self.log('exit sccuss')
        exit()
        
    def log(self,log_data):
        cwd = os.getcwd()
        with open(f'{cwd}/log.txt','a',encoding='UTF8') as f:
            log_time = str(time.asctime( time.localtime(time.time()) ))
            f.write(log_time+','+str(log_data)+'\n')
    
    def New_driver(self):
        options = Options()
        options.add_argument('--headless')
        # chrome_options=options,
        dr = webdriver.Chrome(executable_path=driver_path)
        dr.maximize_window()
        dr.implicitly_wait(2)
        self.dr = dr

    def LoginTunGee(self,LoginPhone,LoginPassWord):
        dr =self.dr
        LoginPhone = LoginPhone
        LoginPassWord = LoginPassWord
        userLoginBtnXpath = '//div[@role="button" and contains(text(),"账号登录")]'
        phoneInputXpath = '//input[@placeholder="请输入手机号码" ]'
        passwordInputXpath  = '//input[@placeholder="请输入密码" ]'
        TunGee = "https://user.tungee.com/users/sign-in"
        dr.get(TunGee)
        sleep(1)
        userLoginBtn = dr.find_element_by_xpath(userLoginBtnXpath)
        pInput = dr.find_element_by_xpath(phoneInputXpath)
        pwInput = dr.find_element_by_xpath(passwordInputXpath)
        LoginBtn = dr.find_element_by_tag_name('button')
        userLoginBtn.click()
        sleep(0.5)
        pInput.send_keys(LoginPhone)
        pwInput.send_keys(LoginPassWord)
        LoginBtn.click()
        
    def get_CRMList(self,graber):  
        dr =self.dr
        CRMBtnXpath = '//*[contains(text(),"探迹CRM")]'
        customerListXpath = '//*[contains(text(),"客户管理")]' 
        grabInputXpath = "//tr/th[contains(text(),'负责人范围')]/../td//input"
        grabItemCss = '.ant-cascader-menu-item-keyword'
        CRMBtn = dr.find_element_by_xpath(CRMBtnXpath)


        CRMBtn.click()
        sleep(3)
        customerList = dr.find_element_by_xpath(customerListXpath)
        customerList.click()
        
        sleep(2)
        grabInput = dr.find_element_by_xpath(grabInputXpath)
        grabInput.click()
        grabInput.send_keys(graber)
        sleep(0.05)
        grabItem = dr.find_element_by_css_selector(grabItemCss)
        grabItem.click()
        

    def run_PhoneJs(self):
        dr =self.dr
        try :
            dr.execute_script(
                """
                dList = document.querySelectorAll(".ant-table-row > td:nth-child(4) > div");
                for(i = 0;i<=dList.length;i++){dList[i].setAttribute("style","user-select: all")};
                """
            )
        except :
            pass
        try:
            dr.execute_script(
                """
                aList = document.querySelectorAll(".ant-table-row > td:nth-child(4) > div > a");
                for(i = 0;i<=aList.length;i++){aList[i].setAttribute("style","user-select: all")};
                """
            )
        except :
            pass
        try :
            dr.execute_script(
                """
                SpList = document.querySelectorAll(".ant-table-row > td:nth-child(4) > div> a > span");
                for (i = 0;i<=SpList.length;i++) {SpList[i].textContent = ""};
                """
            )
        except :
            pass
        self.log("Js done")

    def getCustomer(self):
        dr = self.dr
        CustomerNameCss = ".ant-table-row > td:nth-child(3) span"
        # CustomerNameList = [i.text for i in dr.find_elements_by_css_selector(CustomerNameCss)]
        CustomerPhoneCss = '.ant-table-row > td:nth-child(4) > div:nth-child(1)'
        # CustomerPhoneList = [i.text for i in dr.find_elements_by_css_selector(CustomerPhoneCss)]   
        CustomerPhone2Css = '.ant-table-row > td:nth-child(5) a'
        addreeCss = '.ant-table-row > td:nth-child(6) span'
        allList = []
        # 按客户行获取数据
        rowCss = 'div.ant-table-body  tbody.ant-table-tbody > tr.ant-table-row'
        rows = dr.find_elements_by_css_selector(rowCss)
        #循环行获取公司名、电话和地址
        for i in rows :
            CustomerName = i.find_element_by_css_selector(CustomerNameCss).text
            CustomerPhone = i.find_elements_by_css_selector(CustomerPhoneCss)
            CustomerAddresss = i.find_elements_by_css_selector(addreeCss)
            if len(CustomerAddresss) != 0 :
                CustomerAddress = CustomerAddresss[0].text
            else:
                CustomerAddress = ''
            if len(CustomerPhone) != 0 :
                allList.append([CustomerName,CustomerPhone[0].text,CustomerAddress])
            else :
                CustomerPhone2 = i.find_elements_by_css_selector(CustomerPhone2Css)
                if len(CustomerPhone2) != 0 :
                    cp2 =  CustomerPhone2[0].text
                    allList.append([CustomerName,cp2,CustomerAddress])
                else :
                    allList.append([CustomerName,'',CustomerAddress])
            sleep(0.1)
        return allList
        

    def click_eye(self):
        dr = self.dr
        eyeXpath = '//img[contains(@src,"ca2d2e375c4ad3baaf7c5d154e34c5a9.svg")]'
        
        eyeList = dr.find_elements_by_xpath(eyeXpath)
        
        if eyeList == [] :
            self.log("eye click done!")
        else :
            for i in eyeList :
                dr.execute_script("arguments[0].scrollIntoView();",i)
                dr.execute_script("arguments[0].click();", i)
                    
    def next_page_btn(self):
        dr = self.dr
        nextPageBtnXpath = "//*[@class=' ant-pagination-next']"
        nextPageBtn = dr.find_elements_by_xpath(nextPageBtnXpath)
        return nextPageBtn
    
    def btn_submit(self,event):
        self.UserName = str(self.UserNameInput.Value)
        self.PassWord = str(self.PassWordInput.Value)
        self.Graber = str(self.GraberList.GetStringSelection())
        # print('UserName',self.UserName)
        # print('PassWord',self.PassWord)
        print('Graber',self.Graber)
        try :
            if self.Isdone == False :
                self.done.SetLabelText("执行中")
                self.run()
            else :
                self.done.SetLabelText("完成！！！")
        except Exception as e:
            self.done.SetLabelText("执行出错，详情请查看日志")
            print(e)
            self.log(e)        

    
    def RunRoad(self):
        try :
            self.done.SetLabelText(f"执行中第{self.PageRuning}页")
            self.Rerun = False
            # 点击所有小眼睛
            self.click_eye()
            self.run_PhoneJs()
            list1 = self.getCustomer()
            print("len(list1)",len(list1))
            for i in list1:
                self.writer.writerow(i)
            self.log(f'第{self.PageRuning}页完成')
            print(f'第{self.PageRuning}页完成')
            nextPageLen =  len(self.next_page_btn())
            if nextPageLen != 0 :
                self.next_page_btn()[0].click()
                self.PageRuning += 1
            sleep(2)

            del list1
        except Exception as e:
            self.log(e)
            self.log(list1)
            self.log(f'{self.PageRuning}页需要重新获取客户列表')
            self.done.SetLabelText(f'重新获取{self.PageRuning}页')
            self.Rerun = True    
    
    def RerunRoad(self):
        while self.Rerun == True and self.RerunTime != 0 :
                self.log('正在重新获取客户列表') 
                self.RunRoad()
                self.RerunTime -= 1                       
                if self.RerunTime == 0:
                    self.Rerun == False            
                  
    def splitName(self):
        df =pd.read_csv(self.csvFilePath)
        df['is_name'] = df['电话'].str.split('：').str.get(1)
        df['姓名'] = df['is_name'].where(pd.isnull(df['is_name']),df['电话'].str.split('：').str.get(0),inplace=False)
        df['电话'] = df['电话'].where(df['电话'].str.split('：').str.len() == 1,df['电话'].str.split('：').str.get(1),inplace=False)
        df = df.drop('is_name',axis=1)
        d = df.pop('姓名')
        df.insert(1,'姓名',d)   
        df.to_csv(self.csvFilePath,index=False)
        
    def run(self):
        self.done.SetLabelText("执行中")
        dr = self.New_driver()
        LoginPhone = self.UserName
        LoginPassWord = self.PassWord
        self.LoginTunGee(LoginPhone,LoginPassWord)
        self.get_CRMList(self.Graber)
        sleep(3)
        # 创建csv
        csvfile = open(self.csvFilePath,'w',encoding='UTF8', newline='')
        self.writer = csv.writer(csvfile)
        self.writer.writerow(['公司名称','电话','地址'])
        # 需要获取列表，直到没有下一页
        
        if self.next_page_btn() == [] :
            self.RunRoad()
            if self.Rerun == True:
                self.RerunRoad()
        else:
            while self.next_page_btn() != [] :
                self.RunRoad()
                if self.Rerun == True:
                    self.RerunRoad()
                    
            #跑最后一页
            self.RunRoad()  
            if self.Rerun == True:
                    self.Rerun()      
            
                
        csvfile.close()
        self.dr.quit()
        replace(self.csvFilePath,'@','')
        self.splitName()
        self.log("all done")
        self.Isdone = True
        self.done.SetLabelText('完成')
        
        
