import re
import urllib.request


from concurrent.futures import ThreadPoolExecutor
import requests

class Page_scroller:           

    def __init__(self, original_url, threads, limits):
        self.urls = {}
        self.original_url = original_url
        self.max_threads = threads
        self.limits = int(limits)
        self.regex = re.compile(
            r'^(?:http|ftp)s?://' # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
            r'localhost|' #localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        
    def run_scraper(self):
        '''
        if the submitted url is valid, add it to a list. The scraper starts crawling concurrently. 
        It stopps crawling once it reaches to a given limit and returns the list of urls. 
        if the submitted url is not valid, it returns an empty list
        '''
        if not self._validate_url(self.original_url):
            print('not a valid url')
            return self.urls

        list_size = 0
        self.urls.update({
            self.original_url : None
        })

        while self.limits >= len(self.urls):
            # print(len(self.urls))
            with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
                for url in self.urls.keys():
                    executor.submit(self._wrapper, url)
                    if len(self.urls) >= self.limits:
                        break
                # executor.map(self._wrapper, self.urls.keys())
                # self.urls = list(set(self.urls))

                if len(self.urls) >= self.limits:
                    break
                if len(self.urls) == list_size:
                    break
                
                list_size = len(self.urls)
                print(len(self.urls))

            if len(self.urls) >= self.limits:
                break
        # return self.urls[:self.limits]
        return dict(list(self.urls.items())[:self.limits])
    
    def _wrapper(self, url):
        self._scraper(url)
    
    def _scraper(self, url):
        '''
        crawl the web page and add the found links to the list, if the link is not valid, add nothing to the list 
        '''
        if len(self.urls) >= self.limits:
            pass

        if not self._validate_url(url):
            pass

        try:   
            response = urllib.request.urlopen(url)
            html = response.read().decode('utf-8')
            # print(html)
            links = self._get_links_by_html(html) # find more links
            title = self._get_title_by_html(html) # find a title
            # print('url: ')
            # print(url) 
            # print('title: ')
            if url in self.urls and title == self.urls[url]: # if the same url already exists, skip 
                pass
            print('title: ' + title)
            self.urls.update({
                url : title
            })
            for link in links:
                self.urls.update({
                    link : None
                })
                # print(len(self.urls))
                if len(self.urls) >= self.limits:
                    break
            if len(self.urls) >= self.limits:
                pass
            # print(self.urls)
            # print(len(self.urls))

            # self.urls = list(set(self.urls.extend(list(links))))
        except (UnicodeDecodeError, ValueError, Exception) as e:
            print('!'*50)
            print(url)
            print(e)
            print('!'*50)
            pass

    def _validate_url(self, url):
        '''
        check if the submitted url is valid as an url
        '''
        return re.match(self.regex, url) != None
    
    def _get_links_by_html(self, html):
        ''' find links in side the html '''
        return set([link[0] for link in re.findall('"((http|ftp)s?://.*?)"', html)]) 

    def _get_title_by_html(self, html):
        ''' find a title of the page '''
        try:
            return html.split('<title>')[1].split('</title>')[0]
        except Exception as e:
            return "No title"
