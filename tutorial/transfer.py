from bs4 import BeautifulSoup as bs
import lxml
import pdfkit

# with open("F:/beautifulsoup.html", "rb") as book:
#     soup = bs(book.read().decode('utf-8', errors='ignore'), "lxml")
#
# for a in soup.select("a"):
#     del a["href"]
#
# for pat in soup.select("a.headerlink"):
#     pat.decompose()
#
# with open("F:output.html", "wb") as out:
#     out.write(str(soup).encode('utf-8'))

pdfkit.from_file("F:/output.html", "F:/out.pdf")
