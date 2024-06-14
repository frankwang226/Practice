# from Interface_test.apis.base_api import BaseApi
# from Interface_test.utils.file_tools import FileTool
import time

from apis.base_api import BaseApi
from utils.file_tools import FileTool


class ProductGroupBy(BaseApi):
    def get_act_cfg_operation_log(self, id):
        """
        查看日志
        :return:
        """
        old_url = "mall/Act/MallActCommon/GetActCfgOperationlog"
        new_url = "omcr/mallactbasic/MallActCommon/GetActCfgOperationlog"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"ActId": id, "ActTypeStr": "MS", "PageIndex": 1, "PageSize": 10}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def get_prd_group_buy_list(self):
        """
        列表数据查询
        :return:
        """
        old_url = "mall/Pro/ProductGroupBuy/GetPrdGroupBuyList"
        new_url = "omcr/mallactbasic/ProductGroupBuy/GetPrdGroupBuyList"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"PageIndex": 1, "PageSize": 20, "Type": 0, "ProName": "", "CreateUser": "", "ApplyShop": "",
                   "ShopType": "", "Id": ""}

        r_old = self.send("GET", old_url, params=payload, headers=header)
        r_new = self.send("GET", new_url, params=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def export_act_data(self):
        """
        数据导出
        :return:
        """
        old_url = "mall/Pro/ProductGroupBuy/ExportActData"
        new_url = "omcr/mallactbasic/ProductGroupBuy/ExportActData"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"PageIndex": 1, "PageSize": 20, "Type": 0, "ProName": "", "CreateUser": "", "ApplyShop": "",
                   "ShopType": ""}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def import_datas(self, file):
        """
        导入模版
        :return:
        """
        old_url = "mall/Pro/ProductGroupBuy/ImportDatas"
        new_url = "omcr/mallactbasic/ProductGroupBuy/ImportDatas"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        data = {"ShopType": "SH", "ShopIds": 21172697}

        result = []
        urls = [old_url, new_url]

        for url in urls:
            file_path = FileTool.get_file(f"{file}.xlsx")
            with open(file_path, 'rb') as f:
                files = {'file': f}
                response = self.send("POST", url, files=files, data=data, headers=header)
                result.append(response.json())

        return result

    def batch_enable_or_disabled_group_buy(self, id, type):
        """
        批量启用、禁用
        :return:
        """
        old_url = "mall/Pro/ProductGroupBuy/BatchEnableOrDisabledGroupBuy"
        new_url = "omcr/mallactbasic/ProductGroupBuy/BatchEnableOrDisabledGroupBuy"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"Type": type, "ItemIds": [id]}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def enable_or_disabled_group_buy(self, id, type):
        """
        启用、禁用
        :return:
        """
        old_url = "mall/Pro/ProductGroupBuy/EnableOrDisabledProdGroupBuy"
        new_url = "omcr/mallactbasic/ProductGroupBuy/EnableOrDisabledProdGroupBuy"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"Id": id, "Type": type}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def get_by_id(self, id):
        """
        获取详情
        :return:
        """
        old_url = "mall/Pro/ProductGroupBuy/GetById"
        new_url = "omcr/mallactbasic/ProductGroupBuy/GetById"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"Id": id}

        r_old = self.send("GET", old_url, params=payload, headers=header)
        r_new = self.send("GET", new_url, params=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def save_data(self, shopid, itemid, itemname):
        """
        活动保存
        :return:
        """
        old_url = "mall/Pro/ProductGroupBuy/SaveData"
        new_url = "omcr/mallactbasic/ProductGroupBuy/SaveData"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        startdate = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        enddate = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + 86400 * 2))

        payload = {"ApplyShop": shopid, "actTag": "秒杀", "CanUseCoupon": "false",
                   "NotAllowUseBonusForCash": "false",
                   "AllowBuyAtOriginalPrice": "false", "BegDate": startdate,
                   "EndDate": enddate,
                   "ShopType": "shop", "ItemId": itemid, "ItemName": itemname, "PictureUrl": "",
                   "RuleType": "PD", "SalePrice": 0.01, "Id": 0, "GroupBuyDtlList": [], "GroupBuyPrice": 1,
                   "Stocks": 10, "SalesNum": 0, "ActTags": "秒杀"}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def get_act_shop_infos(self, id):
        """
        获取活动门店信息
        :return:
        """
        old_url = "mall/Pro/ProductGroupBuy/GetActShopInfos"
        new_url = "omcr/mallactbasic/ProductGroupBuy/GetActShopInfos"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"ShopCode": "", "ActId": id, "PageIndex": 1, "PageSize": 5}

        r_old = self.send("GET", old_url, params=payload, headers=header)
        r_new = self.send("GET", new_url, params=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()
