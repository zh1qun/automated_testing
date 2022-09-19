import requests


class ApiRequest(object):
    def __init__(self):
        pass

    # 封装http
    def send_request(self, method, url, data=None, headers=None, cookies=None, json=None, files=None,
                     auth=None, timeout=None, proxies=None, verify=False, cert=None):  # 不开启SSL证书验证就verify=False
        res = requests.request(method=method, url=url, data=data, headers=headers, cookies=cookies, json=json,
                               files=files,
                               auth=auth, timeout=timeout, proxies=proxies, verify=verify, cert=cert)

        return res
