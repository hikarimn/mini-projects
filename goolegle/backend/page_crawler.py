import re
import urllib.request
from concurrent.futures import ThreadPoolExecutor
import requests

class Page_crawler:           

    def __init__(self, original_url, threads, limit):
        self.urls = []
        self.original_url = original_url
        self.result = []
        self.max_threads = threads
        self.limit = limit
        self.regex = re.compile(
            r'^(?:http|ftp)s?://' # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
            r'localhost|' #localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    def run_crawler(self):
        if not self._validate_input():
            return []
        for url in self.get_urls():
            title = self._get_title_by_url(url)
            self.result.append({
                'url': url,
                "title": title
            })
        return self.result
        
    def get_urls(self):
        '''
        if the submitted url is valid, add it to a list. The scraper starts crawling concurrently. 
        It stopps crawling once it reaches to a given limit and returns the list of urls. 
        if the submitted url is not valid, it returns an empty list
        '''
        list_size = 0
        self.urls.append(self.original_url)

        while self.limit >= len(self.urls):
            with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
                executor.map(self._wrapper, self.urls)
                self.urls = list(set(self.urls))

                if len(self.urls) >= self.limit:
                    break
                if len(self.urls) == list_size:
                    break
                
                list_size = len(self.urls)

            if len(self.urls) >= self.limit:
                break
        return self.urls[:self.limit]
    
    def _wrapper(self, url):
        self._scraper(url)
    
    def _scraper(self, url):
        '''
        crawl the web page and add the found links to the list, if the link is not valid, add nothing to the list 
        '''
        if len(self.urls) >= self.limit:
            pass

        if not self._validate_url(url):
            pass

        try:    
            links = self._get_links_by_url(url)
            self.urls = list(set(self.urls.extend(links)))
        except (UnicodeDecodeError, ValueError, Exception) as e:
            pass
    
    def _get_links_by_url(self, url):
        ''' find a list of urls on the page '''
        try:
            html = urllib.request.urlopen(url).read().decode('utf-8')
            links = []
            for link in re.findall('"((http|ftp)s?://.*?)"', html):
                links.append(link[0])
                if len(self.urls) + len(links)>= self.limit:
                    break
            return links
        except:
            return []

    def _get_title_by_url(self, url):
        ''' find a title of the page with a given url '''
        try:
            html = urllib.request.urlopen(url).read().decode('utf-8')
            title = html.split('<title>')[1].split('</title>')[0]
            return title
        except Exception as e:
            return "No title"

    def _validate_input(self):
        try:
            self.original_url = str(self.original_url)
            self.limit = int(self.limit)
            return len(self.original_url) > 0 and self.limit > 0 and isinstance(self.original_url, str) and isinstance(self.limit, int) and self._validate_url(self.original_url)
        except Exception as e:
            print('!' * 20 + 'invalid input' + '!' * 20)
            print(e)
            return False
        
    def _validate_url(self, url):
        ''' check if the submitted url is valid as an url '''
        return re.match(self.regex, url) != None