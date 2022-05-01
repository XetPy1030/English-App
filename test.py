import pandas as pd
from pprint import pprint

excel = pd.read_excel("words.xlsx").to_dict()

words = [{"word": "", "translate": "", "image": "", "other": ""}]

titles = excel.keys()
for i in range(len(titles)):
    pass