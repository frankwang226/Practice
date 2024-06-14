import logging

import allure
import pytest

from apis.ecommerce.product_presale.product_presale import ProductPresale
from utils.compare_json import compare_json_data
from utils.file_tools import FileTool


# 实例化夹子函数
@pytest.fixture(scope="class")
def productpresale(env_config):
    yield ProductPresale(env_config)


@allure.suite("预售")
@allure.feature("预售")
class TestProductPresale:
    @pytest.fixture()
    def env(self, env_config):
        yield env_config

    def test_getactcfgoperationlog(self, productpresale):
        res = productpresale.get_prod_presale_list()
        id = res[1].get("Data").get("PagedList")[0].get("Id")
        response = productpresale.get_act_cfg_operation_log(id)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_getprodpresalelist(self, productpresale):
        response = productpresale.get_prod_presale_list()
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_enableprodpresale(self, productpresale, env):
        global payload
        data = FileTool.read_yaml("ProductPresale_save")
        if env == "q1":
            payload = data.get("q1").get("payload")
        elif env == "tp":
            payload = data.get("tp").get("payload")
        productpresale.save_data(payload)
        res = productpresale.get_prod_presale_list()
        actid = res[1].get("Data").get("PagedList")[0].get("Id")
        response = productpresale.enable_prod_presale(actid)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_disabledprodpresale(self, productpresale, env):
        global payload
        data = FileTool.read_yaml("ProductPresale_save")
        if env == "q1":
            payload = data.get("q1").get("payload")
        elif env == "tp":
            payload = data.get("tp").get("payload")
        productpresale.save_data(payload)
        res = productpresale.get_prod_presale_list()
        actid = res[1].get("Data").get("PagedList")[0].get("Id")
        productpresale.enable_prod_presale(actid)
        response = productpresale.disabled_prod_presale(actid)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_getbyid(self, productpresale):
        res = productpresale.get_prod_presale_list()
        id = res[1].get("Data").get("PagedList")[0].get("Id")
        response = productpresale.get_by_id(id)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_savedata(self, productpresale, env):
        global payload
        data = FileTool.read_yaml("ProductPresale_save")
        if env == "q1":
            payload = data.get("q1").get("payload")
        elif env == "tp":
            payload = data.get("tp").get("payload")
        response = productpresale.save_data(payload)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_importdatas(self, productpresale):
        response = productpresale.import_datas("限券定金预售导入表")
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_getactshopinfos(self, productpresale, env):
        global payload
        data = FileTool.read_yaml("ProductPresale_save")
        if env == "q1":
            payload = data.get("q1").get("payload")
        elif env == "tp":
            payload = data.get("tp").get("payload")
        productpresale.save_data(payload)
        res = productpresale.get_prod_presale_list()
        id = res[1].get("Data").get("PagedList")[0].get("Id")
        response = productpresale.get_act_shop_infos(id)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_releaseproduct(self, productpresale, env):
        global payload
        data = FileTool.read_yaml("ProductPresale_save")
        if env == "q1":
            payload = data.get("q1").get("payload")
        elif env == "tp":
            payload = data.get("tp").get("payload")
        productpresale.save_data(payload)
        res = productpresale.get_prod_presale_list()
        id = res[1].get("Data").get("PagedList")[0].get("Id")
        response = productpresale.release_product(id)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_saveconfigpresaleagreement(self, productpresale, env):
        global id
        if env == "q1":
            id = 60021
        elif env == "tp":
            id = 60018
        response = productpresale.save_config_presale_agreement(id)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_getpresaleconfigbykey(self, productpresale):
        response = productpresale.get_presale_config_by_key()
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True
