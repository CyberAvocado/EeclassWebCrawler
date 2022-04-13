from turtle import end_fill
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import tkinter as tk #tkinter=tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


def EeclassWebCrawler():
    PYTH = "chromedriver.exe" #chromedriver的檔案路徑
    driver = webdriver.Chrome(PYTH) #請selenium抓取上述鏈結
    driver.get("https://eeclass.csu.edu.tw/index/login")#易課2.0登入網址
    driver.maximize_window() #chromedriver視窗最大化
    search = driver.find_element_by_name("account")#找到元素「account」表格欄位
    search.send_keys(entry2.get())#抓取「帳號欄位」中的資料，填入網頁中的「account」表格欄位
    search1 = driver.find_element_by_name("password")#找到元素「password」表格欄位
    search1.send_keys(entry3.get())#抓取「密碼欄位」中的資料，填入網頁中的「password」表格欄位
    time.sleep(scaleExample.get())#停歇x秒，依照下方「scaleExample = tk.Scale」之數值決定
    driver.find_element_by_xpath('//*[@id="login_form"]/div[7]/div/button').click()#找到xpath=「//*[@id="login_form"]/div[7]/div/button」的按鈕並觸發
    time.sleep(1)#停歇1秒
    link = driver.find_element_by_link_text("我的首頁")#找到link_text=「我的首頁」的連結文字
    link.click()#點擊上述連結文字
    time.sleep(1)#停歇1秒
    link = driver.find_element_by_link_text(entry.get())
    link.click()
    time.sleep(1)
    link = driver.find_element_by_link_text("討論區")#找尋link_text=「討論區」的文字連結
    link.click()#點擊上述連結文字
    time.sleep(1)#停歇1秒
    link = driver.find_element_by_link_text(entry1.get())#抓取「討論區主題欄位」中的資料
    link.click()#點擊上述連結文字
    time.sleep(1.5)#停歇1.5秒
    link = driver.find_element_by_link_text("顯示先前的回應")#找到link_text=「顯示先前的回應」的連結文字
    link.click()#點擊上述連結文字
    time.sleep(1)#停歇1秒
    link = driver.find_element_by_link_text("顯示先前的回應")#找到link_text=「顯示先前的回應」的連結文字
    link.click()#點擊上述連結文字
    time.sleep(1)#停歇1秒
    link = driver.find_element_by_link_text("顯示先前的回應")#找到link_text=「顯示先前的回應」的連結文字
    link.click()#點擊上述連結文字
    time.sleep(1)#停歇1秒
    #上述指令是為了確保留言名單完整顯示
    PosterName= driver.find_elements(By.CLASS_NAME, "poster-name")#抓取CLASS_NAME=「poster-name」的標籤內容
    for PosterName in PosterName:
        print(PosterName.text)#列印名單
    #readOnlyText.insert('insert',PosterName)
    time.sleep(2)#停歇2秒
    driver.quit()#退出(關閉)chromedriver

window = tk.Tk()
window.title('易課2.0爬蟲程式')#tkinter視窗標題
window.geometry("400x500+250+150")#tkinter視窗大小

label = tk.Label(window, text = '請輸入課程')
label.pack()

# 輸入欄位
entry = tk.Entry(window,width = 20) 
entry.pack()


label1 = tk.Label(window, text = '請輸入討論區名稱')#欄位1標籤
label1.pack()

# 輸入欄位1
entry1 = tk.Entry(window,width = 20) #討論區主題欄位
entry1.pack()

label2 = tk.Label(window, text = '請輸入學號或職編')#欄位2標籤
label2.pack()

# 輸入欄位2
entry2 = tk.Entry(window,width = 15) #帳號欄位
entry2.pack()

label3 = tk.Label(window, text = '密碼')#欄位3標籤
label3.pack()

# 輸入欄位3
entry3 = tk.Entry(window,width = 15,show="*") #密碼欄位
entry3.pack()

button = ttk.Button(window, text = "確認",command = EeclassWebCrawler, bootstyle=PRIMARY) #當「確認」按鈕被點擊，執行「def EeclassWebCrawler():」中的命令
button.pack(padx=8, pady=8)

#readOnlyText = tk.Text(window, width=45, height=12) #開發中項目，原本是要讓名單顯示在此，但一直出bug
#readOnlyText.place(x=40,y=230) 

label5=tk.Label(window, text = '驗證碼輸入等待時長')#說明文字
label5.pack()

label4 = tk.Label(window, text = ['1','2','3','4','5','6','7','8','9','10','11','12','13',])
label4.pack(padx=8, pady=5)
scaleExample = tk.Scale(window,orient='horizontal',length=150,resolution=0.1,from_=2,to=13,)#驗證碼輸入等待時長滑感
scaleExample.pack()

window.mainloop()
