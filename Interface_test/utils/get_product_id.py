# from Interface_test.apis.base_api import BaseApi
# from Interface_test.utils.file_tools import FileTool
import logging

from apis.base_api import BaseApi
from utils.file_tools import FileTool


class GetProduct(BaseApi):

    # def __init__(self, env):
    #     yaml_data = FileTool.read_yaml("cookie")
    #     self.tag = yaml_data.get("tag")
    #     self.brandId = yaml_data.get("cookies").get(env).get("brandId")
    #     self.userMobile = yaml_data.get("cookies").get(env).get("userMobile")
    #     self.password = yaml_data.get("cookies").get(env).get("password")
    #     self.userId = yaml_data.get("cookies").get(env).get("userId")
    #     self.ssoId = yaml_data.get("cookies").get(env).get("ssoId")
    #     self.accountUrl = yaml_data.get("cookies").get(env).get("accountUrl")
    #     self.crmHost = yaml_data.get("cookies").get(env).get("crmHost")
    #     self.cookies = self.getcookie(brandId=self.brandId, userMobile=self.userMobile, password=self.password,
    #                                   userId=self.userId, ssoId=self.ssoId, accountUrl=self.accountUrl,
    #                                   crmHost=self.crmHost)
    #     self.cookies["cookie"] += f"ezr-env-tag={self.tag}"
    def get_product_id(self):
        """
        获取商品id
        :return:
        """

        url = "mall/Pro/Product/GetSelectList"
        header = {"v": self.getVerify(url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"PageIndex": 1, "PageSize": 9, "Name": "", "BeginSalePrice": "", "EndSalePrice": "",
                   "IsOnSale": "false", "GroupyId": "", "CategoryId": "", "ProductBrandId": "", "Status": 0,
                   "AttrCodes": "", "ProdType": ""}

        res = self.send("GET", url, params=payload, headers=header)
        product_id = res.json().get("Data").get("PagedList")[0].get("Id")
        logging.info(f"取出的商品id为{product_id}")
        return product_id

if __name__ == '__main__':
    base = GetProduct("tp")
    base.get_product_id()