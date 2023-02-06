from fastapi import FastAPI
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import uvicorn
import smtplib

app = FastAPI()


@app.get("/")
def nas100api():
    div_classes = {'open': "js-symbol-open",
                   'volume': "js-symbol-volume",
                   'daily low': "js-symbol-header__range-price-l",
                   'daily high': "js-symbol-header__range-price-r"}

    base_url = 'https://www.tradingview.com/symbols/OANDA-NAS100USD/'
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    data = {}
    try:
        driver.get(base_url)
        WebDriverWait(driver, 30)

        header_container = driver.find_element(By.CLASS_NAME, 'js-header-fundamentals')
        for key, val in div_classes.items():
            element = header_container.find_element(By.CLASS_NAME, val)
            data[key] = element.text
            print("Great!!!!!")
        result = "Open: {}\nVolume: {}\nDaily low: {}\nDaily high: {}".format(
            data.get("open", ""), 
            data.get("volume", ""), 
            data.get("daily low", ""), 
            data.get("daily high", ""))
        
        smt = smtplib.SMTP('smtp.gmail.com', 587)
        smt.ehlo()
        smt.starttls()
        smt.login('rttteddy@gmail.com', 'fhaldaiuqtzzkmhh')
        smt.sendmail('rttteddy@gmail.com',
                        'rttteddy@gmail.com',
                        f'Subject: TradeMavericks Price Notification!!!!!\n\nNASDAQ100 Price List\n\n{result}')
        smt.quit()
            # print(data)

    except Exception as e:
        print(e)
    finally:
        driver.close()
    return "Delivered to Teddy"

@app.get("/us30")
def us30api():
    div_classes = {'open': "js-symbol-open",
                   'volume': "js-symbol-volume",
                   'daily low': "js-symbol-header__range-price-l",
                   'daily high': "js-symbol-header__range-price-r"}

    base_url = 'https://www.tradingview.com/symbols/OANDA-US30USD/'
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    data = {}
    try:
        driver.get(base_url)
        WebDriverWait(driver, 30)

        header_container = driver.find_element(By.CLASS_NAME, 'js-header-fundamentals')
        for key, val in div_classes.items():
            element = header_container.find_element(By.CLASS_NAME, val)
            data[key] = element.text
            print("Great!!!!!")
        result = "Open: {}\nVolume: {}\nDaily low: {}\nDaily high: {}".format(
            data.get("open", ""), 
            data.get("volume", ""), 
            data.get("daily low", ""), 
            data.get("daily high", ""))
        
        smt = smtplib.SMTP('smtp.gmail.com', 587)
        smt.ehlo()
        smt.starttls()
        smt.login('rttteddy@gmail.com', 'fhaldaiuqtzzkmhh')
        smt.sendmail('rttteddy@gmail.com',
                        'rttteddy@gmail.com',
                        f'Subject: TradeMavericks Price Notification!!!!!\n\nUS30 Price List\n\n{result}')
        smt.quit()
            # print(data)

    except Exception as e:
        print(e)
    finally:
        driver.close()
    return "Delivered to Teddy"

@app.get("/ger30")
def ger30api():
    div_classes = {'open': "js-symbol-open",
                   'volume': "js-symbol-volume",
                   'daily low': "js-symbol-header__range-price-l",
                   'daily high': "js-symbol-header__range-price-r"}

    base_url = 'https://www.tradingview.com/symbols/GLOBALPRIME-GER30/'
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    data = {}
    try:
        driver.get(base_url)
        WebDriverWait(driver, 30)

        header_container = driver.find_element(By.CLASS_NAME, 'js-header-fundamentals')
        for key, val in div_classes.items():
            element = header_container.find_element(By.CLASS_NAME, val)
            data[key] = element.text
            print("Great!!!!!")
        result = "Open: {}\nVolume: {}\nDaily low: {}\nDaily high: {}".format(
            data.get("open", ""), 
            data.get("volume", ""), 
            data.get("daily low", ""), 
            data.get("daily high", ""))
        
        smt = smtplib.SMTP('smtp.gmail.com', 587)
        smt.ehlo()
        smt.starttls()
        smt.login('rttteddy@gmail.com', 'fhaldaiuqtzzkmhh')
        smt.sendmail('rttteddy@gmail.com',
                        'rttteddy@gmail.com',
                        f'Subject: TradeMavericks Price Notification!!!!!\n\GER30 Price List\n\n{result}')
        smt.quit()
            # print(data)

    except Exception as e:
        print(e)
    finally:
        driver.close()
    return "Delivered to Teddy"


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=7000)
