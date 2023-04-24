import unittest
from bs4 import BeautifulSoup

import requests

app_ip = "http://127.0.0.1:8080"

def post_to_app(input_text):
    data = {
        'content': input_text
    }
    r = requests.post(app_ip, data=data)
    soup = BeautifulSoup(r.content, 'html.parser')
    output_text = soup.find(id="output").text
    return output_text

class TestCensorTextFlaskApp(unittest.TestCase):

    def test_upper(self):
        input_text = "In this text the name John should be censored."
        output_text = post_to_app(input_text)
        assert("John" not in output_text)
        assert("████" in output_text)
    
    def test_random_ascii(self):
        input_text = "h0MkVi^Ia&.rHjEI>xa[QH$xD;)GdHc.aqkZ6~C)WEE}Bm6UaBDB&N<Yc(je!cs"
        output_text = post_to_app(input_text)
        assert(len(output_text) != 0)

    def test_empty_string(self):
        input_text = ""
        output_text = post_to_app(input_text)
        assert(output_text == "")
    


if __name__ == '__main__':
    unittest.main()