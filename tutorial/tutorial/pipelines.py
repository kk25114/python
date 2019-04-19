# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pdfkit
from bs4 import BeautifulSoup as bs

class TutorialPipeline(object):
    template = """
    <html>
      <head>
        <meta name="pdfkit-page-size" content="Legal"/>
        <meta name="pdfkit-orientation" content="Landscape"/>
      </head>
      <body>
      {}
      </body>
      </html>
    """
    files = []

    def process_item(self, item, spider):
        with open('F:/' + item['title']+'.html', 'wb+') as f:
            html = self.template.format(item['content'])
            soup = bs(html, "lxml")
            if soup.find_all("img"):
                for img in soup.find_all("img"):
                    img["src"] = "https://docs.scrapy.org/en/latest" + img["src"].split("..")[-1]

            f.write(soup.text.encode('utf-8'))
            self.files.append('F:/' + item['title']+'.html')
        return item


