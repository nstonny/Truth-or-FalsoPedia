import wikipedia
import random

from data_wikipedia import get_data_wikipedia


class Category:
    def __init__(self, category, url=None):
        self.category = category
        self.url = url

    def __str__(self):
        return f"Category is {self.category}"


    def choose_category(self):
        """Returns User selected category"""

        return self.category


    def get_category_links(self):
        """Returns a list of links from the category page
        user selected"""

        if self.url:
            get_all_links = get_data_wikipedia(self.url)
        else:
            page = wikipedia.page(self.category)
            get_all_links = page.links

        links = get_all_links[1:20]
        return links


    def select_random_articles(self):
        """Selects three random links from the links returned
        from the wikipedia page"""

        links = self.get_category_links()
        random_links = []

        for i in range(3):
            random_link = random.choice(links)
            random_links.append(random_link)
        return random_links


    def get_summary(self):
        """Returns summary of the random links"""

        random_links = self.select_random_articles()
        summary_list = []
        for link in random_links:
            try:
                summary = wikipedia.summary(link, sentences=1, auto_suggest=False)
                if summary:
                    summary_list.append(summary)
            except Exception as e:
                print(f"The error is {e}")
        return summary_list








