class CssSelector:
    news: str
    news_subject: str
    cookies_popup: str
    cookies_popup_dismiss: str
    youtube_icon: str
    search_icon: str

    def __init__(self):
        self.news = '[data-menuitem="news"]'
        self.news_subject = '.b-block__newslistdefault'
        self.cookies_popup = '.gdpr-text'
        self.cookies_popup_dismiss = '.gdpr-dismiss'
        self.youtube_icon = '.social_icon_div youtube-icon-ixbt'
        self.search_icon = '.icon icon-search'
