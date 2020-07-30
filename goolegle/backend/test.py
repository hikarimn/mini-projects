# -*- coding: utf-8 -*-

from page_scroller import Page_scroller 

# region Application Example Scripts

def test_application():
    '''
    Given that it has a relatively simple functionality, 
    I decided not to employ unit testing frameworks.
    To test this,
    python3 test.py
    '''
    
    url7 = 1
    url6 = ""
    url5 = "https://"
    url4 = "http://walrus.ai/"
    url3 = "https://stackoverflow.com/questions/33272548/getting-the-title-using-urllib"                              
    url2 = "https://www.w3.org/Icons/w3c_home"
    url1 = "http://www.u.arizona.edu/~erdmann/mse350/topics/list_comprehensions.html"
    limit = '12'
    scroller = Page_scroller(url6, 5, limit)
    scraped_urls = scroller.run_scraper()    
    print('-------------------------final result--------------------------------')
    print(scraped_urls)
    print(len(scraped_urls))
    print('---------------------------------------------------------------------')
    
    return

# endregion Application Example Scripts

# region Main Script
if __name__ == "__main__":
    test_application()

# endregion Main Script
