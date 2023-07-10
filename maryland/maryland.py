import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_binary

ZIP_ZONE = '21220'


options = webdriver.ChromeOptions()

url = "https://www.dllr.state.md.us/cgi-bin/ElectronicLicensing/OP_Search/OP_search.cgi?calling_app=HIC::HIC_business_location"
headers = {
    "Accept": "*/*",

    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
}
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")

browser = webdriver.Chrome(options=options)

try:
    browser.get(url=url)
    time.sleep(5)
    zip_inpt = browser.find_element("name", "zip")
    zip_inpt.send_keys(ZIP_ZONE)
    time.sleep(5)
    zip_inpt.send_keys(Keys.ENTER)
    page = browser.page_source
    with open(f'data/Maryland{ZIP_ZONE}.html', 'w', encoding='utf-8') as f:
        f.write(page)
    cnt = 0
    time.sleep(5)
    while True:
        button_lst = browser.find_elements("name", "Submit")
        if not button_lst:
            print('Пагинации на станице нет')
            break
        elif len(button_lst) == 1:
            if button_lst[0].get_attribute("value") == " Previous 50 ":
                print(f'Последняя страница {cnt}')
                break
            else:
                cnt += 1
                button_lst[0].click()
                page = browser.page_source
                with open(f'data/Maryland{ZIP_ZONE}-{cnt}.html', 'w', encoding='utf-8') as f:
                    f.write(page)
                print((f'save page # {cnt}'))
                time.sleep(5)
                continue
        else:
            cnt += 1
            button_lst[1].click()
            page = browser.page_source
            with open(f'data/Maryland{ZIP_ZONE}-{cnt}.html', 'w', encoding='utf-8') as f:
                f.write(page)
            print((f'save page # {cnt}'))
            time.sleep(5)
            continue
except Exception as ex:
    print(ex)
finally:
    browser.close()
    browser.quit()
