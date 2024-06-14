import hashlib
import logging

import requests

from utils.file_tools import FileTool


class BaseApi:
    def __init__(self, env):
        logging.info(f"env:{env}")
        yaml_data = FileTool.read_yaml("config")
        # env = yaml_data.get("env").get("default")
        self.baseurl = yaml_data.get("env").get("baseurl").get(env)
        self.tag = yaml_data.get("tag")
        self.brandId = yaml_data.get("env").get("cookies").get(env).get("brandId")
        self.userMobile = yaml_data.get("env").get("cookies").get(env).get("userMobile")
        self.password = yaml_data.get("env").get("cookies").get(env).get("password")
        self.userId = yaml_data.get("env").get("cookies").get(env).get("userId")
        self.ssoId = yaml_data.get("env").get("cookies").get(env).get("ssoId")
        self.accountUrl = yaml_data.get("env").get("cookies").get(env).get("accountUrl")
        self.crmHost = yaml_data.get("env").get("cookies").get(env).get("crmHost")
        self.cookies = self.getcookie(brandId=self.brandId, userMobile=self.userMobile, password=self.password,
                                      userId=self.userId, ssoId=self.ssoId, accountUrl=self.accountUrl,
                                      crmHost=self.crmHost)
        self.cookies["cookie"] += f"ezr-env-tag={self.tag}"

    # yaml_data = FileTool.read_yaml("config")
    # BaseUrl = yaml_data.get("baseurl").get(env)
    # BaseUrl = "https://crm-q1.ezrpro.com/api/"
    # BaseUrl = "https://crm-tp.ezrpro.com/api/"

    def getVerify(self, path, userId):
        """
        pc接口的V
        """
        # requests.packages.urllib3.disable_warnings()
        if userId is None:
            global login_config
            # load_login_config()  # 重新加载 login_config
            userId = login_config["userId"]
        payload = {}
        v_header = {'cookie': 'opt.authorize=L4jNV1nhZMO9qtdTEEXUcXYE5o9Syies'}
        v_url = f'https://tester.ezrpro.work/api/OpenApi/GetV?userId={userId}&apiPath={path}'
        value = requests.request("GET", v_url, headers=v_header, data=payload, verify=False)
        # print(value.json())
        v = value.json()["data"]
        # print(v)
        return v

    def getcookie(self, brandId=None, userMobile=None, password=None, userId=None, ssoId=None, accountUrl=None,
                  crmHost=None):
        # if brandId is None:
        #     global login_config
        #     # load_login_config()  # 重新加载 login_config
        #     brandId = login_config["brandId"]
        #     userMobile = login_config["userMobile"]
        #     password = login_config["password"]
        #     userId = login_config["userId"]
        #     ssoId = login_config["ssoId"]
        #     accountUrl = login_config["accountUrl"]
        #     crmHost = login_config["crmHost"]
        # try:
        #     if (not accountUrl or not crmHost) and cloud:
        #         sites = cloud_map.get(cloud.lower(), None)
        #     if sites:
        #         accountUrl = sites[0]
        #         crmHost = sites[1]
        #         else:
        #             raise "登陆PC传参异常，没有传递accountUrl和crmHost 或者没有传递登陆的云"

        # requests.packages.urllib3.disable_warnings()
        # 密码进行MD5加密
        md5 = hashlib.md5()
        md5.update(password.encode('utf8'))
        md5_pass_world = md5.hexdigest()
        # 1. 进入系统接口
        account_res = requests.get(accountUrl)
        login_uid = account_res.cookies.get("login_uid")
        wx_log_state = account_res.cookies.get("wx_log_state")
        login_cookie = 'login_uid=' + login_uid + ";" + "wx_log_state=" + wx_log_state
        # 2.请求登录接口
        login_url = f'{accountUrl}/Login/Login'
        data = f'LoginType=0&UserCode={userMobile}&UserPwd={md5_pass_world}'
        headers = {
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'cookie': login_cookie
        }
        login_res = requests.post(login_url, data=data, headers=headers, verify=False)
        # 3.获取登录后的cookie
        login_sid = login_res.cookies.get("login_sid")
        # 4. 选择品牌接口
        brand_change_url = f'{accountUrl}/Login/BrandChange?brandId={brandId}&userId={userId}&rturl='
        headers = {
            'cookie': f'login_uid={login_uid}; wx_log_state={wx_log_state};'
                      f'login_sid={login_sid}'
        }
        requests.get(brand_change_url, headers=headers, verify=False)
        # 4请求login接口
        crm_url = f'{crmHost}/login?tokenId={login_sid}'
        payload = {}
        headers = {'cookie': f'pcl_brandid={brandId}'}
        requests.request("GET", crm_url, headers=headers, data=payload, verify=False)
        # 5请求测试接口
        # url = f"{crmHost}/api/crm/cms/SysBrandNotice/HaveNoticeRedAlarm"
        # payload = {}
        # headers = {
        #     'cookie': f'pcl_sid={login_sid};pcl_brandid={brandId};pcl_buid={ssoId};'
        # }
        # response = requests.request("GET", url, headers=headers, datas=payload, verify=False)
        # print(response.text)
        # print("--------9")

        req_headers = {
            'cookie': f'pcl_sid={login_sid};pcl_brandid={brandId};pcl_buid={ssoId};',
        }
        # print(req_headers)
        # print("--------")
        #     EZR.cookie = req_headers
        #     EZR.vUserId = userId
        #     EZR.api_platform_type = 'pc'
        return req_headers
        # except Exception as ex:
        #     log.info(f"👀登陆PC失败~~:{ex}")
        #     EZR.cookie = {}
        #     return {}

    def send(self, method, url, **kwargs):
        requests.packages.urllib3.disable_warnings()
        url = self.baseurl + url
        res = requests.request(method=method, url=url, **kwargs, verify=False)
        return res

# if __name__ == '__main__':
#     base = BaseApi()
#     base.getcookie(brandId=739, userMobile="13524204498", password="qwer1234", userId=21000098, ssoId=220467,
#                    accountUrl="https://account-demo.ezrpro.com", crmHost="https://crm-q1.ezrpro.com")
