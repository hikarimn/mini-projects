
import bs4
import re
import urllib.request

# from concurrent.futures import ThreadPoolExecutor
import requests

class Page_scroller:           

    def __init__(self, original_url, threads, limits):

        self.urls = []
        self.original_url = original_url
        self.results = {}
        self.max_threads = threads
        self.limits = limits
        self.url_counter = 0

    # def __make_request(self, url):
    #     try:
    #         r = requests.get(url=url, timeout=20)
    #         r.raise_for_status()
    #     except requests.exceptions.Timeout:
    #         r = requests.get(url=url, timeout=60)
    #     except requests.exceptions.ConnectionError:
    #         r = requests.get(url=url, timeout=60)
    #     except requests.exceptions.RequestException as e:
    #         raise e
    #     return r.url, r.text

    # def __parse_results(self, url, html):
    #     try:
    #         soup = BeautifulSoup(html, 'html.parser')
    #         title = soup.find('title').get_text()
    #         print(title)
    #         for link in soup.find_all('a', href=True):
    #             # print(link['href'])
    #             # print(link)
    #             if link['href'].startswith('https://'):
    #                 self.urls.append(link['href'])
    #             else:
    #                 self.urls.append(url + link['href'])
    #             if len(self.urls) >= self.limits:
    #                 break
    #             print(len(self.urls))
    #     except Exception as e:
    #         raise e

    #     if title:
    #         self.results[url] = title

    # def wrapper(self, url):
    #     url, html = self.__make_request(url)
    #     self.__parse_results(url, html)

    # def run_script1(self):
    #     i = 0
    #     with ThreadPoolExecutor(max_workers=min(len(self.urls),self.max_threads)) as Executor:
    #         while self.limits >= len(self.urls):
    #             # print(len(self.urls))
    #             for u in self.urls:
    #             # while i < len(self.urls): 
                    
    #             # for u in self.urls:
    #                 # if i >= self.limits:
    #                 #     break
    #                 jobs = [Executor.submit(self.wrapper, u)]
    #                 # print(u)
    #                 # print(len(self.urls))
    #                 # i += 1
    #     return self.urls

    def run_script(self):
        self.urls.append(self.original_url)

        while self.limits >= len(self.urls):
            for url in self.urls:
                try:
                    r = requests.get(url=url, timeout=20)
                    r.raise_for_status()
                except requests.exceptions.Timeout:
                    r = requests.get(url=url, timeout=60)
                except requests.exceptions.ConnectionError:
                    r = requests.get(url=url, timeout=60)
                except requests.exceptions.RequestException as e:
                    raise e

                soup = bs4.BeautifulSoup(r.text, 'html.parser')
                title = soup.find('title').get_text()
    
                for link in soup.find_all('a', href=True):
                    # print(link['href'])
                    # print(link)
                    if link['href'].startswith('https://'):
                        self.urls.append(link['href'])
                    else:
                        self.urls.append(url + link['href'])
                    print(len(self.urls))
                    if len(self.urls) >= self.limits:
                        break

                    if self.limits <= len(self.urls):
                        break            
                if self.limits <= len(self.urls):
                    break  
            if self.limits <= len(self.urls):
                break 
                        

        print(self.urls)
        return self.urls


        

        # while(len(self.urls) <= self.limits):
        #     resp = urllib.request.urlopen("https://github.com/hikarimn")
        #     soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))

        #     for link in soup.find_all('a', href=True):
        #         if self.limits <= len(self.urls):
        #             break
        #         if link['href'].startswith('https://') or link['href'].startswith('http://'):
        #             self.urls.append(link['href'])
        #         else:
        #             self.urls.append(url + link['href'])
        #         print(link['href'])