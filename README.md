# AnalyticaHouse Scraper Assignment

## Proje Kurulumu
Projeyi bilgisayarınıza klonladıktan sonra komut istemcisinde, projenin olduğu dizine gidin.

Proje dizinine gittikten sonra gerekli bağımlılıkları indirmek için aşağıda belirtilen komutu çalıştırın.
```
pip install requirements.txt
```
Aynı dizin içerisinde aşağıdaki kodu çalıştırarak programı çalıştırabilirsiniz.
```
py main.py
```

## Gereksinimler
- Python
- BeautifulSoup https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- Pygsheets https://pygsheets.readthedocs.io/en/stable/
- Requests https://docs.python-requests.org/en/latest/
- Regex https://docs.python.org/3/library/re.html
- Pandas https://pandas.pydata.org/docs/

## Proje Raporu
https://docs.google.com/spreadsheets/d/1gRUx5WAtTZaA9MWU3J4PRUKBmEAYt9ZbOgv1SJNc2Io

## Proje Öğrenimleri
Bu projede bir python dosyası üzerinde gerçek zamanlı olarak Google Sheets ile çalışma deneyimi elde ettim.

## Sorular

### Eğer 10.000 URL gezmeniz gerekseydi, işlemi tamamlamak saatler sürerdi. Bu işlemi hızlandırmak için ne yapılabilir?
Verilen URLlerde parse işlemi gerçekleştirmeden önce o sayfanın bir ürün sayfası olup olmadığı kontrol edilir. URL, bir ürün sayfasını işaret ediyorsa parse işlemi gerçekleştirilir. Arama sayfası veya ana sayfa gibi sayfalarda parse işlemi uygulanmayacağından, işlem bu şekilde hızlandırılır.

### Bu işlemi her gün çalıştırmak için ne kullanmak veya ne yapmak gerekir? 
İlgili python projesi bir flask uygulamasına çevrilerek sunucuda çalıştırılabilir. Böylece bir zamanlama koşulu uygulayarak, bu işlem otomatize edilebilir.

### API nedir? Nasıl çalışır?
API (Application Programming Interface), kendine ait veriler ve çalışma prensipleri ile geliştirilmiş uygulamaların, birbirileri ile iletişime geçerek çalışmasını mümkün kılan yazılımlardır.
Sunucudan alınan verinin kullanıcının anlayabileceği şekilde anlamlı hale getirir.