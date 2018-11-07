import logging

import requests
from bs4 import BeautifulSoup
from collections import Counter

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python Website Parser function processed a request.')

    url = req.params.get('url')

    logging.info(f"Received request for target URL {url}")

    if url:

        resultText = ""

        website = requests.get(url)
        soup = BeautifulSoup(website.content, 'html.parser')
        h1 = [''.join(s.findAll(text=True))for s in soup.findAll('h1')]
        if h1:
            resultText += h1[0] + '\n\n'    
        text = [''.join(s.findAll(text=True))for s in soup.findAll('p')]
        for item in text:
            resultText += item
        return func.HttpResponse(f"{resultText}")
    else:
        return func.HttpResponse(
             "Please pass a url on the query string",
             status_code=400
        )
