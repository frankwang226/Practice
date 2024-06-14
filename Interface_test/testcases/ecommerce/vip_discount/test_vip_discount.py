import logging

import allure
import pytest

from apis.ecommerce.vip_discount.vip_discount import VipDiscount
from utils.compare_json import compare_json_data
from utils.get_product_id import GetProduct


# from Interface_test.apis.ecommerce.vip_discount.vip_discount import VipDiscount
# from Interface_test.utils.compare_json import compare_json_data
# from Interface_test.utils.get_product_id import GetProduct

# 实例化夹子函数
@pytest.fixture(scope="class")
def vipdiscount(env_config):
    yield VipDiscount(env_config)


@allure.suite("会员权益折扣")
@allure.feature("会员权益折扣")
class TestVipDiscount:
    @pytest.fixture()
    def env(self, env_config):
        yield env_config

    def test_getlist(self, vipdiscount):
        response = vipdiscount.get_list()
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_getactcfgoperationlog(self, vipdiscount):
        response = vipdiscount.get_act_cfg_operation_log()
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_savedata(self, vipdiscount, env):
        pro_id = GetProduct(env).get_product_id()
        response = vipdiscount.save_data(pro_id)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_importdatas(self, vipdiscount):
        response = vipdiscount.import_datas("会员权益商品导入表")
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_getactconfiglist(self, vipdiscount):
        response = vipdiscount.get_act_config_list()
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_removeall(self, vipdiscount, env):
        pro_id = GetProduct(env).get_product_id()
        vipdiscount.save_data(pro_id)
        res = vipdiscount.get_list()
        ids = res[1].get("Data").get("Result")[0].get("Id")
        response = vipdiscount.remove_all(ids)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_updateisenable(self, vipdiscount, env):
        pro_id = GetProduct(env).get_product_id()
        vipdiscount.save_data(pro_id)
        res = vipdiscount.get_list()
        id = res[1].get("Data").get("Result")[0].get("Id")
        response = vipdiscount.update_is_enable(id)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_exportactdata(self, vipdiscount):
        response = vipdiscount.export_act_data()
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_isremovedata(self, vipdiscount):
        response = vipdiscount.is_remove_data()
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_updatemindiscountbyid(self, vipdiscount, env):
        itemid = GetProduct(env).get_product_id()
        vipdiscount.save_data(itemid)
        response = vipdiscount.update_min_discount_by_id(itemid)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True
