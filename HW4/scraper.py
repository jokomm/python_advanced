"""Using BeautifulSoup to scrape data from ordi.ee."""

from bs4 import BeautifulSoup
import requests
import json

# URL to querry
url = 'https://ordi.eu/tahvlid-ja-e-lugerid/'

#Function to scrape data from url
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
all_products = []

def get_next_page(soup):
    """Find the link for next page."""
    next_page = soup.find('a', class_="next")
    #print(next_page)
    if next_page and ('href' in next_page.attrs):
        new_url = next_page.attrs['href']
        #print(new_url)
        # Get next page and parse it wihh soup
        new_page = requests.get(new_url)
        new_soup = BeautifulSoup(new_page.text, 'html.parser')
        return new_soup
    else:
        print("Done")
        return None


def get_data(soup, all_products):
    """Function to scrape data from url."""

    tag_list = soup.find_all("div", {"class": "category-products"})
    #print(tag_list)
    for tag in tag_list:
        titles= tag.find_all("h2", {"class": "product-name"})
        #print(product_names)
        prices = tag.find_all("span", {"class": "price"})
        #print(product_price)
        images = tag.find_all("img")
        #print(product_img)

        for i in range(len(titles)):
            product_dict = {"Title": [title.text for title in titles][i],
                            "Price": [price.text.replace(u'\xa0', u' ') for price in prices][i],
                            "Picture href:": [image['src'] for image in images][i]}

            all_products.append(product_dict)

    print(all_products)
    return all_products


# Scrape all until done
while soup:
    # get all player URLs from one list page
    all_products = get_data(soup, all_products)
    # go to next list page, make new soup
    soup = get_next_page(soup)


#Write product data to a .json file
with open('data.json', 'w') as outfile:
    json.dump(all_products, outfile)
