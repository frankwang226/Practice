import logging
import time

import allure
import pytest

from apis.ecommerce.new_user_exclusive.new_user_exclusive import NewUserExclusive
from utils.compare_json import compare_json_data
from utils.file_tools import FileTool
from utils.get_product_id import GetProduct


# from Interface_test.apis.ecommerce.new_user_exclusive.new_user_exclusive import NewUserExclusive
# from Interface_test.utils.compare_json import compare_json_data
# from Interface_test.utils.file_tools import FileTool
# from Interface_test.utils.get_product_id import GetProduct

# 实例化夹子函数
@pytest.fixture(scope="class")
def newuserexlusive(env_config):
    yield NewUserExclusive(env_config)


@allure.suite("新人专享")
@allure.feature("新人专享")
class TestNewUserExclusive:
    @pytest.fixture()
    def env(self, env_config):
        yield env_config

    def test_get_act_cfg_operation_log(self, newuserexlusive):
        res = newuserexlusive.get_list("")
        actid = res[1].get("Data").get("PagedList")[0].get("Id")
        response = newuserexlusive.get_act_cfg_operation_log(actid)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_get_list(self, newuserexlusive):
        response = newuserexlusive.get_list("")
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_save_data_new(self, newuserexlusive, env):
        global shopid
        if env == "q1":
            shopid = "21172697,22202839"
        elif env == "tp":
            shopid = "10000048,21002691"
        response = newuserexlusive.save_data_new(shopid)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_get_by_id(self, newuserexlusive):
        res = newuserexlusive.get_list("")
        id = res[1].get("Data").get("PagedList")[0].get("Id")
        # print(type(id))
        response = newuserexlusive.get_by_id(id)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_set_disabled(self, newuserexlusive, env):
        global payload_enable, payload_disable
        data = FileTool.read_yaml("NewUserExclusive_disable")
        if env == "q1":
            payload_enable = data.get("q1").get("payload_enable")
            payload_disable = data.get("q1").get("payload_disable")
        elif env == "tp":
            payload_enable = data.get("tp").get("payload_enable")
            payload_disable = data.get("tp").get("payload_disable")
        response = newuserexlusive.set_disabled(payload_enable)
        time.sleep(5)
        newuserexlusive.set_disabled(payload_disable)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_save_act_pro_info(self, newuserexlusive, env):
        global shopid
        if env == "q1":
            shopid = "21172697,22202839"
        elif env == "tp":
            shopid = "10000048,21002691"
        res = newuserexlusive.save_data_new(shopid)
        actid = res[1].get("Data").get("Id")
        itemid = GetProduct(env).get_product_id()
        response = newuserexlusive.save_act_pro_info(actid, itemid)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_get_act_pro_list_page(self, newuserexlusive):
        res = newuserexlusive.get_list("")
        actid = res[1].get("Data").get("PagedList")[0].get("Id")
        response = newuserexlusive.get_act_pro_list_page(actid)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_import_act_pros(self, newuserexlusive):
        res = newuserexlusive.get_list(4)
        actid = res[1].get("Data").get("PagedList")[0].get("Id")
        response = newuserexlusive.import_act_pros(actid, "新人专享商品导入模板")
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_export_act_pros(self, newuserexlusive):
        res = newuserexlusive.get_list("")
        actid = res[1].get("Data").get("PagedList")[-1].get("Id")
        response = newuserexlusive.export_act_pros(actid)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_batch_cancel_act_pros(self, newuserexlusive, env):
        global shopid
        if env == "q1":
            shopid = "21172697,22202839"
        elif env == "tp":
            shopid = "10000048,21002691"
        res = newuserexlusive.save_data_new(shopid)
        actid = res[1].get("Data").get("Id")
        itemid = GetProduct(env).get_product_id()
        newuserexlusive.save_act_pro_info(actid, itemid)
        response = newuserexlusive.batch_cancel_act_pros(actid, itemid)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_cancel_all_act_pros(self, newuserexlusive, env):
        global shopid
        if env == "q1":
            shopid = "21172697,22202839"
        elif env == "tp":
            shopid = "10000048,21002691"
        res = newuserexlusive.save_data_new(shopid)
        actid = res[1].get("Data").get("Id")
        itemid = GetProduct(env).get_product_id()
        newuserexlusive.save_act_pro_info(actid, itemid)
        response = newuserexlusive.cancel_all_act_pros(actid)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_get_act_pro_detail_by_id(self, newuserexlusive, env):
        global shopid
        if env == "q1":
            shopid = "21172697,22202839"
        elif env == "tp":
            shopid = "10000048,21002691"
        res = newuserexlusive.save_data_new(shopid)
        actid = res[1].get("Data").get("Id")
        itemid = GetProduct(env).get_product_id()
        newuserexlusive.save_act_pro_info(actid, itemid)
        response = newuserexlusive.get_act_pro_detail_by_id(actid, itemid)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_copy_act_by_id(self, newuserexlusive, env):
        global shopid
        if env == "q1":
            shopid = "21172697,22202839"
        elif env == "tp":
            shopid = "10000048,21002691"
        res1 = newuserexlusive.save_data_new(shopid)
        actid = res1[1].get("Data").get("Id")
        res2 = newuserexlusive.get_by_id(actid)
        cfgid = res2[1].get("Data").get("DiscountActOthercfg").get("Id")
        response = newuserexlusive.copy_act_by_id(actid, cfgid)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_get_act_shop_infos(self, newuserexlusive, env):
        global shopid
        if env == "q1":
            shopid = "21172697,22202839"
        elif env == "tp":
            shopid = "10000048,21002691"
        newuserexlusive.save_data_new(shopid)
        res = newuserexlusive.get_list("")
        actid = res[1].get("Data").get("PagedList")[0].get("Id")
        response = newuserexlusive.get_act_shop_infos(actid)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_delete_act_shops(self, newuserexlusive, env):
        global shopid
        if env == "q1":
            shopid = "21172697,22202839"
        elif env == "tp":
            shopid = "10000048,21002691"
        newuserexlusive.save_data_new(shopid)
        res1 = newuserexlusive.get_list("")
        actid = res1[1].get("Data").get("PagedList")[0].get("Id")
        res2 = newuserexlusive.get_act_shop_infos(actid)
        shopid = res2[1].get("Data").get("PagedList").get("ActShopDataItems")[0].get("Id")
        response = newuserexlusive.delete_act_shops(actid, shopid)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True
