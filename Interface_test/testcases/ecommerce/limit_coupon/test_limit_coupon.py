import logging
import time

import allure
import pytest

from apis.ecommerce.limit_coupon.limit_coupon import LimitCoupon
from utils.compare_json import compare_json_data


# 实例化夹子函数
@pytest.fixture(scope="class")
def limitcoupon(env_config):
    yield LimitCoupon(env_config)


@allure.suite("限券抢购")
@allure.feature("限券抢购")
class TestLimitCoupon:
    @pytest.fixture()
    def env(self, env_config):
        yield env_config

    def test_getactcfgoperationlog(self, limitcoupon):
        res = limitcoupon.get_list()
        id = res[1].get("Data").get("PagedList")[0].get("Id")
        response = limitcoupon.get_act_cfg_operation_log(id)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_getlist(self, limitcoupon):
        response = limitcoupon.get_list()
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_setisenable(self, limitcoupon, env):
        global productid, couponid, couponname, shopid
        if env == "q1":
            productid = 2830922
            couponid = 79527
            couponname = "Hubert_邀请券_无门槛"
            shopid = 21172697
        elif env == "tp":
            productid = 12976798
            couponid = 274
            couponname = "dd无门槛邀请券"
            shopid = 10000048
        limitcoupon.save(productid, couponid, couponname, shopid)
        res = limitcoupon.get_list()
        id = res[1].get("Data").get("PagedList")[0].get("Id")
        response = limitcoupon.set_is_enable(id, "false")
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        time.sleep(3)
        limitcoupon.set_is_enable(id, "true")
        time.sleep(3)
        limitcoupon.set_is_release(id)
        assert result is True

    def test_setisrelease(self, limitcoupon, env):
        global productid, couponid, couponname, shopid
        if env == "q1":
            productid = 2830922
            couponid = 79527
            couponname = "Hubert_邀请券_无门槛"
            shopid = 21172697
        elif env == "tp":
            productid = 12976798
            couponid = 274
            couponname = "dd无门槛邀请券"
            shopid = 10000048
        limitcoupon.save(productid, couponid, couponname, shopid)
        res = limitcoupon.get_list()
        id = res[1].get("Data").get("PagedList")[0].get("Id")
        limitcoupon.set_is_enable(id, "false")
        time.sleep(3)
        limitcoupon.set_is_enable(id, "true")
        time.sleep(3)
        response = limitcoupon.set_is_release(id)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_getlimitcouponinfo(self, limitcoupon):
        res = limitcoupon.get_list()
        id = res[1].get("Data").get("PagedList")[0].get("Id")
        response = limitcoupon.get_limit_coupon_info(id)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_limitcouponcheck(self, limitcoupon, env):
        global productid, shopid
        if env == "q1":
            productid = 2830922
            shopid = 21172697
        elif env == "tp":
            productid = 12976798
            shopid = 10000048
        response = limitcoupon.limit_coupon_check(productid, shopid)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_save(self, limitcoupon, env):
        global productid, couponid, couponname, shopid
        if env == "q1":
            productid = 2830922
            couponid = 79527
            couponname = "Hubert_邀请券_无门槛"
            shopid = 21172697
        elif env == "tp":
            productid = 12976798
            couponid = 274
            couponname = "dd无门槛邀请券"
            shopid = 10000048
        response = limitcoupon.save(productid, couponid, couponname, shopid)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True
