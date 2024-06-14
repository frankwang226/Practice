import time
import random

from apis.base_api import BaseApi
from utils.file_tools import FileTool


# from Interface_test.apis.base_api import BaseApi
# from Interface_test.utils.file_tools import FileTool


class ProductBonusAct(BaseApi):
    def get_list(self, name, state):
        """
        列表查询
        :return:
        """
        # cookies = self.getcookie(brandId=739, userMobile="13524204498", password="qwer1234", userId=21000098,
        #                          ssoId=220467,
        #                          accountUrl="https://account-demo.ezrpro.com", crmHost="https://crm-q1.ezrpro.com")
        # cookies["cookie"] += "ezr-env-tag=d4992"
        # self.getcookie(brandId=186, userMobile="13524204498", password="qwer1234", userId=12175923, ssoId=220467,
        #                accountUrl="https://account.ezrpro.com", crmHost="https://crm-tp.ezrpro.com")

        old_url = "mall/Pro/ProductBonusAct/GetList"
        new_url = "omcr/mallactbasic/ProductBonusAct/GetList"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"actBegTime": "", "actEndTime": "", "ActItemType": 0, "begTime": "", "codeName": "",
                   "CreateUser": "", "endTime": "", "Id": "", "Name": name, "pageIndex": 1, "pageSize": 10,
                   "shopType": "", "State": state}

        # r_old = self.send("POST", old_url, payload, header)
        # r_new = self.send("POST", new_url, payload, header)
        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)

        # print("--------")
        # print(r_old.json())
        # print("请求头:", r_old.request.headers)
        # print("请求体:", r_old.request.body)
        # print("---------------------------old.py---------------------------")
        # print(r_new.json())
        # print("请求头:", r_new.request.headers)
        # print("请求体:", r_new.request.body)

        return r_old.json(), r_new.json()

    def out_excel(self):
        """
        列表导出
        :return:
        """
        old_url = "mall/Pro/ProductBonusAct/OutExcel"
        new_url = "omcr/mallactbasic/ProductBonusAct/OutExcel"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"actBegTime": "", "actEndTime": "", "ActItemType": 0, "begTime": "", "codeName": "",
                   "CreateUser": "", "endTime": "", "Id": "", "Name": "", "shopType": "", "State": ""}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)

        return r_old.json(), r_new.json()

    def import_datas(self, file):
        """
        导入模版
        :return:
        """
        old_url = "mall/Pro/ProductBonusAct/ImportDatas"
        new_url = "omcr/mallactbasic/ProductBonusAct/ImportDatas"
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

        # r_old = self.send("POST", old_url, files=files, data=data, headers=header)
        # r_new = self.send("POST", new_url, files=files, data=data, headers=header)
        # print(r_old.json())
        # print(r_new.json())

        # return r_old.json(), r_new.json()

    def enable_bonus_act(self, ids):
        """
        批量启用
        :return:
        """
        old_url = "mall/Pro/ProductBonusAct/EnableBonusAct"
        new_url = "omcr/mallactbasic/ProductBonusAct/EnableBonusAct"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"ids": ids}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)

        return r_old.json(), r_new.json()

    def disabled_bonus_act(self, ids):
        """
        批量禁用
        :return:
        """
        old_url = "mall/Pro/ProductBonusAct/DisabledBonusAct"
        new_url = "omcr/mallactbasic/ProductBonusAct/DisabledBonusAct"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"ids": ids}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)

        return r_old.json(), r_new.json()

    def batch_release_act_pro(self, ids):
        """
        批量释放
        :param ids:
        :return:
        """
        old_url = "mall/Pro/ProductBonusAct/BatchReleaseActPro"
        new_url = "omcr/mallactbasic/ProductBonusAct/BatchReleaseActPro"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"Ids": ids}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)

        return r_old.json(), r_new.json()

    def get_by_id(self, id):
        """
        获取详情
        :return:
        """
        old_url = "mall/Pro/ProductBonusAct/GetById"
        new_url = "omcr/mallactbasic/ProductBonusAct/GetById"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"id": id}

        r_old = self.send("GET", old_url, params=payload, headers=header)
        r_new = self.send("GET", new_url, params=payload, headers=header)

        # print(r_old.json())

        return r_old.json(), r_new.json()

    def get_act_cfg_operation_log(self, id):
        """
        操作日志
        :return:
        """
        old_url = "mall/Act/MallActCommon/GetActCfgOperationlog"
        new_url = "omcr/mallactbasic/MallActCommon/GetActCfgOperationlog"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"ActId": id, "ActTypeStr": "JFDH", "PageIndex": 1, "PageSize": 10}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)

        return r_old.json(), r_new.json()

    def save_data(self, payload):
        """
        保存活动
        :return:
        """
        old_url = "mall/Pro/ProductBonusAct/SaveData"
        new_url = "omcr/mallactbasic/ProductBonusAct/SaveData"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)

        return r_old.json(), r_new.json()

    def get_bonus_group_list(self):
        """
        积分兑换商品分组
        :return:
        """
        old_url = "mall/Pro/ProductBonusAct/GetBonusGroupList"
        new_url = "omcr/mallactbasic/ProductBonusAct/GetBonusGroupList"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"PageIndex": 1, "PageSize": 1000, "Status": 1}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def update_bonus_act_cfg_status(self):
        """
        积分兑换商品分组-开关
        :return:
        """
        old_url = "mall/Pro/ProductBonusAct/UpdateBonusActCfgStatus"
        new_url = "omcr/mallactbasic/ProductBonusAct/UpdateBonusActCfgStatus"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"GroupStatus": 0}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)

        return r_old.json(), r_new.json()

    def update_bonus_group_status(self, groupid):
        """
        积分兑换商品分组-启用禁用
        :param groupid:
        :return:
        """
        old_url = "mall/Pro/ProductBonusAct/UpdateBonusGroupStatus"
        new_url = "omcr/mallactbasic/ProductBonusAct/UpdateBonusGroupStatus"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"GroupId": groupid, "Status": 1}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)

        return r_old.json(), r_new.json()

    def save_bonus_group_info(self, id):
        """
        新建积分兑换商品分组
        :return:
        """
        old_url = "mall/Pro/ProductBonusAct/SaveBonusGroupInfo"
        new_url = "omcr/mallactbasic/ProductBonusAct/SaveBonusGroupInfo"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"GroupName": "wdytest", "Id": id}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)

        return r_old.json(), r_new.json()

    def add_bonus_pool(self, actids):
        """
        总规则-保存
        :param actids:
        :return:
        """
        old_url = "mall/Pro/ProductBonusPool/AddBonusPool"
        new_url = "omcr/mallactbasic/ProductBonusPool/AddBonusPool"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"ActIds": [actids], "PoolName": "wdytest", "PoolTotalNum": 0, "PoolLimitNum": 0, "LimitType": 0,
                   "ForMonth": "", "Id": 0}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)
        print(r_new.json())

        return r_old.json(), r_new.json()

    def get_bonus_pool(self):
        """
        总规则-查询
        :return:
        """
        old_url = "mall/Pro/ProductBonusPool/GetBonusPool"
        new_url = "omcr/mallactbasic/ProductBonusPool/GetBonusPool"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"pageIndex": 1, "pageSize": 10}

        r_old = self.send("GET", old_url, params=payload, headers=header)
        r_new = self.send("GET", new_url, params=payload, headers=header)

        return r_old.json(), r_new.json()

    def get_act_list(self):
        """
        获取积分活动列表
        :return:
        """
        old_url = "mall/Pro/ProductBonusPool/GetActList"
        new_url = "omcr/mallactbasic/ProductBonusPool/GetActList"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"IsSelected": "false", "Name": "", "ActIds": [], "PageIndex": 1, "PageSize": 10}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)
        print(r_new.json())

        return r_old.json(), r_new.json()

    def get_pool_info_by_id(self, poolid):
        """
        根据Id获取总规则信息
        :param poolid:
        :return:
        """
        old_url = "mall/Pro/ProductBonusPool/GetPoolInfoById"
        new_url = "omcr/mallactbasic/ProductBonusPool/GetPoolInfoById"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"poolId": poolid}

        r_old = self.send("GET", old_url, params=payload, headers=header)
        r_new = self.send("GET", new_url, params=payload, headers=header)

        return r_old.json(), r_new.json()

    def del_bonus_pool(self, poolid):
        """
        删除限兑配置
        :param poolid:
        :return:
        """
        old_url = "mall/Pro/ProductBonusPool/DelBonusPool"
        new_url = "omcr/mallactbasic/ProductBonusPool/DelBonusPool"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"poolId": poolid}

        r_old = self.send("GET", old_url, params=payload, headers=header)
        r_new = self.send("GET", new_url, params=payload, headers=header)

        return r_old.json(), r_new.json()

    def get_pool_dtl(self, poolid):
        """
        获取限兑的明细
        :param poolid:
        :return:
        """
        old_url = "mall/Pro/ProductBonusPool/GetPoolDtl"
        new_url = "omcr/mallactbasic/ProductBonusPool/GetPoolDtl"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"poolId": poolid, "pageIndex": 1, "pageSize": 5}

        r_old = self.send("GET", old_url, params=payload, headers=header)
        r_new = self.send("GET", new_url, params=payload, headers=header)

        return r_old.json(), r_new.json()

    def release_product(self, id):
        """
        释放专用商品
        :param id:
        :return:
        """
        old_url = "mall/Pro/ProductBonusAct/ReleaseProduct"
        new_url = "omcr/mallactbasic/ProductBonusAct/ReleaseProduct"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"Id": id}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)

        return r_old.json(), r_new.json()

    def get_bonus_act_cfg(self):
        """
        活动积分兑换基础配置
        :return:
        """
        old_url = "mall/Pro/ProductBonusAct/GetBonusActCfg"
        new_url = "omcr/mallactbasic/ProductBonusAct/GetBonusActCfg"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {}

        r_old = self.send("GET", old_url, params=payload, headers=header)
        r_new = self.send("GET", new_url, params=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def get_bonus_act_by_group_id(self, groupid):
        """
        分页查询积分兑换分组列表
        :param groupid:
        :return:
        """
        old_url = "mall/Pro/ProductBonusAct/GetBonusActByGroupId"
        new_url = "omcr/mallactbasic/ProductBonusAct/GetBonusActByGroupId"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"groupId": groupid, "PageIndex": 1, "PageSize": 10}

        r_old = self.send("GET", old_url, params=payload, headers=header)
        r_new = self.send("GET", new_url, params=payload, headers=header)

        return r_old.json(), r_new.json()

    def save_group_bonus_sort(self, Id):
        """
        保存分组活动排序
        :param Id:
        :return:
        """
        old_url = "mall/Pro/ProductBonusAct/SaveGroupBonusSort"
        new_url = "omcr/mallactbasic/ProductBonusAct/SaveGroupBonusSort"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        displayindex = random.randint(1, 10)
        payload = {"BonusActGroups": [{"Id": Id, "DisplayIndex": displayindex}]}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)

        return r_old.json(), r_new.json()

    def update_bonus_group(self, actid, groupid):
        """
        绑定分组
        :param actid:
        :param groupid:
        :return:
        """
        old_url = "mall/Pro/ProductBonusAct/UpdateBonusGroup"
        new_url = "omcr/mallactbasic/ProductBonusAct/UpdateBonusGroup"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"ActId": actid, "GroupId": groupid, "UpdateType": 0}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)

        return r_old.json(), r_new.json()

    def get_page_link(self):
        """
        分页获取活动列表链接
        :return:
        """
        old_url = "mall/Pro/ProductBonusAct/GetPageLink"
        new_url = "omcr/mallactbasic/ProductBonusAct/GetPageLink"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {}

        r_old = self.send("GET", old_url, params=payload, headers=header)
        r_new = self.send("GET", new_url, params=payload, headers=header)

        return r_old.json(), r_new.json()

    def update_bonus_act_cfg(self):
        """
        修改动态积分兑换价显示规则
        :return:
        """
        old_url = "mall/Pro/ProductBonusAct/UpdateBonusActCfg"
        new_url = "omcr/mallactbasic/ProductBonusAct/UpdateBonusActCfg"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"BonusExDisplayRule": "MIN"}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)

        return r_old.json(), r_new.json()


if __name__ == '__main__':
    base = ProductBonusAct("q1")
    # base.save_group_bonus_sort(50159)
    # base.get_bonus_group_list()
    # base.save_data()
    base.import_datas("积分兑换导入表")
