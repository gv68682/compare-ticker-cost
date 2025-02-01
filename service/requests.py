import finnhub
#pip3 install finnhub--python
#pip3 install urllib3==1.26.6
#NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020

def makeConnection(apiKey):
    c =finnhub.Client(api_key=apiKey)
    return c



def makeConnectionBit():
    print("Not required")
    