from services.search_service import search_person
from services.scraper import scrape_page

def run_search_agent(name, context):

    search_results = search_person(
        name,
        context
    )

    documents = []

    for result in search_results:

        try:

            url = result.get("href")

            if not url:
                continue

            content = scrape_page(url)

            if content:

                documents.append({
                    "title": result.get("title"),
                    "url": url,
                    "content": content
                })

        except Exception as e:

            print(f"Agent Error: {e}")

    return documents