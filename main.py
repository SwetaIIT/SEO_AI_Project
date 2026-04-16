"""
Main entry point for the SEO AI Project
Orchestrates YouTube, LinkedIn, and Web scrapers
"""

from scrapers.youtube_scraper import YouTubeScraper
from scrapers.linkedin_scraper import LinkedInScraper
from scrapers.web_scraper import WebScraper
from utils.helpers import save_to_csv, setup_logging

# Initialize logging
logger = setup_logging(__name__)

def main():
    """Main function to run all scrapers"""
    
    logger.info("Starting SEO AI Project...")
    
    # Example: YouTube Scraper
    youtube = YouTubeScraper()
    logger.info("YouTube scraper initialized")
    
    # Example: LinkedIn Scraper
    linkedin = LinkedInScraper()
    logger.info("LinkedIn scraper initialized")
    
    # Example: Web Scraper
    web = WebScraper()
    logger.info("Web scraper initialized")
    
    logger.info("All scrapers ready. Configure and run scrapers as needed.")

if __name__ == "__main__":
    main()