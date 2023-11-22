# This function extract the BPD stage from GEO dataset site
# Base Site => https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE121097
# Dataset site => https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc={Sample ID}

import requests
from bs4 import BeautifulSoup

def scrap_data(sample_id):
    stage_dict = {}
    base_link = "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc="
    URL = base_link + sample_id
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    element = soup.find(string = lambda text: "bpd:" in text)

    if element:
        bpd_stage = element.text.split(":")[-1].strip()
        print(sample_id + " : " + bpd_stage)
        return bpd_stage
        
    else:
        print(sample_id + " : Stage Not Found")
        return 0
