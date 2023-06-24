import requests
from bs4 import BeautifulSoup
from lxml import html

class VulmonScraper:
    def __init__(self, cve):
        self.cve = cve
        self.response = requests.get(f"https://vulmon.com/vulnerabilitydetails?qid={cve}&scoretype=cvssv3")
        self.soup = BeautifulSoup(self.response.content, 'html.parser')
        self.tree = html.fromstring(self.response.content)

    def meta_info(self):
        cve_name = self.soup.find('h1', class_="ui header column jstitle1").text.strip()
        cvss = self.soup.find('div', class_='value').text.strip()
        published_date = self.soup.find('div', class_='meta').text.strip()
        description = self.soup.find('p', class_='jsdescription1 content_overview').text.strip()

        if not cve_name:
            cve_name = None
        if not cvss:
            cvss = None
        if not published_date:
            published_date = None
        else:
            date = published_date.split(' ')
            published_date = date[1]
        if not description:
            description = None

        data = {
            "CVEName": cve_name,
            "CVSSv3": cvss,
            "PublishedDate": published_date,
            "Description": description
        }
        return data

    def vuln_products(self):
        vulnerable_products = self.tree.xpath('//tbody/tr/td/p/text()')
        products = {}
        if vulnerable_products:
            for i, product in enumerate(vulnerable_products):
                index = f"Product{i}"
                products[index] = product
        else:
            products["Products"] = None
        return products

    def exploits_links(self):
        exploit_elements = self.tree.xpath('//div[@class="content"]/div[@class="header"]/a')
        exploits = {}
        if exploit_elements:
            for z, element in enumerate(exploit_elements):
                url = element.attrib.get('href')
                name = f"Exploit{z}"
                exploits[name] = url
        else:
            exploits["Exploit"] = None
        return exploits

    def github_links(self):
        github_links = self.tree.xpath('//div[@class="content"]/div[@class="header"]/a/@href')
        github = {}
        if github_links:
            for x, glink in enumerate(github_links):
                link = f"GitHubLink{x}"
                if 'https' in link or 'http' in link:
                    github[link] = glink
                else:
                    github[link] = f'https://vulmon.com{glink}'
                
        else:
            github["GithubLink"] = None
        return github

    def reference_links(self):
        links = self.tree.xpath('//div[@class="ui list ex5"]/a')
        references = {}
        if links:
            link_urls = [link.get("href") for link in links]
            for y, url in enumerate(link_urls):
                reference = f"Reference{y}"
                references[reference] = url
        else:
            references["Reference"] = None
        return references

    def scrape_data(self):
        data = {
            "metaInfo": self.meta_info(),
            "vulnProducts": self.vuln_products(),
            "exploitsLinks": self.exploits_links(),
            "githubLinks": self.github_links(),
            "referenceLinks": self.reference_links()
        }
        return data


# if __name__ == __main__:
#     # Example usage
#     cve = "CVE-2023-25938"
#     scraper = VulmonScraper(cve)
#     scraped_data = scraper.scrape_data()
#     print(scraped_data.keys())
# import vulmonsahil
# Data = vulmonsahil.VulmonScraper("CVE-2023-25938")
# Data.scrape_data()
