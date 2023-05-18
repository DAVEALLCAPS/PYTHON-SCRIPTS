import sys
import pyshorteners
import pyperclip

def shorten_url(url):
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(url)
    return short_url

if __name__ == "__main__":
    if len(sys.argv) > 1:
        long_url = sys.argv[1]  # Get the first command line argument
        short_url = shorten_url(long_url)
        print(short_url)

        # Copy to clipboard
        pyperclip.copy(short_url)
        print("Copied short URL to clipboard!")
    else:
        print("Please provide a URL")
