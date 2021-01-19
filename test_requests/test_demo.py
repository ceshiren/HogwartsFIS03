#导入requests库
import requests
def test_demo():
    r = requests.request(method="GET", url= "https://httpbin.testing-studio.com/get")
    print(r.json())
    print(r.status_code)