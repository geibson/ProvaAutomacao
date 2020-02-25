import requests

def test_Api():
    url = 'http://5b847b30db24a100142dce1b.mockapi.io/api/v1/simulador'    
    resp = requests.get(url)           
    print(resp.text[0:1])
    print("    ",resp.text[1:8])
    print("    ",resp.text[8:42])
    print("    ",resp.text[42:83])
    print(resp.text[83:])

  
