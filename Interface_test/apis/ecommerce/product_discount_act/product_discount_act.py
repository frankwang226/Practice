from apis.base_api import BaseApi
from utils.file_tools import FileTool


class ProductDiscountAct(BaseApi):
    def get_set_disabled_record_list(self):
        """
        启用记录
        :return:
        """
        old_url = "mall/pro/ProductDiscountAct/GetSetDisabledRecordList"
        new_url = "omcr/mallactbasic/ProductDiscountAct/GetSetDisabledRecordList"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"ActId": 52508, "ActTypeStr": "YS2", "PageIndex": 1, "PageSize": 10}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def get_act_pro_detail_by_id(self):
        """
        限时优惠获取条码
        :return:
        """
        old_url = "mall/Pro/ProductDiscountAct/GetActProDetailById"
        new_url = "omcr/mallactbasic/ProductDiscountAct/GetActProDetailById"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"ActId": 52508, "ActTypeStr": "YS2", "PageIndex": 1, "PageSize": 10}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def batch_cancel_act_pros(self):
        """
        批量取消活动商品
        :return:
        """
        old_url = "Pro/ProductDiscountAct/BatchCancleActPros"
        new_url = "omcr/mallactbasic/ProductDiscountAct/BatchCancleActPros"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"ActId": 52508, "ActTypeStr": "YS2", "PageIndex": 1, "PageSize": 10}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def update_act_pros_close_discount(self):
        """
        查看日志
        :return:
        """
        old_url = "Pro/ProductDiscountAct/UpdateActProIsCloseDiscount"
        new_url = "omcr/mallactbasic/ProductDiscountAct/UpdateActProIsCloseDiscount"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"ActId": 52508, "ActTypeStr": "YS2", "PageIndex": 1, "PageSize": 10}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def export_act_pros(self):
        """
        导出活动商品列表
        :return:
        """
        old_url = "Pro/ProductDiscountAct/ExportActPros"
        new_url = "omcr/mallactbasic/ProductDiscountAct/ExportActPros"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"ActId": 52508, "ActTypeStr": "YS2", "PageIndex": 1, "PageSize": 10}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()