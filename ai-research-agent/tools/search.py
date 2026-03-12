from ddgs import DDGS


class DuckDuckGoSearchTool:
    """
    Tool that searches the web using DuckDuckGo
    """

    def __init__(self, max_results: int = 5):
        self.max_results = max_results

    def search(self, query: str):
        """
        Perform web search and return results
        """
        results = []

        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=self.max_results):
                results.append(
                    {
                        "title": r["title"],
                        "href": r["href"],
                        "body": r["body"],
                    }
                )

        return results