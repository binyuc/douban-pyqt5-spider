import selenium.webdriver as webdriver
from lxml import etree
import random
import time
import requests
import cv2
import numpy as np
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
from loguru import logger
from PyQt5.QtCore import QThread, pyqtSignal
import re


class WorkThread(QThread):
    # 使用信号和UI主线程通讯，参数是发送信号时附带参数的数据类型，可以是str、int、list等
    finishSignal = pyqtSignal(str)
    displaySignal = pyqtSignal(str)

    # 带参数示例
    def __init__(self, username, password, url, comment, header, random_target, star, time, excel, blacklist,
                 parent=None):
        super(WorkThread, self).__init__(parent)
        self.username = username
        self.password = password
        self.url = url
        self.comment = comment
        self.header = header
        self.random_target = random_target
        self.star = star
        self.wait_time = time
        self.excel = excel
        self.blacklist = blacklist

    def open_browser(self):
        options = webdriver.FirefoxOptions()
        if self.header == '无头浏览':
            self.displaySignal.emit('不显示浏览器')
            options.add_argument('-headless')
        else:
            self.displaySignal.emit('显示浏览器')
        options.add_argument("--disable-gpu")
        self.displaySignal.emit('正在打开浏览器...')
        self.browser = webdriver.Firefox(options=options, executable_path='geckodriver.exe')
        self.browser.implicitly_wait(10)

    def close_browser(self):
        self.displaySignal.emit('正在关闭浏览器...')
        time.sleep(1)
        self.browser.quit()

    def load_account(self):
        if self.excel != '':
            path = self.excel.replace('\\', '//')
            account_list = pd.read_excel(path).to_dict(orient='records')
        elif self.username != '' and self.password != '':
            account_list = []
            temp = {}
            temp['用户名'] = self.username
            temp['密码'] = self.password
            temp['文案'] = self.comment

            account_list.append(temp)
        else:
            self.displaySignal.emit('请检查登录数据是否完整')
        return account_list

    def login_douban(self):
        url = 'https://www.douban.com/'
        self.browser.get(url)
        time.sleep(2)
        self.browser.switch_to.frame(self.browser.find_elements_by_tag_name('iframe')[0])
        switch_buttom = \
        self.browser.find_elements_by_xpath('//ul[@class="tab-start"]/li[@class="account-tab-account"]')[0]
        switch_buttom.click()
        self.displaySignal.emit('正在尝试登录...')
        input1 = self.browser.find_element_by_id('username')
        input1.clear()
        if self.username != '':
            input1.send_keys(self.username)
        else:
            input1.send_keys(self.load_username)
        input2 = self.browser.find_element_by_id('password')
        input2.clear()
        if self.password != '':
            input2.send_keys(self.password)
        else:
            input2.send_keys(self.load_password)
        bottom = self.browser.find_element_by_class_name('account-form-field-submit ')
        bottom.click()
        time.sleep(3)

    def check_login(self):
        try:
            self.account_info = self.browser.find_element_by_xpath('//a[@class="bn-more"]/span[1]').text
            self.displaySignal.emit(self.account_info)
        except Exception as e:
            self.displaySignal.emit('报错内容为:' + str(e))
            if 'Message: Browsing context has been discarded' in str(e):
                self.displaySignal.emit('浏览器异常，页面断联...')
                self.displaySignal.emit('刷新页面中...')
                self.browser.refresh()
            if 'Message: Unable to locate element:' in str(e):
                self.displaySignal.emit('尚未登录成功...遭遇验证码')
                self.switch_to_iframe()
                self.get_img()
                button = self.browser.find_element_by_id('tcaptcha_drag_thumb')
                # 拖动操作用到ActionChains类，实例化
                action = ActionChains(self.browser)
                action.click_and_hold(button).perform()
                distance = self.get_image_offset()
                # 滑动
                self.displaySignal.emit('正在滑动验证码滑块...')
                action.move_by_offset(xoffset=distance, yoffset=0).perform()
                action.reset_actions()
                time.sleep(5)

    def check_login_twice(self):
        try:
            self.browser.refresh()
            self.displaySignal.emit(self.browser.find_element_by_xpath('//a[@class="bn-more"]/span[1]').text)
            time.sleep(5)
            if '的帐号' in self.browser.find_element_by_xpath('//a[@class="bn-more"]/span[1]').text:
                status = 1
            else:
                self.displaySignal.emit('未找到登录后的账户信息')
                status = 0

        except Exception as e:
            self.displaySignal.emit('报错内容为:' + str(e))
            self.displaySignal.emit('未知错误发生！！！！请截图并联系技术员修复BUG')
            status = 0
        self.displaySignal.emit('状态为：' + str(status))
        return status

    def switch_to_iframe(self):
        self.displaySignal.emit('切换至验证码图层...')
        time.sleep(2)
        auth_frame = self.browser.find_element_by_id('tcaptcha_iframe')
        self.browser.switch_to.frame(auth_frame)

    def get_img(self):
        self.displaySignal.emit('获取背景图和滑块图的url...')
        background_image_url = self.browser.find_element_by_id('slideBg').get_attribute('src')
        slider_image_url = self.browser.find_element_by_id('slideBlock').get_attribute('src')
        return background_image_url, slider_image_url

    def download_image(self, img_url, imgname):
        self.displaySignal.emit('以流的形式下载文件...')
        image = requests.get(img_url, stream=True)
        imgName = ''.join(["./", imgname])
        with open(imgName, 'wb') as f:
            for chunk in image.iter_content(chunk_size=1024):  # 循环写入  chunk_size：每次下载的数据大小
                if chunk:
                    f.write(chunk)
                    f.flush()
            f.close()
        self.displaySignal.emit('验证码下载完成')

    def get_image_offset(self):
        back_image = 'back_image.png'  # 背景图像命名
        slider_image = 'slider_image.png'  # 滑块图像命名
        background_image_url, slider_image_url = self.get_img()
        self.download_image(background_image_url, back_image)
        self.download_image(slider_image_url, slider_image)
        # 获取图片并灰度化
        block = cv2.imread(slider_image, 0)
        template = cv2.imread(back_image, 0)
        w, h = block.shape[::-1]
        # print(w, h)
        # 二值化后图片名称
        block_name = 'block.jpg'
        template_name = 'template.jpg'
        # 保存二值化后的图片
        cv2.imwrite(block_name, block)
        cv2.imwrite(template_name, template)
        block = cv2.imread(block_name)
        block = cv2.cvtColor(block, cv2.COLOR_RGB2GRAY)
        block = abs(255 - block)
        cv2.imwrite(block_name, block)
        block = cv2.imread(block_name)
        template = cv2.imread(template_name)
        # 获取偏移量
        # 模板匹配，查找block在template中的位置，返回result是一个矩阵，是每个点的匹配结果
        result = cv2.matchTemplate(block, template, cv2.TM_CCOEFF_NORMED)
        x, y = np.unravel_index(result.argmax(), result.shape)
        #     print(x,y)
        # 由于获取到的验证码图片像素与实际的像素有差(实际：280*158 原图：680*390)，故对获取到的坐标进行处理
        offset = y * (280 / 680)
        # 画矩形圈出匹配的区域
        # 参数解释：1.原图 2.矩阵的左上点坐标 3.矩阵的右下点坐标 4.画线对应的rgb颜色 5.线的宽度
        cv2.rectangle(template, (y, x), (y + w, x + h), (7, 249, 151), 2)
        #     show(template)
        # print(offset - 23)
        return offset - 23

    def attack_random_target(self):
        if self.random_target == '随机电影':
            self.displaySignal.emit('选取随机电影中...')
            # target_url = 'https://movie.douban.com'
            target_url = 'https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&watched=on&page_limit=20&page_start=0'
        elif self.random_target == '随机电视剧':
            self.displaySignal.emit('随机电视剧中...')
            # target_url = 'https://movie.douban.com/tv'
            target_url = 'https://movie.douban.com/tv/#!type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&watched=on&page_limit=20&page_start=0'
        self.browser.get(target_url)
        time.sleep(5)
        for viewmore in range(1, 2):
            self.browser.find_element_by_xpath('//a[@class="more"]').click()
            time.sleep(1.5)
        tree = etree.HTML(self.browser.page_source)
        if self.blacklist != '':
            blacklist = self.blacklist.split(',')
            while True:
                self.random_url = random.choice(tree.xpath('//a[@class="item"]/@href'))
                douban_id = re.findall('.*subject/(.*?)/.*', self.random_url)[0]
                if douban_id in blacklist:
                    continue
                else:
                    break
        else:
            try:
                self.random_url = random.choice(tree.xpath('//a[@class="item"]/@href'))
            except Exception as e:
                self.displaySignal.emit(e)
                time.sleep(1)
                self.browser.refresh()
                time.sleep(2)
                self.random_url = random.choice(tree.xpath('//a[@class="item"]/@href'))

        self.browser.get(self.random_url)
        time.sleep(1)

    def get_target_star(self, current_rating):
        if float(current_rating) <= 2:
            target_star = 1
        elif 2 < float(current_rating) <= 4:
            target_star = 2
        elif 4 < float(current_rating) <= 6:
            target_star = 3
        elif 6 < float(current_rating) <= 8:
            target_star = 4
        elif 8 < float(current_rating) <= 10:
            target_star = 5
        self.displaySignal.emit('给予星级评分为: ' + str(target_star))
        return target_star

    def give_star(self, star):
        if star == 1:
            self.browser.find_element_by_id('star1').click()
        if star == 2:
            self.browser.find_element_by_id('star2').click()
        if star == 3:
            self.browser.find_element_by_id('star3').click()
        if star == 4:
            self.browser.find_element_by_id('star4').click()
        if star == 5:
            self.browser.find_element_by_id('star5').click()

    def give_comment(self):
        current_rating = self.browser.find_elements_by_xpath('//strong[@class="ll rating_num"]')[0].text
        self.movie_title = self.browser.find_elements_by_xpath('//div[@id="content"]/h1/span[1]')[0].text
        self.displaySignal.emit(self.movie_title)
        try:
            target_star = self.get_target_star(current_rating)
        except:
            target_star = 4
        # 点击短评
        self.browser.find_elements_by_xpath('//div[@class="mod-hd"]/a')[0].click()
        # 检查是否有评价历史
        if self.browser.find_elements_by_xpath('//textarea[@name="comment"]')[0].text == '':
            # 点击看过
            try:
                self.browser.find_element_by_xpath('//span[@class="interest-status"]/label[3]').click()
            except:
                self.browser.find_element_by_xpath('//span[@class="interest-status"]/label[2]').click()
            # 评分
            time.sleep(3)
            if self.star != '0':
                self.displaySignal.emit('正在输入指定星级...:' + str(self.star))
                self.give_star(int(self.star))
            elif self.url != '':
                self.give_star(int(self.load_star))
                self.displaySignal.emit('正在输入EXCEL指定星级...:' + str(self.load_star))
            else:
                self.give_star(target_star)
            # 输入短评
            time.sleep(3)
            comment_input = self.browser.find_element_by_id('comment')
            comment_input.clear()
            if self.comment != '':
                self.displaySignal.emit('正在输入指定评论...')
                comment_input.send_keys(self.comment)
            else:
                self.displaySignal.emit('正在输入文案库评论...')
                comment_input.send_keys(self.load_comment)
            # 提交
            time.sleep(1)
            self.browser.find_element_by_id('share-shuo').click()
            time.sleep(3)
            self.browser.find_element_by_xpath('//input[@value="保存"]').click()
            time.sleep(5)
        else:
            a_list = self.browser.find_elements_by_xpath('//div[@id="recommendations"]/div/dl/dt/a')
            self.browser.get(random.choice(a_list).get_attribute("href"))
            self.give_comment()

    def get_screenshot(self):
        self.browser.get('https://www.douban.com/mine/')
        time.sleep(1)
        self.browser.refresh()
        time.sleep(2)
        if self.load_username != '':
            filename = self.movie_title + str(self.load_username)
            self.browser.get_screenshot_as_file(r'屏幕截图\{}.png'.format(filename))
        else:
            filename = self.movie_title + str(self.username)
            self.browser.get_screenshot_as_file(r'屏幕截图\{}.png'.format(filename))
        self.displaySignal.emit(r'屏幕截图\{}.png'.format(filename))

    def get_wait(self):
        if self.wait_time != '':
            if '-' in self.wait_time:
                less_time = self.wait_time.split('-')[0]
                more_time = self.wait_time.split('-')[1]
                final_time = random.randint(int(less_time), int(more_time))
                self.displaySignal.emit('随机等待' + str(final_time))
                time.sleep(int(final_time))
        else:
            time.sleep(5)

    @logger.catch
    def run_spider(self):
        self.displaySignal.emit("---------豆瓣自动评论发布程序v1----2021.3.26----启动中---------")
        account_list = self.load_account()
        for account in account_list:
            self.load_username = account['用户名']
            self.load_password = account['密码']
            self.load_comment = account['文案']
            self.load_star = account['星级']
            self.open_browser()
            self.login_douban()
            self.check_login()
            if self.check_login_twice() == 1:
                if 'douban' not in self.url:
                    self.displaySignal.emit('无指定url，随机选取目标...')
                    self.attack_random_target()
                    self.give_comment()
                else:
                    self.displaySignal.emit('有指定url...')
                    self.browser.get(self.url)
                    # try:
                    self.give_comment()
                    # except Exception as e:
                    #     self.displaySignal.emit(str(e))
                    #     self.displaySignal.emit('请检查指定的url是否正确，是否为电影或电视剧评分页')

                self.get_wait()

                if self.username != '' or self.url != '':
                    self.get_screenshot()
            else:
                self.close_browser()
                self.displaySignal.emit('已关闭')
            self.close_browser()
        self.finishSignal.emit('end')
        return

    def run(self):
        logger.add('my_log.log', rotation="100 MB")
        self.run_spider()
