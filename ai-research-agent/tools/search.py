from duckduckgo_search import DDGS

class DuckDuckGoSearch:
    def __init__(self, max_results=5):
        self.search_engine = DDGS()
        self.max_results = max_results
    
    def search(self, query: str):
        results = []

        with DDGS() as ddgs:
            for result in ddgs.text(query, max_results=self.max_results):
                results.append({
                    'title': result['title'],
                    'href': result['href'],
                    'body': result['body']
                })