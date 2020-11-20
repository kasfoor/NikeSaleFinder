from bs4 import BeautifulSoup as soup
from selenium import webdriver
from time import sleep
import ssl
from webdriver_manager.chrome import ChromeDriverManager


def run_app():
    ssl._create_default_https_context = ssl._create_unverified_context
    my_url = "https://www.nike.com/w/sale-shoes-3yaepzy7ok"

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(my_url)

    i = 320
    while i > -1:
        driver.execute_script("window.scrollBy(0,500)","")
        sleep(.5)
        i -= 1

    print("Scrolling Done")


    #parse html
    page_html = driver.page_source
    page_soup = soup(page_html, "html.parser")

    #grab each product on page
    containers = page_soup.findAll("div", {"class": "product-card__body"})

    filename = "products.csv"
    f = open(filename,"w")

    headers = "Product Name, Price\n"
    f.write(headers)


    for container in containers:
        title_container = container.findAll("a",{"class": "product-card__link-overlay"})
        product_name = title_container[0].text

        price_container = container.findAll("div", {"class":"product-price is--current-price css-s56yt7"})
        product_price = price_container[0].text

        link_container = container.findAll("a",{"class": "product-card__link-overlay"})
        product_link = link_container[0].get("href")

        f.write(product_name + "," + product_price + "," + product_link + "\n")

    f.close()

    driver.close()

run_app()