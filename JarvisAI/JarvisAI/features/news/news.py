from urllib.request import urlopen
from bs4 import BeautifulSoup as soup


def news():
    """
    This method will tells top 15 current NEWS
    :return: list / bool
    """
    try:
        news_url = "https://news.google.com/news/rss"
        Client = urlopen(news_url)
        xml_page = Client.read()
        Client.close()
        soup_page = soup(xml_page, "xml")
        news_list = soup_page.findAll("item")
        return [str(news.title.text.encode('utf-8'))[1:] for news in news_list[:15]]
    except Exception as e:
        print(e)
        return False
