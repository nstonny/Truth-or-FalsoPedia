#include imports

class WikiService:
    # Fetches article summaries from the Wikipedia REST API.

    BASE_URL = "https://en.wikipedia.org/api/rest_v1/page/summary/"

    def __init__(self):
        # set timeout
        pass

    def get_summary(self, topic: str):
        # Fetches the Wikipedia summary for a single article.
        pass

    def get_random_summaries(self, count: int) :
        # Returns summaries for a random selection from config.TOPICS.
        pass

    def build_url(self, topic: str):
        pass

    #def _parse_response(self, response: requests.Response, topic: str):
        #pass



