from apis.base_api import BaseApi
from utils.file_tools import FileTool


class ProductPresale(BaseApi):
    def get_act_cfg_operation_log(self, id):
        """
        查看日志
        :return:
        """
        old_url = "mall/Act/MallActCommon/GetActCfgOperationlog"
        new_url = "omcr/mallactbasic/MallActCommon/GetActCfgOperationlog"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"ActId": id, "ActTypeStr": "YS2", "PageIndex": 1, "PageSize": 10}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def get_prod_presale_list(self):
        """
        列表数据查询
        :return:
        """
        old_url = "mall/Pro/ProductPresale/GetProdPresaleList"
        new_url = "omcr/mallactbasic/ProductPresale/GetProdPresaleList"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"Type": 0, "ShopType": "", "ShopName": "", "ProName": "", "CreateUser": "",
                   "PresaleType": 2, "PageIndex": 1, "PageSize": 10, "Id": "", "Scene": 1}

        r_old = self.send("GET", old_url, params=payload, headers=header)
        r_new = self.send("GET", new_url, params=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def out_export_pro(self):
        """
        列表导出
        :return:
        """
        old_url = "mall/Pro/ProductPresale/OutExportPro"
        new_url = "omcr/mallactbasic/ProductPresale/OutExportPro"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"Type": 0, "ShopType": "", "ShopName": "", "ProName": "", "CreateUser": "",
                   "PresaleType": 2, "PageIndex": 1, "PageSize": 10, "Scene": 1}

        r_old = self.send("GET", old_url, params=payload, headers=header)
        r_new = self.send("GET", new_url, params=payload, headers=header)
        # print(r_new.json())

        result = r_new.content
        print(result)
        with open('output.xlsx', 'wb') as file:
            file.write(result)

        return result

    def enable_prod_presale(self, actid):
        """
        活动启用
        :return:
        """
        old_url = "mall/Pro/ProductPresale/EnableProdPresale"
        new_url = "omcr/mallactbasic/ProductPresale/EnableProdPresale"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"ItemIds": [2830916], "Ids": [actid]}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def disabled_prod_presale(self, actid):
        """
        活动禁用
        :return:
        """
        old_url = "mall/Pro/ProductPresale/DisabledProdPresale"
        new_url = "omcr/mallactbasic/ProductPresale/DisabledProdPresale"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"Ids": [actid]}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def get_by_id(self, id):
        """
        获取活动详情
        :return:
        """
        old_url = "mall/Pro/ProductPresale/GetById"
        new_url = "omcr/mallactbasic/ProductPresale/GetById"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"id": id, "name": ""}

        r_old = self.send("GET", old_url, params=payload, headers=header)
        r_new = self.send("GET", new_url, params=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def save_data(self, payload):
        """
        活动保存
        :return:
        """
        old_url = "mall/Pro/ProductPresale/SaveData"
        new_url = "omcr/mallactbasic/ProductPresale/SaveData"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def import_datas(self, file):
        """
        活动导入
        :return:
        """
        old_url = "mall/Pro/ProductPresale/ImportDatas"
        new_url = "omcr/mallactbasic/ProductPresale/ImportDatas"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        data = {"preSaleType": 1, "ShopType": "SH", "ApplyShop": "", "Scene": 1}

        result = []
        urls = [old_url, new_url]

        for url in urls:
            file_path = FileTool.get_file(f"{file}.xlsx")
            with open(file_path, 'rb') as f:
                files = {'file': f}
                response = self.send("POST", url, files=files, data=data, headers=header)
                result.append(response.json())

        return result

    def get_act_shop_infos(self, id):
        """
        获取活动门店
        :return:
        """
        old_url = "mall/Pro/ProductPresale/GetActShopInfos"
        new_url = "omcr/mallactbasic/ProductPresale/GetActShopInfos"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"ShopCode": "", "ActId": id, "PageIndex": 1, "PageSize": 5}

        r_old = self.send("GET", old_url, params=payload, headers=header)
        r_new = self.send("GET", new_url, params=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def release_product(self, id):
        """
        释放专用商品
        :return:
        """
        old_url = "mall/Pro/ProductPresale/ReleaseProduct"
        new_url = "omcr/mallactbasic/ProductPresale/ReleaseProduct"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"ActId": id}

        r_old = self.send("GET", old_url, params=payload, headers=header)
        r_new = self.send("GET", new_url, params=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def save_config_presale_agreement(self, id):
        """
        添加活动配置
        :return:
        """
        old_url = "mall/Pro/ProductPresale/SaveConfigPreSaleAgreement"
        new_url = "omcr/mallactbasic/ProductPresale/SaveConfigPreSaleAgreement"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {"Id": id, "ActValue": "不可退啦啦啦啦啦啦啦啦"}

        r_old = self.send("POST", old_url, json=payload, headers=header)
        r_new = self.send("POST", new_url, json=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()

    def get_presale_config_by_key(self):
        """
        获取活动配置
        :return:
        """
        old_url = "mall/Pro/ProductPresale/GetPreSaleConfigByKey"
        new_url = "omcr/mallactbasic/ProductPresale/GetPreSaleConfigByKey"
        header = {"v": self.getVerify(old_url, self.userId), "cookie": self.cookies["cookie"]}

        payload = {}

        r_old = self.send("GET", old_url, params=payload, headers=header)
        r_new = self.send("GET", new_url, params=payload, headers=header)
        # print(r_new.json())

        return r_old.json(), r_new.json()


if __name__ == '__main__':
    base = ProductPresale("q1")
    print(base.out_export_pro())
