import duckduckgo_search


class WebSearch:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def verify_query(self, query):
        # checks if the query is valid and no empty leading/trailing spaces
        if (
            query is None
            or len(query) <= 1
            or query.strip() == ""
            or query.isspace()
            or query == " "
        ):
            return False
        print(self.search(query))
        return self.search(query)

        def search(self, query: str) -> list[dict]:
            return duckduckgo_search.DDGS().text(query, max_results=5)
