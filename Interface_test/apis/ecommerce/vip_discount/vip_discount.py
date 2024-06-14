# from Interface_test.apis.base_api import BaseApi
# from Interface_test.utils.file_tools import FileTool
from apis.base_api import BaseApi
from utils.file_tools import FileTool


class VipDiscount(BaseApi):
    def get_list(self):
        """
        获取商品
        :return:
        """

        old_url = "mall/Act/VipDiscount/GetList"
        new_url = "omcr/mallactbasic/VipDiscount/GetList"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"PageIndex": 1, "PageSize": 10, "ItemName": "", "BeginAddTime": "", "EndAddTime": ""}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)
        print(r_new.json())

        return r_old.json(), r_new.json()

    def get_act_cfg_operation_log(self):
        """
        查看日志
        :return:
        """
        old_url = "mall/Act/MallActCommon/GetActCfgOperationlog"
        new_url = "omcr/mallactbasic/MallActCommon/GetActCfgOperationlog"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"ActId": 0, "ActTypeStr": "HYQYZK", "PageIndex": 1, "PageSize": 10}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)
        print(r_new.json())

        return r_old.json(), r_new.json()

    def save_data(self, id):
        """
        保存商品
        :return:
        """
        old_url = "mall/Act/VipDiscount/SaveData"
        new_url = "omcr/mallactbasic/VipDiscount/SaveData"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"ItemIdList": [id]}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)

        return r_old.json(), r_new.json()

    def import_datas(self, file):
        """
        导表添加商品/删除商品
        :return:
        """
        data_dic = {"url": ["mall/Act/VipDiscount/ImportDatas", "omcr/mallactbasic/VipDiscount/ImportDatas"],
                    "data": [{"ImportType": 1}, {"ImportType": 2}]}
        print(data_dic["url"][1])
        # old_url = "mall/Act/VipDiscount/ImportDatas"
        # new_url = "omcr/mallactbasic/VipDiscount/ImportDatas"
        header = {"v": self.getVerify(data_dic["url"][1], self.userId), "cookie": self.cookies["cookie"]}
        # data_insert = {"ImportType": 1}
        # data_delete = {"ImportType": 2}

        result = []
        # urls = [old_url, new_url]

        for i in range(2):
            file_path = FileTool.get_file(f"{file}.xlsx")
            with open(file_path, 'rb') as f:
                files = {'file': f}
                response = self.send("POST", data_dic["url"][i], files=files, data=data_dic["data"][i], headers=header)
                print(response.json())
                result.append(response.json())

        return result

    def get_act_config_list(self):
        """
        获取配置
        :return:
        """
        old_url = "mall/Act/ActiveConfig/GetActConfigList"
        new_url = "omcr/mallactbasic/ActiveConfig/GetActConfigList"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"MallActType":1}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)

        return r_old.json(), r_new.json()

    def remove_all(self, ids):
        """
        批量删除商品
        :return:
        """
        old_url = "mall/Act/VipDiscount/RemoveAll"
        new_url = "omcr/mallactbasic/ActiveConfig/RemoveAll"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"DelType": 1, "Ids": [ids],
                   "RequestPara": {"PageIndex": 1, "PageSize": 10, "ItemName": "", "BeginAddTime": "",
                                   "EndAddTime": ""}}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)

        return r_old.json(), r_new.json()

    def update_is_enable(self, id):
        """
        删除商品
        :return:
        """
        old_url = "mall/Act/VipDiscount/UpdateIsEnable"
        new_url = "omcr/mallactbasic/ActiveConfig/UpdateIsEnable"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"Id": id, "IsEnable": "false"}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)

        return r_old.json(), r_new.json()

    def export_act_data(self):
        """
        导出商品
        :return:
        """
        old_url = "mall/Act/VipDiscount/ExportActData"
        new_url = "omcr/mallactbasic/ActiveConfig/ExportActData"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"ItemName": "", "BeginAddTime": "", "EndAddTime": ""}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)

        return r_old.json(), r_new.json()

    def is_remove_data(self):
        """
        是否在清理数据
        :return:
        """
        old_url = "mall/Act/VipDiscount/IsRemoveData"
        new_url = "omcr/mallactbasic/VipDiscount/IsRemoveData"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {}

        r_old = self.send("GET", old_url, params=payload, headers=header)
        r_new = self.send("GET", new_url, params=payload, headers=header)

        return r_old.json(), r_new.json()

    def update_min_discount_by_id(self, itemid):
        """
        更新最低折扣
        :return:
        """
        old_url = "mall/Act/VipDiscount/UpdateMinDiscountById"
        new_url = "omcr/mallactbasic/VipDiscount/UpdateMinDiscountById"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"ItemIds": [itemid], "MinDiscount": 10}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)

        return r_old.json(), r_new.json()


if __name__ == '__main__':
    base = VipDiscount("q1")
    base.import_datas("积分兑换导入表")
