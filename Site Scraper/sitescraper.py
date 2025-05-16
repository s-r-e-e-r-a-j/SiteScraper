import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import os
import argparse

print("\033[93m")
print(r"""


   _____   _   _               _____                                                
  / ____| (_) | |             / ____|                                             
 | (___    _  | |_    ___    | (___     ___   _ __    __ _   _ __     ___   _ __     
  \___ \  | | | __|  / _ \    \___ \   / __| | '__|  / _` | | '_ \   / _ \ | '__|    
  ____) | | | | |_  |  __/    ____) | | (__  | |    | (_| | | |_) | |  __/ | |       
 |_____/  |_|  \__|  \___|   |_____/   \___| |_|     \__,_| | .__/   \___| |_|       
                                                            | |                                                
                                                            |_|  


                                                             Developer: Sreeraj
   """)
print("\033[92m  * GitHub: https://github.com/s-r-e-e-r-a-j/033[0m\n")

# Set to avoid re-downloading the same URL
downloaded_urls = set()

def save_file(url, root_dir):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            parsed_url = urlparse(url)
            # Determine file path to save
            path = os.path.join(root_dir, parsed_url.netloc, parsed_url.path.lstrip("/"))
            os.makedirs(os.path.dirname(path), exist_ok=True)

            if url.endswith(('.jpg', '.jpeg', '.png', '.gif', '.css', '.js')):
                file_path = path
            else:
                file_path = os.path.join(path, "index.html") if path.endswith("/") else path

            with open(file_path, "wb") as f:
                f.write(response.content)
            print(f"\033[94mSaved: {file_path}\033[0m")
    except Exception as e:
        print(f"\033[31mError saving {url}: {e}\033[0m")

def crawl(url, root_dir, max_depth=3, depth=0):
    if depth > max_depth or url in downloaded_urls:
        return
    downloaded_urls.add(url)

    save_file(url, root_dir)
    
    response = requests.get(url)
    if response.status_code != 200:
        return

    soup = BeautifulSoup(response.text, "html.parser")
    base_url = f"{urlparse(url).scheme}://{urlparse(url).netloc}"
    
    # Crawl and save all <a>, <img>, <link>, and <script> tags
    for tag in soup.find_all(["a", "img", "link", "script"]):
        src_or_href = tag.get("href") or tag.get("src")
        if src_or_href:
            # Resolve relative URLs
            full_url = urljoin(base_url, src_or_href)
            if urlparse(full_url).netloc == urlparse(url).netloc:  # stay within the domain
                crawl(full_url, root_dir, max_depth, depth + 1)

def main():
    parser = argparse.ArgumentParser(description="Clone a website locally")
    parser.add_argument("url", help="The URL of the website to download")
    parser.add_argument("-d", "--depth", type=int, default=3, help="Maximum crawl depth (default: 3)")
    parser.add_argument("-o", "--output", default="website_clone", help="Output directory (default: website_clone)")
    args = parser.parse_args()

    # Start crawl
    crawl(args.url, args.output, args.depth)

if __name__ == "__main__":
    main()
