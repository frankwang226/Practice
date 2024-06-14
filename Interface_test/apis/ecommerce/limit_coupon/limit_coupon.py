import time

from apis.base_api import BaseApi
from utils.file_tools import FileTool


class LimitCoupon(BaseApi):

    startdate = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    enddate = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + 86400 * 2))

    def get_act_cfg_operation_log(self, id):
        """
        查看日志
        :return:
        """
        old_url = "mall/Act/MallActCommon/GetActCfgOperationlog"
        new_url = "omcr/mallactbasic/MallActCommon/GetActCfgOperationlog"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"ActId": id, "ActTypeStr": "XQG", "PageIndex": 1, "PageSize": 10}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def get_list(self):
        """
        列表数据查询
        :return:
        """
        old_url = "mall/Pro/LimitCoupon/GetList"
        new_url = "omcr/mallactbasic/LimitCoupon/GetList"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"ActivityName": "", "CreateUser": "", "State": 0, "shopType": "all", "Name": "", "PageIndex": 1,
                   "PageSize": 10, "Id": ""}

        r_old = self.send("GET", old_url, params=payload, headers=header)
        r_new = self.send("GET", new_url, params=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def set_is_enable(self, id, isenable):
        """
        启用/禁用
        :return:
        """
        old_url = "mall/Pro/LimitCoupon/SetIsEnable"
        new_url = "omcr/mallactbasic/LimitCoupon/SetIsEnable"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"Id": id, "IsEnable": isenable}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def set_is_release(self, id):
        """
        释放商品
        :return:
        """
        old_url = "mall/Pro/LimitCoupon/SetIsRelease"
        new_url = "omcr/mallactbasic/LimitCoupon/SetIsRelease"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"id": id}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def get_limit_coupon_info(self, id):
        """
        获取详情
        :return:
        """
        old_url = "mall/Pro/LimitCoupon/GetLimitCouponInfo"
        new_url = "omcr/mallactbasic/LimitCoupon/GetLimitCouponInfo"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"Id": id}

        r_old = self.send("GET", old_url, params=payload, headers=header)
        r_new = self.send("GET", new_url, params=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def limit_coupon_check(self, productid, shopid):
        """
        验证
        :return:
        """
        old_url = "mall/Pro/LimitCoupon/LimitCouponCheck"
        new_url = "omcr/mallactbasic/LimitCoupon/LimitCouponCheck"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"StartTime": self.startdate, "EndTime": self.enddate, "ProIds": productid,
                   "ApplyShop": shopid, "ShopType": "SH"}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def save(self, productid, couponid, couponname, shopid):
        """
        保存
        :return:
        """
        old_url = "mall/Pro/LimitCoupon/Save"
        new_url = "omcr/mallactbasic/LimitCoupon/Save"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"Id": 0, "ProIds": productid, "ActivityLabel": "限券抢购", "CouponId": couponid, "ShopType": "SH",
                   "ApplyShop": shopid, "ShopList": [shopid], "CouponName": couponname,
                   "EndTime": self.enddate, "StartTime": self.startdate, "Url": "",
                   "IsNoExpressFee": "false", "IsUseCoupon": "false", "LimitNum": 0, "WxAppId": "", "Name": "wdytest",
                   "Remark": "", "ScenarioType": "0", "ScenarioUrl": ""}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()


if __name__ == '__main__':
    base = LimitCoupon("q1")
    print(base.set_is_enable(50412, "true"))
