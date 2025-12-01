class CssSelector:
    news: str
    news_subject: str
    cookies_popup: str
    cookies_popup_dismiss: str
    youtube_icon: str
    search_icon: str
    search_input: str
    authorization_button: str

    def __init__(self):
        self.news = '[data-menuitem="news"]'
        self.news_subject = '.b-block__newslistdefault'
        self.cookies_popup = '.gdpr-text'
        self.cookies_popup_dismiss = '.gdpr-dismiss'
        self.youtube_icon = '.youtube-icon-ixbt'
        self.search_icon = '.icon-search'
        self.search_input = '.search_input'
        self.authorization_button = '#auth_top_block2'
