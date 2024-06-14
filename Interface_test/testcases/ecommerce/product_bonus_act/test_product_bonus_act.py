import logging

import allure
import pytest

from apis.ecommerce.product_bonus_act.product_bonus_act import ProductBonusAct
from utils.compare_json import compare_json_data
from utils.file_tools import FileTool


# from Interface_test.apis.ecommerce.product_bonus_act.product_bonus_act import ProductBonusAct
# from Interface_test.utils.compare_json import compare_json_data

# 实例化夹子函数
@pytest.fixture(scope="class")
def productbonusact(env_config):
    yield ProductBonusAct(env_config)


@allure.suite("积分兑换")
@allure.feature("积分兑换")
class TestProductBonusAct:
    @pytest.fixture()
    def env(self, env_config):
        yield env_config

    def test_getlist(self, productbonusact):
        response = productbonusact.get_list("", "")
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_savedata(self, productbonusact, env):
        global payload
        data = FileTool.read_yaml("ProductBonusAct_save")
        if env == "q1":
            payload = data.get("q1").get("payload")
        elif env == "tp":
            payload = data.get("tp").get("payload")

        response = productbonusact.save_data(payload)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_enablebonusact(self, productbonusact, env):
        global payload
        data = FileTool.read_yaml("ProductBonusAct_save")
        if env == "q1":
            payload = data.get("q1").get("payload")
        elif env == "tp":
            payload = data.get("tp").get("payload")

        res = productbonusact.save_data(payload)
        ids = res[1].get("Data").get("Id")
        response = productbonusact.enable_bonus_act(ids)
        productbonusact.disabled_bonus_act(ids)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_disabledbonusact(self, productbonusact, env):
        global payload
        data = FileTool.read_yaml("ProductBonusAct_save")
        if env == "q1":
            payload = data.get("q1").get("payload")
        elif env == "tp":
            payload = data.get("tp").get("payload")

        res = productbonusact.save_data(payload)
        ids = res[1].get("Data").get("Id")
        productbonusact.enable_bonus_act(ids)
        # # 获取需要禁用活动的ids
        # res = productbonusact.get_list("sku98765", "")
        # pagelist = res[1].get("Data").get("PagedList")
        # ids = ', '.join([str(item['Id']) for item in pagelist])

        response = productbonusact.disabled_bonus_act(ids)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_getbyid(self, productbonusact):
        res = productbonusact.get_list("", "")
        id = res[1].get("Data").get("PagedList")[0].get("Id")
        response = productbonusact.get_by_id(id)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_getbonusactcfg(self, productbonusact):
        response = productbonusact.get_bonus_act_cfg()
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_getbonusgrouplist(self, productbonusact):
        response = productbonusact.get_bonus_group_list()
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_getpagelink(self, productbonusact):
        response = productbonusact.get_page_link()
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_getbonuspool(self, productbonusact):
        response = productbonusact.get_bonus_pool()
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_addbonuspool(self, productbonusact):
        res = productbonusact.get_list("", 2)
        actids = res[1].get("Data").get("PagedList")[-1].get("Id")

        response = productbonusact.add_bonus_pool(actids)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_delbonuspool(self, productbonusact):
        poolid = productbonusact.get_bonus_pool()[1].get("Data").get("PagedList")[0].get("Id")
        response = productbonusact.del_bonus_pool(poolid)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_updatebonusactcfgstatus(self, productbonusact):
        response = productbonusact.update_bonus_act_cfg_status()
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_updatebonusactcfg(self, productbonusact):
        response = productbonusact.update_bonus_act_cfg()
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_getactcfgoperationlog(self, productbonusact):
        res = productbonusact.get_list("", "")
        id = res[1].get("Data").get("PagedList")[0].get("Id")
        response = productbonusact.get_act_cfg_operation_log(id)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_savebonusgroupinfo(self, productbonusact, env):
        global id
        if env == "q1":
            id = 50056
        elif env == "tp":
            id = 50016
        response = productbonusact.save_bonus_group_info(id)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_getpoolinfobyid(self, productbonusact):
        res = productbonusact.get_bonus_pool()
        poolid = res[1].get("Data").get("PagedList")[0].get("Id")

        response = productbonusact.get_pool_info_by_id(poolid)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_getactlist(self, productbonusact):
        response = productbonusact.get_act_list()
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_getbonusactbygroupid(self, productbonusact):
        res = productbonusact.get_bonus_group_list()
        pagelist = res[1].get("Data").get("PagedList")
        groupid = next(item['Id'] for item in pagelist if item['ActCount'] > 0)
        response = productbonusact.get_bonus_act_by_group_id(groupid)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_savegroupbonussort(self, productbonusact):
        res1 = productbonusact.get_bonus_group_list()
        pagelist = res1[1].get("Data").get("PagedList")
        groupid = next(item['Id'] for item in pagelist if item['ActCount'] > 0)

        res2 = productbonusact.get_bonus_act_by_group_id(groupid)
        Id = res2[1].get("Data").get("PagedList")[0].get("Id")

        response = productbonusact.save_group_bonus_sort(Id)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_updatebonusgroupstatus(self, productbonusact):
        res = productbonusact.get_bonus_group_list()
        pagelist = res[1].get("Data").get("PagedList")
        groupid = next(item['Id'] for item in pagelist if item['ActCount'] > 0)
        response = productbonusact.update_bonus_group_status(groupid)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_getpooldtl(self, productbonusact):
        res = productbonusact.get_bonus_pool()
        poolid = res[1].get("Data").get("PagedList")[0].get("Id")

        response = productbonusact.get_pool_dtl(poolid)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_releaseproduct(self, productbonusact, env):
        global payload
        data = FileTool.read_yaml("ProductBonusAct_save")
        if env == "q1":
            payload = data.get("q1").get("payload")
        elif env == "tp":
            payload = data.get("tp").get("payload")
        res = productbonusact.save_data(payload)
        id = res[1].get("Data").get("Id")
        response = productbonusact.release_product(id)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_batchreleaseactpro(self, productbonusact, env):
        global payload
        data = FileTool.read_yaml("ProductBonusAct_save")
        if env == "q1":
            payload = data.get("q1").get("payload")
        elif env == "tp":
            payload = data.get("tp").get("payload")
        res = productbonusact.save_data(payload)
        id1 = res[0].get("Data").get("Id")
        id2 = res[1].get("Data").get("Id")
        ids = [id1, id2]
        response = productbonusact.batch_release_act_pro(ids)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_outexcel(self, productbonusact):
        response = productbonusact.out_excel()
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_importdatas(self, productbonusact):
        response = productbonusact.import_datas("积分兑换导入表")
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True

    def test_updatebonusgroup(self, productbonusact):
        res1 = productbonusact.get_list("", 2)
        actid = res1[1].get("Data").get("PagedList")[-1].get("Id")
        print(actid)

        res2 = productbonusact.get_bonus_group_list()
        pagelist = res2[1].get("Data").get("PagedList")
        groupid = next(item['Id'] for item in pagelist if item['ActCount'] > 0)

        response = productbonusact.update_bonus_group(actid, groupid)
        logging.info(response)
        allure.attach(str(response), name="Response", attachment_type=allure.attachment_type.JSON)
        result = compare_json_data(response[0], response[1])
        if result:
            allure.attach("JSON 数据的键和值类型一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("JSON 数据的键和值类型不一致", name="Result", attachment_type=allure.attachment_type.TEXT)
        assert result is True
