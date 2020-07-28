# -*- coding: utf-8 -*-

from scroller.page_scroller import page_scroller

# region Application Example Scripts

def test_application():
    example = page_scroller('https://github.com/hikarimn',
                                     5,
                                     160)
                                     
    example.run_script()
    
    # print(example.results)
    # scroller = page_scroller()
    # scroller.get_links("https://arstechnica.com", 20)
    
    return



# endregion Application Example Scripts

# region Main Script
if __name__ == "__main__":
    test_application()

# endregion Main Script
