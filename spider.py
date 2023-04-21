#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    spider.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: slegaris <slegaris@student.42madrid.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/18 12:57:37 by slegaris          #+#    #+#              #
#    Updated: 2023/04/21 13:36:05 by slegaris         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import urllib.request
from urllib.request import urlopen
from urllib.parse import urlparse, urljoin
import urllib
from bs4 import BeautifulSoup, SoupStrainer
import os
import argparse

parser = argparse.ArgumentParser(description='Web scraper to download images and documents')
parser.add_argument('url', type=str, help='The URL to start scraping from')
parser.add_argument('-r', '--recursive', action='store_true', default=False, help='Whether to scrape recursively')
parser.add_argument('-l', '--depth', type=int, default=5, help='The maximum depth to scrape to (default: 5)')
parser.add_argument('-p', '--path', type=str, default='data', help='The directory to save images and documents to (default: data)')

args = parser.parse_args()

main_url = args.url
max_depth = args.depth
save_dir = args.path

if not args.recursive:
    max_depth = 0

## URL parser
def recursive_scraper(url, main_domain, max_depth, visited_urls, url_list, current_depth=0):
    if current_depth <= max_depth and url not in visited_urls:
        visited_urls.add(url)
        try:
            htmldata = urlopen(url).read()
            soup = BeautifulSoup(htmldata, 'html.parser', parse_only=SoupStrainer('a'))

            for link in soup:
                if link.has_attr('href'):
                    href = link['href']

                    absolute_url = urljoin(url, href)

                    if urlparse(absolute_url).netloc == main_domain and absolute_url not in url_list:
                        url_list.append(absolute_url)
                        recursive_scraper(absolute_url, main_domain, max_depth, visited_urls, url_list, current_depth + 1)
                        # print(f"Retrieving URL: {absolute_url}")

        except Exception as e:
            # print(f"Error: {e}")
            pass

# Inicio Variables:
main_domain = urlparse(main_url).netloc
img_count = 0
visited_urls = set()
url_list = []

recursive_scraper(main_url, main_domain, max_depth, visited_urls, url_list)
# print("-------------------------------------")

# Bucle para img:
for item in url_list:
    try:
        htmldata = urlopen(item).read()
    except Exception as e:
        pass

    soup = BeautifulSoup(htmldata, 'html.parser')
    images = soup.find_all('img')

    for img_tag in images:
            img_url = img_tag['src']
            img_url = urljoin(item, img_url)
            parsed_url = urlparse(img_url)
            image_name = os.path.basename(parsed_url.path)

            if not os.path.exists(save_dir):
                os.makedirs(save_dir)

            save_path = os.path.join(save_dir, image_name)
            
            if not os.path.exists(save_path):
                try:
                    urllib.request.urlretrieve(img_url, save_path)
                    # print(f"Downloaded {image_name}")
                    img_count += 1
                except Exception as e:
                    pass

# Bucle para image:
for item in url_list:
    try:
        htmldata = urlopen(item).read()
    except Exception as e:
        pass

    soup = BeautifulSoup(htmldata, 'html.parser')
    images = soup.find_all('image')

    for img_tag in images:
            img_url = img_tag['href']
            img_url = urljoin(item, img_url)
            parsed_url = urlparse(img_url)
            image_name = os.path.basename(parsed_url.path)

            if not os.path.exists(save_dir):
                os.makedirs(save_dir)

            save_path = os.path.join(save_dir, image_name)
            
            if not os.path.exists(save_path):
                try:
                    urllib.request.urlretrieve(img_url, save_path)
                    # print(f"Downloaded {image_name}")
                    img_count += 1
                except Exception as e:
                    pass
# Picture:
for item in url_list:
    try:
        htmldata = urlopen(item).read()
    except Exception as e:
        pass

    soup = BeautifulSoup(htmldata, 'html.parser')
    images = soup.find_all('picture')

    for img_tag in images:
            img_url = img_tag['srcset']
            img_url = urljoin(item, img_url)
            parsed_url = urlparse(img_url)
            image_name = os.path.basename(parsed_url.path)

            if not os.path.exists(save_dir):
                os.makedirs(save_dir)

            save_path = os.path.join(save_dir, image_name)
            
            if not os.path.exists(save_path):
                try:
                    urllib.request.urlretrieve(img_url, save_path)
                    # print(f"Downloaded {image_name}")
                    img_count += 1
                except Exception as e:
                    pass

if not os.path.exists('docs'):
    os.makedirs('docs')

for link in url_list:
    file_ext = link.split('.')[-1]
    
    if file_ext in ['pdf', 'doc', 'docx']:
        filename = link.split('/')[-1]
        filepath = os.path.join('docs', filename)
        
        urllib.request.urlretrieve(link, filepath)

print(f"The total amount images donwloaded is: {img_count}")
