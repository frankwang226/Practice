import logging

import allure
import pytest

from apis.ecommerce.product_group_by.product_group_by import ProductGroupBy
from utils.compare_json import compare_json_data


# 实例化夹子函数
@pytest.fixture(scope="class")
def productgroupby(env_config):
    yield ProductGroupBy(env_config)


@allure.suite("秒杀")
@allure.feature("秒杀")
class TestProductGroupBy:
    @pytest.fixture()
    def env(self, env_config):
        yield env_config

    def test_getactcfgoperationlog(self, productgroupby):
        res = productgroupby.get_prd_group_buy_list()
        id = res[1].get("Data").get("PagedList")[0].get("Id")
        response = productgroupby.get_act_cfg_operation_log(id)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_getprdgroupbuylist(self, productgroupby):
        response = productgroupby.get_prd_group_buy_list()
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_exportactdata(self, productgroupby):
        response = productgroupby.export_act_data()
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_importdatas(self, productgroupby):
        response = productgroupby.import_datas("秒杀导入表V1")
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_batchenableordisabledgroupbuy(self, productgroupby, env):
        global shopid, itemid, itemname
        if env == "q1":
            shopid = "22202835,21172697"
            itemid = 2830894
            itemname = "Van Cleef & Arpels 四叶草手链"
        elif env == "tp":
            shopid = "25314264,10000048"
            itemid = 12976665
            itemname = "示例商品1"
        productgroupby.save_data(shopid, itemid, itemname)
        res = productgroupby.get_prd_group_buy_list()
        id = res[1].get("Data").get("PagedList")[0].get("Id")
        response = productgroupby.batch_enable_or_disabled_group_buy(id, 1)
        productgroupby.batch_enable_or_disabled_group_buy(id, 2)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_enableordisablegroupbuy(self, productgroupby, env):
        global shopid, itemid, itemname
        if env == "q1":
            shopid = "22202835,21172697"
            itemid = 2830894
            itemname = "Van Cleef & Arpels 四叶草手链"
        elif env == "tp":
            shopid = "25314264,10000048"
            itemid = 12976665
            itemname = "示例商品1"
        productgroupby.save_data(shopid, itemid, itemname)
        res = productgroupby.get_prd_group_buy_list()
        id = res[1].get("Data").get("PagedList")[0].get("Id")
        response = productgroupby.enable_or_disabled_group_buy(id, 1)
        productgroupby.enable_or_disabled_group_buy(id, 2)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_getbyid(self, productgroupby):
        res = productgroupby.get_prd_group_buy_list()
        id = res[1].get("Data").get("PagedList")[0].get("Id")
        response = productgroupby.get_by_id(id)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_savedata(self, productgroupby, env):
        global shopid, itemid, itemname
        if env == "q1":
            shopid = "22202835,21172697"
            itemid = 2830894
            itemname = "Van Cleef & Arpels 四叶草手链"
        elif env == "tp":
            shopid = "25314264,10000048"
            itemid = 12976665
            itemname = "示例商品1"
        response = productgroupby.save_data(shopid, itemid, itemname)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_get_act_shop_infos(self, productgroupby, env):
        global shopid, itemid, itemname
        if env == "q1":
            shopid = "22202835,21172697"
            itemid = 2830894
            itemname = "Van Cleef & Arpels 四叶草手链"
        elif env == "tp":
            shopid = "25314264,10000048"
            itemid = 12976665
            itemname = "示例商品1"
        productgroupby.save_data(shopid, itemid, itemname)
        res = productgroupby.get_prd_group_buy_list()
        actid = res[1].get("Data").get("PagedList")[0].get("Id")
        response = productgroupby.get_act_shop_infos(actid)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True
