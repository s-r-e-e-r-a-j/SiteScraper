# SiteScraper

The Site Scraper Tool is an ethical hacking program developed in Python that enables users to clone websites for educational purposes by copying HTML, CSS, JavaScript, and PHP.


**Note:** Use this tool responsibly and only on sites where you have explicit permission, as unauthorized scraping can lead to legal issues.

## Use Responsibly


 `Warning`: Use SiteScraper only on websites you own or have explicit permission to test and analyze. Unauthorized use of this tool on external sites without permission may violate laws and terms of service.


## Installation

### Clone the repository:

```bash
git clone https://github.com/s-r-e-e-r-a-j/SiteScraper.git
```


### Navigate to the SiteScraper directory

```bash
cd SiteScraper
```

### install Required libraries:-

```bash
pip3 install -r requirements.txt
``````


### Navigate to the Site Scraper directory
``` bash
cd 'Site Scraper'
 ```
### install the tool:
```bash
sudo python3 install.py
```
Then Enter `y` for install


## Usage


 Run SiteScraper from the command line with the following options:

``` bash
sitescraper <URL> [options]
```


## Command-Line Options

### Option	Description


 ```<URL>	The URL of the website to clone```


 ```-d, --depth (Optional) Set the maximum crawl depth (default: 3)```


 ```-o, --output	(Optional) Set the output directory (default: website_clone)     you can also specify path to save    example -o /home/kali/Desktop/result    ```




### Example

 To clone a website up to a depth of 2 and save it in a directory named `my_clone`, use the following command:

```bash
sitescraper https://example.com -d 2 -o /home/kali/Desktop/my_clone
```
After the cloning process is complete, a directory named after the domain (e.g., `http.example.com`) will be created inside my_clone.

To view the cloned website, open the `index.html` file in a browser.

If you see `.php` files in the directory, it means the website has a PHP backend, and you need to start a PHP server to run it properly.

#### Starting the PHP Server
1. **Navigate to the Cloned Website Directory***
   
```bash
cd /home/kali/Desktop/my_clone/http.example.com
```
3. **Start the PHP Server**
Replace `yourmachineipaddress` with your actual local IP (e.g., `192.168.1.5`):

```nginx
php -S yourmachineipaddress:8080
```

**Example:**

```nginx
php -S 192.168.1.5:8080
```
3. **Open the Cloned Website in a Browser**

   
In your web browser, enter:

```arduino
http://yourmachineipaddress:8080
```
**Example:**

```cpp
http://192.168.1.5:8080
```

**Now, you should be able to access and interact with the cloned website.**


#### How It Works
SiteScraper follows these steps:

1. `Initial Crawl`: Downloads the main page of the target site.

 
 2. ` Recursive Crawling`: Finds all internal links, then recursively crawls and saves them.

  
 3. `Asset Handling`: Downloads and saves linked assets (CSS, JS, images).


 4. `File Structure Preservation`: Saves files with the same structure as the original website, maintaining directories and paths.

## uninstallation

```bash
cd SiteScraper
```
```bash
cd 'Site Scraper'
```
```bash
sudo python3 install.py
```
Then Enter `n` for uninstall


## License


 This project is licensed under the MIT License.



