import time

from apis.base_api import BaseApi
from utils.file_tools import FileTool


# from Interface_test.apis.base_api import BaseApi
# from Interface_test.utils.file_tools import FileTool


class NewUserExclusive(BaseApi):
    def get_act_cfg_operation_log(self, actid):
        """
        查看日志
        :return:
        """
        old_url = "mall/Act/MallActCommon/GetActCfgOperationlog"
        new_url = "omcr/mallactbasic/MallActCommon/GetActCfgOperationlog"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"ActId": actid, "ActTypeStr": "NUEL", "PageIndex": 1, "PageSize": 10}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def get_list(self, status):
        """
        查看活动配置
        :return:
        """
        old_url = "mall/Pro/NewUserExclusive/GetList"
        new_url = "omcr/mallactbasic/NewUserExclusive/GetList"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"ActName": "", "CreateUser": "", "StatusString": status, "ImportType": -1, "PageIndex": 1,
                   "PageSize": 10, "Id": 0, "ShopType": "", "ShopIdString": ""}

        r_old = self.send("GET", old_url, params=payload, headers=header)
        r_new = self.send("GET", new_url, params=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def save_data_new(self, shopid):
        """
        保存活动配置列表
        :return:
        """
        old_url = "mall/Pro/NewUserExclusive/SaveDataNew"
        new_url = "omcr/mallactbasic/NewUserExclusive/SaveDataNew"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        startdate = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        enddate = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + 86400 * 2))

        payload = {"Id": "0", "IsDisabled": "true", "ActName": "wdytest", "ActTag": "新人专享",
                   "ActBeginDate": startdate, "ActEndDate": enddate, "ShopType": "SH",
                   "ApplyShop": shopid, "IsShowProIngActView": "true", "IsShowProPreView": "false",
                   "IsLimitSale": "false", "CanUseCoupon": "false", "CouponIds": "", "CouponList": [],
                   "NotUsePetCard": "true", "ProJoinType": "OF",
                   "DiscountActOthercfg": {"SubjectHeadModel": 2, "SubjectHeadBgImage": "",
                                           "SubjectHeadBgColor": "#FFFFFF", "SubjectAdImage": "",
                                           "BackGroundColor": "#F5F5F5", "ShowCountDownType": "true",
                                           "ListShowStyle": 0,
                                           "IsShowActInst": "true", "ActInstructions": "null", "ShareGuideText": "",
                                           "ShareGuideImage": "https://assets-img.ezrpro.com/mobile/img/goods/newcomersActivities-share-default.png",
                                           "BtnRemindBgColor": "#FFBE00", "BtnRemindTextColor": "#FFFFFF", "Id": 0}}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def get_by_id(self, id):
        """
        获取单个活动配置
        :return:
        """
        old_url = "mall/Pro/NewUserExclusive/GetById"
        new_url = "omcr/mallactbasic/NewUserExclusive/GetById"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"Id": id}

        r_old = self.send("GET", old_url, params=payload, headers=header)
        r_new = self.send("GET", new_url, params=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def set_disabled(self, payload):
        """
        活动启动
        :return:
        """
        old_url = "mall/Pro/NewUserExclusive/SetDisabled"
        new_url = "omcr/mallactbasic/NewUserExclusive/SetDisabled"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()
        # return r_new.json()

    def save_act_pro_info(self, actid, itemid):
        """
        添加商品
        :return:
        """
        old_url = "mall/Pro/NewUserExclusive/SaveActProInfo"
        new_url = "omcr/mallactbasic/NewUserExclusive/SaveActProInfo"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"ActId": actid, "ItemIds": [itemid], "SpuOrSku": 1}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def get_act_pro_list_page(self, actid):
        """
        查询商品
        :return:
        """
        old_url = "mall/Pro/NewUserExclusive/GetActProListPage"
        new_url = "omcr/mallactbasic/NewUserExclusive/GetActProListPage"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"ProSearchWord": "", "ActId": actid, "SpuOrSku": 0, "PageIndex": 1, "PageSize": 5}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def import_act_pros(self, actid, file):
        """
        导入商品
        :return:
        """
        old_url = "mall/Pro/NewUserExclusive/ImportActPros"
        new_url = "omcr/mallactbasic/NewUserExclusive/ImportActPros"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        data = {"actId": actid, "Pagesize": 5}

        result = []
        urls = [old_url, new_url]

        for url in urls:
            file_path = FileTool.get_file(f"{file}.xlsx")
            with open(file_path, 'rb') as f:
                files = {'file': f}
                response = self.send("POST", url, files=files, data=data, headers=header)
                # print(response.json())
                result.append(response.json())

        return result

    def export_act_pros(self, actid):
        """
        导出商品
        :return:
        """
        old_url = "mall/Pro/NewUserExclusive/ExportActPros"
        new_url = "omcr/mallactbasic/NewUserExclusive/ExportActPros"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"ActId": actid, "SpuOrSku": 0, "ProSearchWord": ""}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def batch_cancel_act_pros(self, actid, itemid):
        """
        批量删除
        :return:
        """
        old_url = "mall/Pro/NewUserExclusive/BatchCancleActPros"
        new_url = "omcr/mallactbasic/NewUserExclusive/BatchCancleActPros"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"ItemIds": [itemid], "ActId": actid}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def cancel_all_act_pros(self, actid):
        """
        一键清空
        :return:
        """
        old_url = "mall/Pro/NewUserExclusive/CancleAllActPros"
        new_url = "omcr/mallactbasic/NewUserExclusive/CancleAllActPros"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"ActId": actid}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def get_act_pro_detail_by_id(self, actid, itemid):
        """
        编辑商品明细
        :return:
        """
        old_url = "mall/Pro/NewUserExclusive/GetActProDetailById"
        new_url = "omcr/mallactbasic/NewUserExclusive/GetActProDetailById"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"ActId": actid, "ItemId": itemid}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def copy_act_by_id(self, actid, cfgid):
        """
        复制活动
        :return:
        """
        old_url = "mall/Pro/NewUserExclusive/CopyActById"
        new_url = "omcr/mallactbasic/NewUserExclusive/CopyActById"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"Id": "0", "IsDisabled": "true", "ActName": "【复制】wdytest", "ActTag": "新人专享",
                   "ActBeginDate": "2024/05/21 14:59:30", "ActEndDate": "2024/05/23 14:59:30", "ShopType": "SH",
                   "ApplyShop": "", "IsShowProIngActView": "true", "IsShowProPreView": "false", "IsLimitSale": "false",
                   "CanUseCoupon": "false", "CouponIds": "", "CouponList": [], "NotUsePetCard": "true",
                   "ProJoinType": "OF",
                   "DiscountActOthercfg": {"SubjectHeadModel": 2, "SubjectHeadBgImage": "",
                                           "SubjectHeadBgColor": "#FFFFFF", "SubjectAdImage": "",
                                           "BackGroundColor": "#F5F5F5", "ShowCountDownType": 1, "ListShowStyle": 0,
                                           "IsShowActInst": "true", "ActInstructions": "", "ShareGuideText": "",
                                           "ShareGuideImage": "https://assets-img.ezrpro.com/mobile/img/goods/newcomersActivities-share-default.png",
                                           "BtnRemindBgColor": "#FFBE00", "BtnRemindTextColor": "#FFFFFF", "Id": cfgid},
                   "OldActId": actid, "ActType": "NUEL"}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)
        # print(r_old.json())

        return r_old.json(), r_new.json()

    def get_act_shop_infos(self, id):
        """
        获取活动门店信息
        :return:
        """
        old_url = "mall/Pro/NewUserExclusive/GetActShopInfos"
        new_url = "omcr/mallactbasic/NewUserExclusive/GetActShopInfos"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"ShopCode": "", "ActId": id, "PageIndex": 1, "PageSize": 5}

        r_old = self.send("GET", old_url, params=payload, headers=header)
        r_new = self.send("GET", new_url, params=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def delete_act_shops(self, actid, shopid):
        """
        获取活动门店信息
        :return:
        """
        old_url = "mall/Pro/NewUserExclusive/DeleteActShops"
        new_url = "omcr/mallactbasic/NewUserExclusive/DeleteActShops"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"ActId": actid, "ShopId": shopid}

        r_old = self.send("GET", old_url, params=payload, headers=header)
        r_new = self.send("GET", new_url, params=payload, headers=header)
        print(r_new.json())

        return r_old.json(), r_new.json()


if __name__ == '__main__':
    base = NewUserExclusive("q1")
    base.delete_act_shops(64077, 22202839)
    # base.import_act_pros(64065, "新人专享商品导入模板")
