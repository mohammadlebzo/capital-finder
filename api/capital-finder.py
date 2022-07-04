from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


def q_handler(dic, key_word, url):
    q_key = dic[key_word]
    res = requests.get(url + q_key)
    data = res.json()
    return data

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        output = ''

        if 'country' in dic:
            # country = dic['country']
            # url = 'https://restcountries.com/v3.1/name/'
            # r = requests.get(url + country)
            # data = r.json()
            for items in q_handler(dic, "country", "https://restcountries.com/v3.1/name/"):
                output = f"The capital of {items['name']['common']} is {items['capital'][0]}."
            message = output

        elif 'capital' in dic:
            # capital = dic['capital']
            # url = 'https://restcountries.com/v2/capital/'
            # r = requests.get(url + capital)
            # data = r.json()
            for items in q_handler(dic, "capital", "https://restcountries.com/v2/capital/"):
                output = f"{items['capital'][0]} is the capital of {items['name']['common']}."
            message = output

        else:
            message = "Please provide me with a word"

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())

        return
