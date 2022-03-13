import pandas as pd
from Product import Product
import pygsheets
from constants import *

def write_to_gsheet(service_file_path, spreadsheet_id, sheet_name, data_df):
    gc = pygsheets.authorize(service_file=service_file_path)
    sh = gc.open_by_key(spreadsheet_id)
    try:
        sh.add_worksheet(sheet_name)
    except:
        pass
    wks_write = sh.worksheet_by_title(sheet_name)
    wks_write.clear('A1',None,'*')
    wks_write.set_dataframe(data_df, (1,1), encoding='utf-8', fit=True)
    wks_write.frozen_rows = 1

def main():
    urls = pd.read_excel("URLs.xlsx", header=None)
    urls = urls[0].tolist()

    products = []
    for url in urls:
        prod = Product(url)
        if(prod._isPageHasProduct()):
            products.append(prod.toDictionary())
    dataframe = pd.DataFrame.from_records(products)
    write_to_gsheet('credentials.json', GOOGLE_SHEET_ID, GOOGLE_SHEET_NAME, dataframe)

if __name__ == '__main__':
    main()