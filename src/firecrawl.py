import os
from firecrawl import FirecrawlApp, ScrapeOptions
from dotenv import load_dotenv

load_dotenv()

class FirecrawlService:
    def __init__(self):
        """Initialize the Firecrawl service with the API key from environment variables."""
        api_key = os.getenv("FIRECRAWL_API_KEY")
        if not api_key:
            raise ValueError("FIRECRAWL_API_KEY environment variable is not set.")
        self.app = FirecrawlApp(api_key=api_key)

    def search_companies(self, query: str, num_results: int=5):
        try:
            result = self.app.search(
                query = f"{query} company priciing ",
                limit= num_results,
                scrape_options=ScrapeOptions(
                   format=["markdown"],
                )
            )
            return result
        except Exception as e:
            print(f"Error during Firecrawl search: {e}")
            return []
    
    def scrape_company_page(self, url: str):
        try:
            result = self.app.scrape_url(
                url,
                format=["markdown"]
            )
            return result
        except Exception as e:
            print(f"Error during Firecrawl scrape: {e}")
            return None

