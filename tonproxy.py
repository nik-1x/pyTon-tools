import requests
from requests import Response

def proxied_get_request(url) -> Response:
    
    if url.startswith('ton://'):
        url = url.replace('ton://', 'http://')

    elif url.startswith('adnl://'):
        url = url.replace('adnl://', 'http://')

    elif not url.startswith('http://'):
        url = 'http://' + url
        
    proxy_settings = {
        "1": "in1.ton.org:8080",
        "2": "in2.ton.org:8080",
        "3": "in3.ton.org:8080"
    }
    try:
        data = requests.get(url, proxies={'http': proxy_settings["1"]})
        return data
    except:
        try:
            data = requests.get(url, proxies={'http': proxy_settings["2"]})
            return data
        except:
            data = requests.get(url, proxies={'http': proxy_settings["3"]})
            return data

        
            
request = proxied_get_request('adnl://utoljjye6y4ixazesjofidlkrhyiakiwrmes3m5hthlc6ie2h72gllt.adnl/')
if request is not False:
    print("==== Result ====")
    print(request.content.decode())
    print("================")


    
