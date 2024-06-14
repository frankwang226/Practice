# from Interface_test.apis.ecommerce.bargain_act.bargain_act import BargainAct
# from Interface_test.utils.compare_json import compare_json_data
# from Interface_test.utils.get_product_id import GetProduct
import logging
import time

import allure
import pytest

from apis.ecommerce.bargain_act.bargain_act import BargainAct
from utils.compare_json import compare_json_data


# 实例化夹子函数
@pytest.fixture(scope="class")
def bargain(env_config):
    yield BargainAct(env_config)


@allure.suite("砍价")
@allure.feature("砍价活动")
class TestBargainAct:
    @pytest.fixture()
    def env(self, env_config):
        yield env_config

    def test_getactcfgoperationlog(self, bargain):
        # 这里的bargain是调用的实例化夹子函数，拿到返回的实例化对象BargainAct(env_config)
        res = bargain.get_bargain_act_list()
        id = res[1].get("Data").get("PagedList")[0].get("Id")
        response = bargain.get_act_cfg_operation_log(id)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_createorupdatebargainactcfg(self, bargain, env):
        global id
        if env == "q1":
            id = 50010
        elif env == "tp":
            id = 1
        response = bargain.create_or_update_bargain_act_cfg(id)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_getbargainactlist(self, bargain):
        response = bargain.get_bargain_act_list()
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_importdatas(self, bargain, env):
        global shopid
        if env == "q1":
            shopid = 21172697
        elif env == "tp":
            shopid = 10000048
        response = bargain.import_datas("砍价导入表", shopid)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_setactenable(self, bargain, env):
        global productid, productname, productitemNo, shopname, shopid
        if env == "q1":
            productid = 2830924
            productname = "鞋套"
            productitemNo = "tttop0527super030"
            shopname = "wdy%测试门店"
            shopid = 21172697
        elif env == "tp":
            productid = 12976808
            productname = "牛仔裤 随心搭配"
            productitemNo = "GZYtestitem0529"
            shopname = "WDY测试门店"
            shopid = 10000048
        bargain.create_bargain_act(productid, productname, productitemNo, shopname, shopid)
        res = bargain.get_bargain_act_list()
        id = res[1].get("Data").get("PagedList")[0].get("Id")
        response = bargain.set_act_enable(id)
        # 禁用活动 teardown
        time.sleep(3)
        bargain.set_act_disable(id)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_setactdisable(self, bargain, env):
        global productid, productname, productitemNo, shopname, shopid
        if env == "q1":
            productid = 2830924
            productname = "鞋套"
            productitemNo = "tttop0527super030"
            shopname = "wdy%测试门店"
            shopid = 21172697
        elif env == "tp":
            productid = 12976808
            productname = "牛仔裤 随心搭配"
            productitemNo = "GZYtestitem0529"
            shopname = "WDY测试门店"
            shopid = 10000048
        bargain.create_bargain_act(productid, productname, productitemNo, shopname, shopid)
        res = bargain.get_bargain_act_list()
        id = res[1].get("Data").get("PagedList")[0].get("Id")
        bargain.set_act_enable(id)
        response = bargain.set_act_disable(id)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_getbargainactdetail(self, bargain, env):
        global productid, productname, productitemNo, shopname, shopid
        if env == "q1":
            productid = 2830924
            productname = "鞋套"
            productitemNo = "tttop0527super030"
            shopname = "wdy%测试门店"
            shopid = 21172697
        elif env == "tp":
            productid = 12976808
            productname = "牛仔裤 随心搭配"
            productitemNo = "GZYtestitem0529"
            shopname = "WDY测试门店"
            shopid = 10000048
        bargain.create_bargain_act(productid, productname, productitemNo, shopname, shopid)
        res = bargain.get_bargain_act_list()
        id = res[1].get("Data").get("PagedList")[0].get("Id")
        response = bargain.get_bargain_act_detail(id)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_createbargainact(self, bargain, env):
        global productid, productname, productitemNo, shopname, shopid
        if env == "q1":
            productid = 2830924
            productname = "鞋套"
            productitemNo = "tttop0527super030"
            shopname = "wdy%测试门店"
            shopid = 21172697
        elif env == "tp":
            productid = 12976808
            productname = "牛仔裤 随心搭配"
            productitemNo = "GZYtestitem0529"
            shopname = "WDY测试门店"
            shopid = 10000048
        response = bargain.create_bargain_act(productid, productname, productitemNo, shopname, shopid)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_editbargainact(self, bargain, env):
        global productid, productname, productitemNo, shopname, shopid, actid, actdtlid
        if env == "q1":
            productid = 2830924
            productname = "鞋套"
            productitemNo = "tttop0527super030"
            shopname = "wdy%测试门店"
            shopid = 21172697
            actid = 52614
            actdtlid = 53258
        elif env == "tp":
            productid = 12976808
            productname = "牛仔裤 随心搭配"
            productitemNo = "GZYtestitem0529"
            shopname = "WDY测试门店"
            shopid = 10000048
            actid = 280938
            actdtlid = 51286
        response = bargain.edit_bargain_act(productid, productname, productitemNo, shopname, shopid, actid, actdtlid)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_getactstatisticdatabyactid(self, bargain, env):
        global id
        if env == "q1":
            id = 52545
        elif env == "tp":
            id = 37
        response = bargain.get_act_statistic_data_by_act_id(id)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_getbargainrecordlist(self, bargain, env):
        global id
        if env == "q1":
            id = 52545
        elif env == "tp":
            id = 37
        response = bargain.get_bargain_record_list(id)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_exportbargainrecord(self, bargain, env):
        global id
        if env == "q1":
            id = 52545
        elif env == "tp":
            id = 37
        response = bargain.export_bargain_record(id)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_getbargainactdtl(self, bargain, env):
        global productid, productname, productitemNo, shopname, shopid
        if env == "q1":
            productid = 2830924
            productname = "鞋套"
            productitemNo = "tttop0527super030"
            shopname = "wdy%测试门店"
            shopid = 21172697
        elif env == "tp":
            productid = 12976808
            productname = "牛仔裤 随心搭配"
            productitemNo = "GZYtestitem0529"
            shopname = "WDY测试门店"
            shopid = 10000048
        with allure.step("创建砍价活动"):
            bargain.create_bargain_act(productid, productname, productitemNo, shopname, shopid)
        with allure.step("查询列表获取活动id"):
            res = bargain.get_bargain_act_list()
            id = res[1].get("Data").get("PagedList")[0].get("Id")
        with allure.step("启用活动"):
            bargain.set_act_enable(id)
        with allure.step("查询活动详情"):
            response = bargain.get_bargain_act_dtl(id)
            logging.info(response)
            allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_updatebargainactdtl(self, bargain, env):
        global productid, productname, productitemNo, shopname, shopid
        if env == "q1":
            productid = 2830924
            productname = "鞋套"
            productitemNo = "tttop0527super030"
            shopname = "wdy%测试门店"
            shopid = 21172697
        elif env == "tp":
            productid = 12976808
            productname = "牛仔裤 随心搭配"
            productitemNo = "GZYtestitem0529"
            shopname = "WDY测试门店"
            shopid = 10000048
        bargain.create_bargain_act(productid, productname, productitemNo, shopname, shopid)
        res1 = bargain.get_bargain_act_list()
        bargainactid = res1[1].get("Data").get("PagedList")[0].get("Id")
        bargain.set_act_enable(bargainactid)
        res2 = bargain.get_bargain_act_dtl(bargainactid)
        actid = res2[1].get("Data")[0].get("Id")
        response = bargain.update_bargain_act_dtl(bargainactid, actid)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_getactstockrecord(self, bargain, env):
        global productid, productname, productitemNo, shopname, shopid
        if env == "q1":
            productid = 2830924
            productname = "鞋套"
            productitemNo = "tttop0527super030"
            shopname = "wdy%测试门店"
            shopid = 21172697
        elif env == "tp":
            productid = 12976808
            productname = "牛仔裤 随心搭配"
            productitemNo = "GZYtestitem0529"
            shopname = "WDY测试门店"
            shopid = 10000048
        bargain.create_bargain_act(productid, productname, productitemNo, shopname, shopid)
        res1 = bargain.get_bargain_act_list()
        bargainactid = res1[1].get("Data").get("PagedList")[0].get("Id")
        bargain.set_act_enable(bargainactid)
        res2 = bargain.get_bargain_act_dtl(bargainactid)
        actid = res2[1].get("Data")[0].get("Id")
        bargain.update_bargain_act_dtl(bargainactid, actid)
        response = bargain.get_act_stock_record(bargainactid)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_exportbargainlist(self, bargain):
        response = bargain.export_bargain_list()
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_getbargainactshopinfo(self, bargain, env):
        global productid, productname, productitemNo, shopname, shopid
        if env == "q1":
            productid = 2830924
            productname = "鞋套"
            productitemNo = "tttop0527super030"
            shopname = "wdy%测试门店"
            shopid = 21172697
        elif env == "tp":
            productid = 12976808
            productname = "牛仔裤 随心搭配"
            productitemNo = "GZYtestitem0529"
            shopname = "WDY测试门店"
            shopid = 10000048
        bargain.create_bargain_act(productid, productname, productitemNo, shopname, shopid)
        res = bargain.get_bargain_act_list()
        id = res[1].get("Data").get("PagedList")[0].get("Id")
        response = bargain.get_bargain_act_shop_info(id)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_getbargainactlistlink(self, bargain):
        response = bargain.get_bargain_act_list_link()
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_getbargainactconfiginfo(self, bargain):
        response = bargain.get_bargain_act_config_info()
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True
