from selenium import webdriver
from bs4 import BeautifulSoup
import requests

browser = webdriver.PhantomJS()
browser.implicitly_wait(3)

browser.get("http://cyxso.cyworld.com/Login.sk?loginsrc=redirect&redirection=http%3A%2F%2Fwww.cyworld.com%2Fcymain")

element_id = browser.find_element_by_id("uid")
element_id.clear()
element_id.send_keys("ID")
element_pw = browser.find_element_by_id("upw")
element_pw.clear()
element_pw.send_keys("PW")

button = browser.find_element_by_css_selector("input.btn_login[type=image]")
button.submit()

browser.get("http://cy.cyworld.com/home/51979806")
browser.set_window_size(1900, 900, windowHandle='current')
browser.implicitly_wait(2)
browser.save_screenshot("Website_cy.png")

#폴더메뉴
browser.find_element_by_id("folder").click()

#다이어리 클릭
diary = browser.find_element_by_css_selector("label.menuD02")
diary.find_element_by_tag_name("input").click()

#최하위 소스 열기
browser.find_element_by_css_selector("label.menuD02").click()

#최하위 클릭
browser.find_element_by_css_selector("label.menuD03").click()

#확인 클릭
btnfind = browser.find_element_by_id("folderArea")
btnfind = btnfind.find_element_by_tag_name("button").click()
browser.save_screenshot("Website_cy5.png")

#폴더형으로 보기
browser.find_element_by_css_selector("button.typeList[type=button]").click()
browser.implicitly_wait(1)
browser.save_screenshot("Website_cy6.png")
print("구동중입니다.....")

#더보기 19번
for k in range(20):
    browser.find_element_by_css_selector("button.btnMoreView[type=button]").click()
    browser.implicitly_wait(1)
    browser.save_screenshot("Website_cy9.png")

ps = browser.page_source
soup = BeautifulSoup(ps, 'html.parser')
article = soup.select_one("#cyArticle")
article = BeautifulSoup(str(article), 'html.parser')
list_items = article.find_all('a')

#다이어리 순차 방문
print("게시글 접속 합니다.")
for subject in list_items:
    sub = BeautifulSoup(str(subject), 'html.parser')
    if sub.a['href'] == '#write':
        break
    name = sub.span.get_text()
    param = sub.a['href']
    print(sub.h3.get_Text().strip())
    print(param+"을 저장합니다.")
    browser.get('http://cy.cyworld.com'+param)
    source = browser.page_source
    fil = BeautifulSoup(source, 'html.parser')
    txt = fil.select_one('#postData > article > section > div')
    date = fil.select_one('#postData > div.postInfo > ul > li.date > p')
    
    #같은 날 작성한 일기는 뒤에 이어붙이기
    with open(str(date)[3:8]+name+".txt", mode='a+', encoding='utf-8') as f:
        f.write(str(txt))
        f.write("\n\n\n\n\n\n\n\n\n\n\n\n")
        f.close()
        print("저장완료!")

print("종료")
browser.quit()


