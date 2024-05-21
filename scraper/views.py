from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# MAIN FUNCTION

def scraper(request):
    if(request.method=='POST'):
        pr_name = request.POST.get('product_name')

        # ebay function
        ebay_list = ebay(pr_name)

        # print(ebay_list)
        # flipkart function
        flipkart_list = flipkart(pr_name)
        # print(flipkart_list)

        context = {'name' : pr_name , 'flipkart' :flipkart_list , 'ebay' : ebay_list}

        return render(request,'success.html',context)
    else:
        return render(request,'index.html')
    


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
    flipkart_list = []
    for product in products:
        product_name = product.find('div', {'class': '_4rR01T'}).text.strip()
        product_price = product.find('div', {'class': '_30jeq3 _1_WHN1'}).text.strip()
        product_rating = product_ratings[i].text.strip()
        i+=1
        # print(type(product_name))

        pr_list = [product_name,product_price,product_rating]
        flipkart_list.append(pr_list)

    return flipkart_list


def ebay(pr_name):
    # construct url using the product name
    ebay_url = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw='+pr_name

    # Send a GET request to the URL
    response = requests.get(ebay_url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the products on the page
    products = soup.find_all('div' ,{'class' : 's-item__title'})
    product_prices = soup.find_all('span',{'class' : 's-item__price'})
    product_ratings = soup.find_all('span',{'class' : 's-item__seller-info-text'})
    
    ebay_list = []

    lent = min(len(products),len(product_prices),len(product_ratings))
    
    for i in range(1,lent):
        product_name = products[i].span.text.strip()
        product_price = fun(str(product_prices[i]))
        product_rating = product_ratings[i].text.strip()

        temp_list = [product_name,product_price,str(product_rating)]
        ebay_list.append(temp_list)
    return ebay_list

