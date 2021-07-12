from selenium import webdriver
import selenium
import time
import pyimgur


CLIENT_ID = "B114815e13bb751"  # 申請 Imgur API取得ID


account = '********'
password = '****'


def R():
    driver = webdriver.Chrome(
        "C:/Users/austi/python/chromedriver")  # 本機上執行自動化模擬
    driver.get('https://bigdata.scu.edu.tw/mrb/')  # 取得R210空間租借網址
    driver.maximize_window()  # 放大螢幕
    time.sleep(2)  # 待機暫停
    driver.save_screenshot(
        "C:/Users/austi/python/spaceR.png")  # 截圖
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(
        "C:/Users/austi/python/spaceR.png", title="R210的資料")  # 將圖片上傳至imgur
    driver.quit()  # 關閉瀏覽器
    return uploaded_image.link  # return傳出連結，放在linebot圖片連結處


def space1():
    driver = webdriver.Chrome("C:/Users/austi/python/chromedriver")
    driver.get('https://booking.scu.edu.tw/booking/')
    driver.find_element_by_xpath(
        '//*[@id="loginform"]/div[2]/div/input').send_keys(account)
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="loginform"]/div[3]/div/input').send_keys(password)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="login_btn"]').click()
    driver.get('https://booking.scu.edu.tw/booking/Home')
    driver.find_element_by_xpath(
        '//*[@id="general_content"]/div[2]/p[3]/a[2]/button').click()
    driver.find_element_by_xpath('//*[@id="select_room"]').click()
    driver.find_element_by_xpath('//*[@id="select_room"]/option[2]').click()
    driver.save_screenshot("C:/Users/austi/python/space1.jpg")
    pic = Image.open("C:/Users/austi/python/space1.jpg")
    copy = pic.copy()
    newpic = copy.crop((0, 150, 929, 784))
    newpic.save('resize1.png')
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(
        "C:/Users/austi/python/resize1.jpg", title="完成室的資料")
    return uploaded_image.link


def space2():
    driver = webdriver.Chrome("C:/Users/austi/python/chromedriver")
    driver.get('https://booking.scu.edu.tw/booking/')
    driver.find_element_by_xpath(
        '//*[@id="loginform"]/div[2]/div/input').send_keys(account)
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="loginform"]/div[3]/div/input').send_keys(password)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="login_btn"]').click()
    driver.get('https://booking.scu.edu.tw/booking/Home')
    driver.find_element_by_xpath(
        '//*[@id="general_content"]/div[2]/p[3]/a[2]/button').click()
    driver.find_element_by_xpath('//*[@id="select_room"]').click()
    driver.find_element_by_xpath('//*[@id="select_room"]/option[3]').click()
    driver.save_screenshot("C:/Users/austi/python/space2.jpg")
    pic = Image.open("C:/Users/austi/python/space2.jpg")
    copy = pic.copy()
    newpic = copy.crop((0, 150, 929, 784))
    newpic.save('resize2.jpg')
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(
        "C:/Users/austi/python/resize2.jpg", title="未來室的資料")
    return uploaded_image.link


def space3():
    driver = webdriver.Chrome("C:/Users/austi/python/chromedriver")
    driver.get('https://booking.scu.edu.tw/booking/')
    driver.find_element_by_xpath(
        '//*[@id="loginform"]/div[2]/div/input').send_keys(account)
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="loginform"]/div[3]/div/input').send_keys(password)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="login_btn"]').click()
    driver.get('https://booking.scu.edu.tw/booking/Home')
    driver.find_element_by_xpath(
        '//*[@id="general_content"]/div[2]/p[3]/a[2]/button').click()
    driver.find_element_by_xpath('//*[@id="select_room"]').click()
    driver.find_element_by_xpath('//*[@id="select_room"]/option[5]').click()
    driver.save_screenshot("C:/Users/austi/python/space3.jpg")
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(
        "C:/Users/austi/python/space3.jpg", title="現在室的資料")
    return uploaded_image.link


print(R())
