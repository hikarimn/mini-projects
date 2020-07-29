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
    example = page_scroller.Page_scroller("https://www.w3.org/Icons/w3c_home",
                                     5,
                                     20)
                                     
    url = "https://www.w3.org/Icons/w3c_home"
    index = 20
    scroller = Page_scroller(url, 5, index)
    scraped_urls = scroller.run_scraper()    
    print('-------------------------final result--------------------------------')
    print(scraped_urls)
    print('---------------------------------------------------------------------')
    
    return

# endregion Application Example Scripts

# region Main Script
if __name__ == "__main__":
    test_application()

# endregion Main Script
