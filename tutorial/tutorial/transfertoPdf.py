import os
import pdfkit
from bs4 import BeautifulSoup as bs
import lxml

os.chdir("F:/")
root_url = "https://docs.scrapy.org/en/latest"

def judge_html(name):
    if '.html' in name:
        return True
    else:
        return False


chapters = list(filter(judge_html, os.listdir("F:/")))


chapters.sort(key=os.path.getatime, reverse=True)
for chapter in chapters:
    html_doc = open(chapter, "r", encoding="utf-8", errors="ignore")
    soup = bs(html_doc.read(), "lxml")
    html_doc.close()
    # for a in soup.select("a.headerlink"):
    #     a.decompose()
    # if soup.find_all("img"):
    #     for img in soup.find_all("img"):
    #         img["src"] = root_url + img["src"].split("..")[-1]
    #         print(img)
    # for a in soup.select("a"):
    #     del a['href']
    html_doc = open(chapter, "w", encoding="utf-8", errors="ignore")
    html_doc.write(str(soup))
    html_doc.close()


pdfkit.from_file(chapters, "F:/demo.pdf")
