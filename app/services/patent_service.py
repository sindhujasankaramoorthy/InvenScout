from app.clients.serpapi_client import SerpApiClient
from app.models.patent import Patent


class PatentService:

    def __init__(self):
        self.serpapi = SerpApiClient()

    def search_patents(self, query):

        results = self.serpapi.search_patents(query)

        patents = []

        for result in results.get("organic_results", []):

            patent = Patent(
                title=result.get("title", ""),
                publication_number=result.get("publication_number"),
                filing_date=result.get("filing_date"),
                snippet=result.get("snippet"),
                link=result.get("patent_link")
            )

            patents.append(patent)

        return patents