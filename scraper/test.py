from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def scraper():
    if(True):
        # pr_name = request.POST.get('product_name')
        pr_name='iphone'
        ebay_url = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw='+pr_name

        # Send a GET request to the URL
        response = requests.get(ebay_url)

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        # print(soup)
        # Find all the products on the page
        products = soup.find_all('div' ,{'class' : 's-item__title'})
        product_prices = soup.find_all('span',{'class' : 's-item__price'})
        product_ratings = soup.find_all('span',{'class' : 's-item__seller-info-text'})
        # Loop through each product and print the name and price
        print(len(products),len(product_prices),len(product_ratings),"nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn")
        print("\n\n************ EBAY PRICES *************\n\n")
        pro_names = []
        for product in products:
            product_name = product.span.text.strip()
            pro_names.append(product_name)

        pro_prices = []
        x=-1
        for price in product_prices:
            p_price = fun(str(price))
            pro_prices.append(p_price)
            # print(f'Product Price: {p_price}')
        lent=len(pro_prices)
        for i in range(1,lent):
            print('PRODUCT NAME :',pro_names[i],"\n",'PRODUCT PRICE :',pro_prices[i])
            product_rating = product_ratings[x].text.strip()
            x+=1
            print(f'PRODUCT RATING: {product_rating}','\n')
        print("\n\n************ FLIPKART PRICES *************\n\n")
        flipkart(pr_name)
        # return render(request,'success.html')
    # else:est,'index.html')
def fun(str):
    a=''
    flag = True
    str=str[29:]
    for x in range(len(str)):
        i=str[x]
        if(ord(i)-48>=0 and ord(i)-48<=9):
            a+=i
        else:
            break
    x=int(a)*80+2400
    k='RS '+'%s'%x
    return k

def flipkart(pr_name):
    flipkart_url = 'https://www.flipkart.com/search?q='+pr_name

    # Send a GET request to the URL
    response = requests.get(flipkart_url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the products on the page
    products = soup.find_all('div', {'class': '_2kHMtA'})
    product_ratings = soup.find_all('div', {'class': '_3LWZlK'})
    # Loop through each product and print the name and price
    i=0
    for product in products:
        product_name = product.find('div', {'class': '_4rR01T'}).text.strip()
        product_price = product.find('div', {'class': '_30jeq3 _1_WHN1'}).text.strip()
        product_rating = product_ratings[i].text.strip()
        i+=1
        print(type(product_name))
        print(f'PRODUCT NAME: {product_name}')
        print(f'PRODUCT PRICE: {product_price}')
        print(f'PRODUCT RATING: {product_rating}','\n')

scraper()

