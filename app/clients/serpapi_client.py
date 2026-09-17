import os
import serpapi
from dotenv import load_dotenv


load_dotenv()


class SerpApiClient:

    def __init__(self):
        self.api_key = os.getenv("SERPAPI_KEY")

        if not self.api_key:
            raise ValueError("SERPAPI_KEY is not set")

        self.client = serpapi.Client(api_key=self.api_key)

    def search_patents(self, query):

        results = self.client.search({
            "engine": "google_patents",
            "q": query
        })

        return results