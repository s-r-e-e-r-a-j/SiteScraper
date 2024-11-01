SiteScraper

SiteScraper is an ethical hacking and website cloning tool built with Python. It enables users to download entire websites for offline access, analysis, and security assessments. Designed for ethical hackers, researchers, and developers, SiteScraper recursively crawls pages, follows internal links, and saves assets like HTML, CSS, images, and JavaScript, while preserving the original structure of the site

Use Responsibly


Warning: Use SiteScraper only on websites you own or have explicit permission to test and analyze. Unauthorized use of this tool on external sites without permission may violate laws and terms of service.


Installation

Clone the repository:

```git clone https://github.com/s-r-e-e-r-a-j/SITE-SCRAPER-TOOL.git```



```cd SITE-SCRAPER-TOOL```

``` cd 'Site Scraper' ```

Requirements:

```requests```


```beautifulsoup4```


```argparse```

Install It By Executing:

```pip3 install requests```

```pip3 install beautifulsoup4```

```pip3 install argparse```

If You Run This Tool any module is missing execute this command on terminal

```pip3 install missingmodulename```

Usage


Run SiteScraper from the command line with the following options:

```python3 sitescraper.py <URL> [options]```


Command-Line Options

Option	Description


```<URL>	The URL of the website to clone```


```-d, --depth (Optional) Set the maximum crawl depth (default: 3)```


```-o, --output	(Optional) Set the output directory (default: website_clone)```



Example

To clone a website up to a depth of 2 and save it in a directory named my_clone:


```python3 sitescraper.py https://example.com --depth 2 --output my_clone```



How It Works
SiteScraper follows these steps:

1. Initial Crawl: Downloads the main page of the target site.

 
2.  Recursive Crawling: Finds all internal links, then recursively crawls and saves them.

  
3. Asset Handling: Downloads and saves linked assets (CSS, JS, images).


4. File Structure Preservation: Saves files with the same structure as the original website, maintaining directories and paths.


License


This project is licensed under the MIT License.



