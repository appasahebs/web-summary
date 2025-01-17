import sys
from website import Website
if __name__ == "__main__":
    ws = Website()
    website = ws.display_summary("https://www.benzinga.com/") # This will fetch the website and print the title and 