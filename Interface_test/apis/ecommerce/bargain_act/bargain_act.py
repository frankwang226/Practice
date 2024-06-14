import time

import pytest

from apis.base_api import BaseApi
from utils.file_tools import FileTool
# from Interface_test.utils.file_tools import FileTool


class BargainAct(BaseApi):
    def get_act_cfg_operation_log(self, id):
        """
        查看日志
        :return:
        """
        old_url = "mall/Act/MallActCommon/GetActCfgOperationlog"
        new_url = "omcr/mallactbasic/MallActCommon/GetActCfgOperationlog"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"ActId": id, "ActTypeStr": "KJ", "PageIndex": 1, "PageSize": 10}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def create_or_update_bargain_act_cfg(self, id):
        """
        保存砍价设置
        :return:
        """
        old_url = "mall/Pro/BargainAct/CreateOrUpdateBargainActCfg"
        new_url = "omcr/mallactbasic/BargainAct/CreateOrUpdateBargainActCfg"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"BargainCountPerDay": 2, "IsBargainNotice": "true", "Id": id}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def get_bargain_act_list(self):
        """
        获取活动列表
        :return:
        """
        old_url = "mall/Pro/BargainAct/GetBargainActList"
        new_url = "omcr/mallactbasic/BargainAct/GetBargainActList"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"ShopType": "", "ShopName": "", "PageSize": 10, "PageIndex": 1, "BargainActName": "",
                   "CreateUser": "",
                   "BargainActStatus": 0, "Id": "null"}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def import_datas(self, file, shopid):
        """
        活动导入
        :return:
        """
        old_url = "mall/Pro/BargainAct/ImportDatas"
        new_url = "omcr/mallactbasic/BargainAct/ImportDatas"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        data = {"ShopType": "SH", "ShopIds": shopid}

        result = []
        urls = [old_url, new_url]

        for url in urls:
            file_path = FileTool.get_file(f"{file}.xlsx")
            with open(file_path, 'rb') as f:
                files = {'file': f}
                response = self.send("POST", url, files=files, data=data, headers=header)
                result.append(response.json())

        return result

    def set_act_disable(self, id):
        """
        活动禁用启用
        :return:
        """
        old_url = "mall/Pro/BargainAct/SetActDisable"
        new_url = "omcr/mallactbasic/BargainAct/SetActDisable"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"Id": id}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)

        return r_old.json(), r_new.json()
        # return r_new.json()

    def get_bargain_act_detail(self, id):
        """
        活动详情
        :return:
        """
        old_url = "mall/Pro/BargainAct/GetBargainActDetail"
        new_url = "omcr/mallactbasic/BargainAct/GetBargainActDetail"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"Id": id}

        r_old = self.send("GET", old_url, params=payload, headers=header)
        r_new = self.send("GET", new_url, params=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def create_bargain_act(self, productid, productname, productitemNo, shopname, shopid):
        """
        活动保存
        :return:
        """
        old_url = "mall/Pro/BargainAct/CreateBargainAct"
        new_url = "omcr/mallactbasic/BargainAct/CreateBargainAct"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        startdate = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        enddate = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + 86400 * 2))

        payload = {"Title": "wdytest", "StartOn": startdate, "EndOn": enddate,
                   "ProductId": productid, "ProductImg": "", "ProductName": productname, "ProductItemNo": productitemNo,
                   "ProductPriceRange": "0.01", "ShopType": "SH",
                   "Shops": [{"name": shopname, "value": shopid}], "BaseBargainPersonCount": 2,
                   "MiniPriceBargainPersonCount": 3, "IsVipGrade": "false", "VipGrades": [], "IsFreeShipping": "false",
                   "HelpBargainRule": {"HelpBargainRuleType": 0, "RuleValue": ""}, "ActNumType": 1,
                   "BaseBargainPersonPrice": 10, "IsActNotice": "false", "IsShowResidualStock": 0, "BargainActDtls": [
                {"ProductId": productid, "ActNum": 10, "SoldNum": 0, "IsEnable": "true", "PriceRange": "0.01"}],
                   "ValidHours": 1, "Price": 100, "MiniPrice": 1,
                   "ShareText": "Hi 能动动小手指，帮我砍一刀嘛。万分感谢~~", "ShareIco": "", "Id": "null"}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def get_act_statistic_data_by_act_id(self, id):
        """
        数据概括
        :return:
        """
        old_url = "mall/Pro/BargainAct/GetActStatisticDataByActId"
        new_url = "omcr/mallactbasic/BargainAct/GetActStatisticDataByActId"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"Id": id}

        r_old = self.send("GET", old_url, params=payload, headers=header)
        r_new = self.send("GET", new_url, params=payload, headers=header)

        return r_old.json(), r_new.json()

    def get_bargain_record_list(self, id):
        """
        砍价记录
        :return:
        """
        old_url = "mall/Pro/BargainAct/GetBargainRecordList"
        new_url = "omcr/mallactbasic/BargainAct/GetBargainRecordList"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"QueryTimeType": 1, "QueryStartOn": "", "QueryEndOn": "", "UserBargainType": 1,
                   "QueryUserInfoType": 2, "UserInfo": "", "PageIndex": 1, "PageSize": 10, "bargainType": 0,
                   "BargainActivityId": id}

        r_old = self.send("GET", old_url, params=payload, headers=header)
        r_new = self.send("GET", new_url, params=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def export_bargain_record(self, id):
        """
        产出记录导出
        :return:
        """
        old_url = "mall/Pro/BargainAct/ExportBargainRecord"
        new_url = "omcr/mallactbasic/BargainAct/ExportBargainRecord"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"BargainActivityId": id}

        r_old = self.send("GET", old_url, params=payload, headers=header)
        r_new = self.send("GET", new_url, params=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def get_bargain_act_dtl(self, id):
        """
        获取活动数量
        :return:
        """
        old_url = "mall/Pro/BargainAct/GetBargainActDtl"
        new_url = "omcr/mallactbasic/BargainAct/GetBargainActDtl"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"BargainActId": id}

        r_old = self.send("GET", old_url, params=payload, headers=header)
        r_new = self.send("GET", new_url, params=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def update_bargain_act_dtl(self, bargainactid, actid):
        """
        更新调整活动数量
        :return:
        """
        old_url = "mall/Pro/BargainAct/UpdateBargainActDtl"
        new_url = "omcr/mallactbasic/BargainAct/UpdateBargainActDtl"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"BargainActId": bargainactid, "ActDtl": [{"Id": actid, "ActNum": 50}]}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def get_act_stock_record(self, id):
        """
        调整库存记录
        :return:
        """
        old_url = "mall/Pro/BargainAct/GetActStockRecord"
        new_url = "omcr/mallactbasic/BargainAct/GetActStockRecord"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"BargainActId": id, "PageIndex": 1, "PageSize": 10}

        r_old = self.send("GET", old_url, params=payload, headers=header)
        r_new = self.send("GET", new_url, params=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def export_bargain_list(self):
        """
        导出活动列表
        :return:
        """
        old_url = "mall/Pro/BargainAct/ExportBargainList"
        new_url = "omcr/mallactbasic/BargainAct/ExportBargainList"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"BargainActName": "", "BargainActStatus": 0, "CreateUser": "", "ShopName": "", "ShopType": ""}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def get_bargain_act_shop_info(self, id):
        """
        获取砍价活动关联的门店列表信息
        :return:
        """
        old_url = "mall/Pro/BargainAct/GetBargainActShopInfo"
        new_url = "omcr/mallactbasic/BargainAct/GetBargainActShopInfo"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"PageSize": 10, "PageIndex": 1, "BargainActivityId": id, "ShopName": ""}

        r_old = self.send("GET", old_url, params=payload, headers=header)
        r_new = self.send("GET", new_url, params=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def get_bargain_act_list_link(self):
        """
        砍价活动小程序二维码
        :return:
        """
        old_url = "mall/Pro/BargainAct/GetBargainaActListLink"
        new_url = "omcr/mallactbasic/BargainAct/GetBargainaActListLink"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {}

        r_old = self.send("GET", old_url, params=payload, headers=header)
        r_new = self.send("GET", new_url, params=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def get_bargain_act_config_info(self):
        """
        获取活动配置信息
        :return:
        """
        old_url = "mall/Pro/BargainAct/GetBargainActConfigInfo"
        new_url = "omcr/mallactbasic/BargainAct/GetBargainActConfigInfo"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {}

        r_old = self.send("GET", old_url, params=payload, headers=header)
        r_new = self.send("GET", new_url, params=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def edit_bargain_act(self, productid, productname, productitemNo, shopname, shopid, actid, actdtlid):
        """
        编辑砍价活动
        :return:
        """
        old_url = "mall/Pro/BargainAct/EditBargainAct"
        new_url = "omcr/mallactbasic/BargainAct/EditBargainAct"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"Title": "wdytest", "StartOn": "2024-06-06 20:50:14", "EndOn": "2024-06-08 20:50:14",
                   "ProductId": productid, "ProductImg": "", "Price": 100, "ProductName": productname,
                   "ValidHours": 1, "MiniPrice": 1, "BaseBargainPersonCount": 2, "MiniPriceBargainPersonCount": 3,
                   "IsVipGrade": "false", "VipGrades": [], "HelpBargainRule": {"HelpBargainRuleType": 0, "RuleValue": ""},
                   "ShopType": "SH", "Shops": [{"Name": shopname, "Value": shopid}], "IsFreeShipping": "false",
                   "ShareText": "Hi 能动动小手指，帮我砍一刀嘛。万分感谢~~", "ShareIco": "", "IsEnable": "false",
                   "IsCan": "false", "ProductItemNo": productitemNo, "ProductPriceRange": "82.9", "CreateUser": "wdy",
                   "CreateDate": "2024-06-06 20:50:16", "CreateUserCode": "WDY", "UserId": 12175923,
                   "BaseBargainPersonPrice": 10, "ActNumType": 1, "IsShowResidualStock": 0, "BargainActDtls": [
                {"Id": actdtlid, "ProductId": productid, "BarId": 0, "ActNum": 10, "SoldNum": 0, "PriceRange": "82.9",
                 "IsEnable": "true", "SkuAttrValsEx": "null"}], "IsActNotice": "false", "HotRecommend": "None",
                   "HotRecommendList": "null", "isOldItem": 1, "Id": actid}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def set_act_enable(self, id):
        """
        设置活动启用
        :return:
        """
        old_url = "mall/Pro/BargainAct/SetActEnable"
        new_url = "omcr/mallactbasic/BargainAct/SetActEnable"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"Id": id}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()


if __name__ == '__main__':
    base = BargainAct("tp")
    # base.get_act_cfg_operation_log()
    # base.create_or_update_bargain_act_cfg()
    base.set_act_disable(280938)