# Web Crawler made with Scrapy Framework and Selenium API to interact and extract the comments in the news of Portal G1.
# Author.........: Lucas Darlindo F. Rodrigues (lucas.darlindo@gmail.com), from Federal University of Western Para (IEG);
# Initial Version: Feb 21, 2019;
# Updated........: May 20, 2019;
# Upgrades.......: i) Preprocessing features in the extraction of the comments.
# Version........: CrawlerG1_Comments_v5L-Rev3 (L = Local Edition, ChromeDriver v74: Google Chrome / Chromium);
# Prerequisites..: Google Chrome v74 or Chromium v74 and ChromeDriver v74 (Python 3.7 with Selenium and Scrapy).

# Import Section
import scrapy
import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Insert here all the keywords to be search in the crawler execution!
labels = ['CLA']


# Method to verify if the keyword is present in the article title
def checkTitle(title):
    return re.compile(r'\b({0})\b'.format(title), flags=re.IGNORECASE).search


# Code
class CommentsG1(scrapy.Spider):
    name = "CommentsG1"
    allowed_domains = ['g1.globo.com']
    start_urls = ['https://g1.globo.com/busca/?q=&order=relevant&species=notícias']

    custom_settings = {
        'FEED_FORMAT': 'csv',
        "FEED_URI": "CSV_Data/G1_Data/Comments/CommentsG1_%(time)s.csv"
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.driver = webdriver.Chrome()

    def parse(self, response):
        self.driver.get(response.url)

        ################################################################# Getting the news #################################################################
        for label in labels:
            self.driver.get('https://g1.globo.com/busca/?q=' + label + '&order=relevant&species=notícias')
            hasMore = True
            principal = self.driver.current_window_handle

            while hasMore == True:
                # Keep loading all the news in the page until ends and it's ready to continue the process of parsing and crawl.
                try:
                    if self.driver.find_element_by_xpath('//*[@id="content"]/div/div/div/a'):
                        while self.driver.find_element_by_xpath('//*[@id="content"]/div/div/div/a'):
                            try:
                                nLoadMore = self.driver.find_element_by_xpath('//*[@id="content"]/div/div/div/a')
                                nLoadMore.location_once_scrolled_into_view
                                nLoadMore.click()
                            except:
                                pass
                            time.sleep(10)
                except:
                    pass

                # Loading the news: getting their identifiers and appending into a list (IDs)
                nLast = '0'
                nID = self.driver.find_elements_by_xpath('//*[@id="content"]/div/div/ul/li')
                nID_List = []
                for n in nID:
                    if n.get_attribute('data-position') > nLast:
                        nID_List.append(n.get_attribute('data-position'))

                # Loading the news: acessing
                time.sleep(5)
                for i in nID_List:
                    nLast = i
                    # Catch the link of the article, scrolls to him and acess into a new tab.
                    try:
                        articleXPath = self.driver.find_element_by_xpath(
                            '/html/body/section/div/div/ul/li[@data-position=' + i + ']/div[2]/a')
                    except:
                        try:
                            articleXPath = self.driver.find_element_by_xpath(
                                '/html/body/section/div/div/ul/li[@data-position=' + i + ']/div[3]/a')
                        except:
                            pass
                    # Open the article in a new tab in order to keep the list full loaded and to save time.
                    try:
                        time.sleep(2)
                        articleXPath.location_once_scrolled_into_view
                        articleLink = 'https://' + articleXPath.get_attribute('href')[8:]
                        self.driver.execute_script("window.open('');")
                        self.driver.switch_to.window(self.driver.window_handles[1])
                        time.sleep(2)
                        self.driver.get(articleLink)
                        time.sleep(5)
                    except:
                        try:
                            self.driver.switch_to.window(self.driver.window_handles[1])
                            self.driver.close()
                        except:
                            pass

                    ######################################################## Parsing and Extraction ##########################################################
                    # Parsing process: commentary section
                    # All the 'time.sleep()' are for give the browser time to load all the items

                    # Extract the title and verify if it has the keyword of search, if not, just ignore.
                    try:
                        titleXPath = self.driver.find_element_by_xpath('/html/head/meta[@name="title"]')
                        title = titleXPath.get_attribute('content')
                        # Check if the article openned have on it's title the active keyword.
                        if (checkTitle(label)(str.lower(title))):
                            # Scrolls to the comments section, in order to load if it has.                     
                            try:
                                comment_xpath = self.driver.find_element_by_xpath(
                                    '//main[@class="mc-body theme"]//div[@id="boxComentarios"]')
                                comment_xpath.location_once_scrolled_into_view
                                time.sleep(5)
                                comment_xpath.location_once_scrolled_into_view
                                time.sleep(1)
                            except:
                                try:
                                    comment_xpath = self.driver.find_element_by_xpath(
                                        '//*[@id="glb-corpo"]/div/div[1]/div[1]/div[2]')
                                    comment_xpath.location_once_scrolled_into_view
                                    time.sleep(5)
                                    comment_xpath.location_once_scrolled_into_view
                                    time.sleep(1)
                                except:
                                    try:
                                        comment_xpath = self.driver.find_element_by_xpath('//*[@id="boxComentarios"]')
                                        comment_xpath.location_once_scrolled_into_view
                                        time.sleep(5)
                                        comment_xpath.location_once_scrolled_into_view
                                        time.sleep(1)
                                    except:
                                        pass
                            # Try to click the "Load more comments" button until it loads all of them
                            try:
                                while self.driver.find_element_by_xpath(
                                        '/html/body/div[2]/main/div[4]/div[2]/div/div[4]/button'):
                                    cLoadMore = self.driver.find_element_by_xpath(
                                        '/html/body/div[2]/main/div[4]/div[2]/div/div[4]/button')
                                    time.sleep(2)
                                    cLoadMore.location_once_scrolled_into_view
                                    time.sleep(5)
                                    cLoadMore.click()
                            except:
                                try:
                                    while self.driver.find_element_by_xpath(
                                            '/html/body/div[2]/main/div[4]/div[3]/div/div[4]/button'):
                                        cLoadMore = self.driver.find_element_by_xpath(
                                            '/html/body/div[2]/main/div[4]/div[3]/div/div[4]/button')
                                        time.sleep(2)
                                        cLoadMore.location_once_scrolled_into_view
                                        time.sleep(5)
                                        cLoadMore.click()
                                except:
                                    try:
                                        while self.driver.find_element_by_xpath(
                                                '//*[@id="boxComentarios"]/div[4]/button'):
                                            cLoadMore = self.driver.find_element_by_xpath(
                                                '//*[@id="boxComentarios"]/div[4]/button')
                                            time.sleep(2)
                                            cLoadMore.location_once_scrolled_into_view
                                            time.sleep(5)
                                            cLoadMore.click()
                                    except:
                                        pass

                            try:
                                # Catch the IDs of the users and append into a list
                                ids = self.driver.find_elements_by_xpath("//*[contains(@id, 'comentario-')]")
                                comment_ids = []
                                for i in ids:
                                    comment_ids.append(i.get_attribute('id'))

                                lastAuthor = ""
                                lastComment = ""
                                duplicated = False

                                # The IDs are used here to extract their comment(s) directly
                                for c in comment_ids:
                                    try:
                                        cAuthorXPath = self.driver.find_element_by_xpath(
                                            '//*[@id="' + c + '"]/div[1]/div/div[2]/strong')
                                        cDateXPath = self.driver.find_element_by_xpath(
                                            '//*[@id="' + c + '"]/div[1]/div/div[2]/div[2]/abbr')
                                        commentData = self.driver.find_element_by_xpath(
                                            '//*[@id="' + c + '"]/div[1]/div/div[2]/p')
                                        likesXPath = self.driver.find_element_by_xpath(
                                            '/html/body/div[2]/main/div[4]/div[2]/div/div[4]/ul/li[@id="' + c + '"]/div[1]/div/div[2]/div[3]/button[1]')
                                        dislikesXPath = self.driver.find_element_by_xpath(
                                            '/html/body/div[2]/main/div[4]/div[2]/div/div[4]/ul/li[@id="' + c + '"]/div[1]/div/div[2]/div[3]/button[2]')

                                        cAuthor = cAuthorXPath.text
                                        cDate = cDateXPath.get_attribute('title')
                                        comment = commentData.text
                                        likes = likesXPath.text
                                        dislikes = dislikesXPath.text

                                        # Verifying if the last author and comment are the same of actual (preprocessing: filtering duplicated comments)
                                        if (lastAuthor == cAuthor and lastComment == comment):
                                            duplicated = True
                                        else:
                                            duplicated = False

                                        # Verifying if the comment is not empty (preprocessing: filtering empty comments and ignoring if is and duplicated)
                                        if (len(comment) > 0 and duplicated == False):
                                            # Yield: CSV File
                                            yield {
                                                'Author': cAuthor,
                                                'Published': cDate,
                                                'Comment': comment,
                                                'Likes': likes,
                                                'Dislikes': dislikes,
                                                'Article': title,
                                                'Keyword': label
                                            }
                                    except:
                                        # Model 1
                                        try:
                                            cAuthorXPath = self.driver.find_element_by_xpath(
                                                '//div[@class="glbComentarios-lista-resposta"]//li[@id="' + c + '"]/div[1]/div/div[2]/strong')
                                            cDateXPath = self.driver.find_element_by_xpath(
                                                '//div[@class="glbComentarios-lista-resposta"]//li[@id="' + c + '"]/div[1]/div/div[2]/div[2]/abbr')
                                            commentData = self.driver.find_element_by_xpath(
                                                '//*[@id="' + c + '"]/div/div/div[2]/p')
                                            likesXPath = self.driver.find_element_by_xpath(
                                                '//div[@class="glbComentarios-lista-resposta"]//li[@id="' + c + '"]/div[1]/div/div[2]/div[3]/button[1]')
                                            dislikesXPath = self.driver.find_element_by_xpath(
                                                '//div[@class="glbComentarios-lista-resposta"]//li[@id="' + c + '"]/div[1]/div/div[2]/div[3]/button[2]')

                                            cAuthor = cAuthorXPath.text
                                            cDate = cDateXPath.get_attribute('title')
                                            comment = commentData.text
                                            likes = likesXPath.text
                                            dislikes = dislikesXPath.text

                                            # Verifying if the last author and comment are the same of actual (preprocessing: filtering duplicated comments)
                                            if (lastAuthor == cAuthor and lastComment == comment):
                                                duplicated = True
                                            else:
                                                duplicated = False

                                            # Verifying if the comment is not empty (preprocessing: filtering empty comments and ignoring if is and duplicated)
                                            if (len(comment) > 0 and duplicated == False):
                                                # Yield: CSV File
                                                yield {
                                                    'Author': cAuthor,
                                                    'Published': cDate,
                                                    'Comment': comment,
                                                    'Likes': likes,
                                                    'Dislikes': dislikes,
                                                    'Article': title,
                                                    'Keyword': label
                                                }
                                        except:
                                            # Model 2
                                            try:
                                                cAuthorXPath = self.driver.find_element_by_xpath(
                                                    '//*[@id="' + c + '"]/div/div/div[2]/strong')
                                                cDateXPath = self.driver.find_element_by_xpath(
                                                    '//*[@id="' + c + '"]/div/div/div[2]/div[2]/abbr')
                                                commentData = self.driver.find_element_by_xpath(
                                                    '//*[@id="' + c + '"]/div/div/div[2]/p')
                                                likesXPath = self.driver.find_element_by_xpath(
                                                    '//*[@id="' + c + '"]/div/div/div[2]/div[3]/button[1]')
                                                dislikesXPath = self.driver.find_element_by_xpath(
                                                    '//*[@id="' + c + '"]/div/div/div[2]/div[3]/button[2]')

                                                cAuthor = cAuthorXPath.text
                                                cDate = cDateXPath.get_attribute('title')
                                                comment = commentData.text
                                                likes = likesXPath.text
                                                dislikes = dislikesXPath.text

                                                # Verifying if the last author and comment are the same of actual (preprocessing: filtering duplicated comments)
                                                if (lastAuthor == cAuthor and lastComment == comment):
                                                    duplicated = True
                                                else:
                                                    duplicated = False

                                                # Verifying if the comment is not empty (preprocessing: filtering empty comments and ignoring if is and duplicated)
                                                if (len(comment) > 0 and duplicated == False):
                                                    # Yield: CSV File
                                                    yield {
                                                        'Author': cAuthor,
                                                        'Published': cDate,
                                                        'Comment': comment,
                                                        'Likes': likes,
                                                        'Dislikes': dislikes,
                                                        'Article': title,
                                                        'Keyword': label
                                                    }
                                            except:
                                                pass
                                comment_ids.clear()
                            # Has no comments on the article, ignore.
                            except:
                                pass
                    except:
                        pass
                    # Close the tab and wait (8 sec.)
                    try:
                        time.sleep(5)
                        self.driver.close()
                        time.sleep(3)
                    except:
                        pass
                    # Return to the main tab, with all the news loaded.    
                    try:
                        self.driver.window_handles(principal)
                    except:
                        try:
                            self.driver.switch_to.window(principal)
                        except:
                            pass

                hasMore = False
            # Clear the list of IDs of the news, to advance to the next keyword on the list.
            nID_List.clear()

        # End of the crawler execution
        nID_List.clear()
        self.driver.close()
