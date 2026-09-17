from app.services.query_service import QueryService
from app.services.patent_service import PatentService


idea = "A smart water bottle that reminds users to drink based on activity level"


# Step 1: Expand the idea using Gemini
query_service = QueryService()

expanded_queries = query_service.expand_query(idea)

print("\nTechnical queries:")
for query in expanded_queries["technical_queries"]:
    print("-", query)


# Step 2: Search patents using the generated technical queries
patent_service = PatentService()

patents = patent_service.search_patents(
    expanded_queries["technical_queries"]
)


# Step 3: Display results
print("\nTotal patents found:", len(patents))

for patent in patents[:10]:
    print("\n", patent.model_dump())