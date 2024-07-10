import duckduckgo_search


class WebSearch:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def verify_query(self, query: str) -> list[dict]:
        # checks if the query is valid and no empty leading/trailing spaces
        if (
            query is None
            or len(query) <= 1
            or query.strip() == ""
            or query.isspace()
            or query == " "
        ):
            return False

        # cleanup the results
        results = duckduckgo_search.DDGS().text(query, max_results=5)

        print(results)
        return results
