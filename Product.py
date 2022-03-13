from bs4 import BeautifulSoup as bs
import requests as req
import re
from constants import *

class Product:
    def __init__(self, url):
        self.url = BASE_URL + url
        self.soup = bs(req.get(self.url).content, 'html.parser')
        
    def _isPageHasProduct(self):
        flag = self.soup.find("div", attrs={"id": "productRight"})
        if(flag == None):
            return False
        return True
    def _isProductHasDiscount(self):
        price_section = self.soup.find("div", attrs= {"class": "priceLine"})
        if(price_section != None):
            if(len(price_section.find_all("span")) > 2):
                self.hasDiscount = True
            else:
                self.hasDiscount = False
        else:
            self.hasDiscount = False
        return self.hasDiscount
        
    def getProductCode(self):
        product_code_section = self.soup.find("div", attrs={"class": "product-feature-content"})
        if(product_code_section != None):
            self.productCode = self.clean_text(list(product_code_section.children)[-1])
        else:
            self.productCode = "-"
        return self.productCode
    def getProductName(self):
        # ürün ismi -> h1 id:product-name
        self.name = self.clean_text(self.soup.find("h1", attrs={"id": "product-name"}).text)
        return self.name
    def getOffer(self):
        return "-"
    def getProductPrice(self):
        # ürün fiyat -> span class:product-price
        price_section = self.soup.find("span", attrs={"class": "product-price"})
        if(price_section != None):
            self.productPrice = self.clean_text(price_section.text)
            return self.productPrice
        return "STOKTA YOK"
    def getSalePrice(self):
        return "-"
    def getProductAvailability(self):
        self.productAvailability = [a.p.text for a in self.soup.find("div", attrs= {"class": "new-size-variant"}).find_all("a") if a["class"][-1] != "passive"]
        if(len(self.productAvailability) > 0):
            return self.productAvailability
        return "-"
    def getProductUnavailability(self):
        self.productUnavailability = [a.p.text for a in self.soup.find("div", attrs= {"class": "new-size-variant"}).find_all("a") if a["class"][-1] == "passive"]
        if(len(self.productUnavailability) > 0):
            return self.productUnavailability
        return "-"
    def getProductRate(self):
        star_section = self.soup.find("span", attrs={"class": "ranked-average-star2"})
        if(star_section != None):
            if(star_section.text != ""):
                self.productRate = self.clean_text(star_section.text)
            else:
                self.productRate = "-"
        else:
            self.productRate = "-"
        return self.productRate
    def toDictionary(self):
        if(self._isProductHasDiscount()):
            return {
                "Ürün Kodu": self.getProductCode(),
                "Ürün İsmi": self.getProductName(),
                "İndirim Oranı": self.getOffer(),
                "Ürün Fiyatı": self.getProductPrice(),
                "İndirimsiz Fiyatı": self.getSalePrice(),
                "Mevcut Olmayan Bedenler": self.getProductUnavailability(),
                "Mevcut Bedenler": self.getProductAvailability(),
                "Ürün Puanı": self.getProductRate()
            }
        else:
            return {
                "Ürün Kodu": self.getProductCode(),
                "Ürün İsmi": self.getProductName(),
                "Ürün Fiyatı": self.getProductPrice(),
                "Mevcut Olmayan Bedenler": self.getProductUnavailability(),
                "Mevcut Bedenler": self.getProductAvailability(),
                "Ürün Puanı": self.getProductRate()
            }
                                
    @staticmethod
    def clean_text(text):
        unwanteds = ["\n"]
        for unwanted in unwanteds:
            text = text.replace(unwanted, "")
        text = re.sub(r"^\s+|\s+$", "", text)
        return text