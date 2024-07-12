import requests


class Jokes:
    def get_joke(self) -> str:
        # Fetches a random joke
        r = requests.get("https://v2.jokeapi.dev/joke/Any")
        # return the joke then the punchline

        r = r.json()
        if r["type"] == "single":
            return r["joke"]
        else:
            return f"{r['setup']}... {r['delivery']}"
