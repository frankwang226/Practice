import concurrent.futures
import threading

import requests

url = "https://wxa-tp.ezrpro.com/home/Mall/Trade/SubmitOrder"

header = {"ezr-sv": "1",
          "ezr-sp": "2",
          "ezr-userid": "oBtnQt8AqCW6BRvZ8o1YuUPoXQdU",
          "ezr-brand-id": "186",
          "ezr-cop-id": "86",
          "uber-trace-id": "cb4de6129fd90276:cb4de6129fd90276:0:1",
          "ezr-vuid": "14356012",
          "ezr-st": "1715671824754",
          "ezr-source": "weapp",
          "ezr-ss": "24b0bdb64e0897966587b8f8543ce873fa501abd",
          "Accept-Encoding": "gzip,compress,br,deflate",
          "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.43(0x18002b2f) NetType/WIFI Language/zh_CN",
          "Referer": "https://servicewechat.com/wx5beca244ced909cd/0/page-frame.html",
          "Connection": "keep-alive"}

payload = {"ActId": 270854, "Action": 1, "ActType": 7, "AddressId": 13051395,
           "BonusForCash": {"Amount": 0.2, "Bonus": 20, "IsSelect": "false"}, "BuyerRemark": "", "Coupons": [],
           "DelivType": 0, "ExpressFee": {"ExpressFeeType": "MY", "ExpressFee": 0, "RuleId": -1, "ExpressBonus": 0,
                                          "ExpressFeeMsg": ""}, "InviteCoupons": [], "PackActDiscountAmount": 1591.9,
           "PassCode": "", "PayAmount": 1, "PayBonus": 0, "PayType": 0,
           "PrepayCard": {"EzrPrepayCards": [], "UseThirdPrepaidCard": "false", "UseThirdPrepaidCardAmount": 0},
           "ReductionAmount": 0, "RequireOrder": 0, "SelfFetchShopId": 0, "ShopId": 10000048, "Skus": [
        {"GiftActId": 0, "ActType": 0, "Bonus": 0, "Qty": 1, "SkuId": 19588357, "ShoppingCartId": 666,
         "CustomFieldsList": []},
        {"GiftActId": 0, "ActType": 0, "Bonus": 0, "Qty": 1, "SkuId": 19588356, "ShoppingCartId": 667,
         "CustomFieldsList": []},
        {"GiftActId": 0, "ActType": 0, "Bonus": 0, "Qty": 1, "SkuId": 1533, "ShoppingCartId": 668,
         "CustomFieldsList": []},
        {"GiftActId": 0, "ActType": 0, "Bonus": 0, "Qty": 1, "SkuId": 1298, "ShoppingCartId": 669,
         "CustomFieldsList": []},
        {"GiftActId": 0, "ActType": 0, "Bonus": 0, "Qty": 1, "SkuId": 1296, "ShoppingCartId": 670,
         "CustomFieldsList": []},
        {"GiftActId": 0, "ActType": 0, "Bonus": 0, "Qty": 1, "SkuId": 1131, "ShoppingCartId": 671,
         "CustomFieldsList": []},
        {"GiftActId": 0, "ActType": 0, "Bonus": 0, "Qty": 1, "SkuId": 1129, "ShoppingCartId": 672,
         "CustomFieldsList": []},
        {"GiftActId": 0, "ActType": 0, "Bonus": 0, "Qty": 1, "SkuId": 838, "ShoppingCartId": 673,
         "CustomFieldsList": []},
        {"GiftActId": 0, "ActType": 0, "Bonus": 0, "Qty": 1, "SkuId": 837, "ShoppingCartId": 674,
         "CustomFieldsList": []},
        {"GiftActId": 0, "ActType": 0, "Bonus": 0, "Qty": 1, "SkuId": 744, "ShoppingCartId": 675,
         "CustomFieldsList": []},
        {"GiftActId": 0, "ActType": 0, "Bonus": 0, "Qty": 1, "SkuId": 1506, "ShoppingCartId": 676,
         "CustomFieldsList": []},
        {"GiftActId": 0, "ActType": 0, "Bonus": 0, "Qty": 1, "SkuId": 19583989, "ShoppingCartId": 677,
         "CustomFieldsList": []},
        {"GiftActId": 0, "ActType": 0, "Bonus": 0, "Qty": 1, "SkuId": 13822103, "ShoppingCartId": 678,
         "CustomFieldsList": []},
        {"GiftActId": 0, "ActType": 0, "Bonus": 0, "Qty": 1, "SkuId": 13822090, "ShoppingCartId": 679,
         "CustomFieldsList": []},
        {"GiftActId": 0, "ActType": 0, "Bonus": 0, "Qty": 1, "SkuId": 13822085, "ShoppingCartId": 680,
         "CustomFieldsList": []},
        {"GiftActId": 0, "ActType": 0, "Bonus": 0, "Qty": 1, "SkuId": 19669379, "ShoppingCartId": 681,
         "CustomFieldsList": [{"Id": 50020, "Name": "老多选", "IsRequired": "false", "Type": 3, "OptionContentList": [],
                               "SelectOptionContentList": [], "FormatCheck": 0, "SerialNumber": 0},
                              {"Id": 50019, "Name": "老单选", "IsRequired": "false", "Type": 2, "OptionContentList": [],
                               "SelectOptionContentList": [], "FormatCheck": 0, "SerialNumber": 0},
                              {"Id": 50018, "Name": "老文本", "IsRequired": "false", "Type": 1, "OptionContentList": [],
                               "SelectOptionContentList": [], "FormatCheck": 0, "SerialNumber": 0}]},
        {"GiftActId": 0, "ActType": 0, "Bonus": 0, "Qty": 1, "SkuId": 13811473, "ShoppingCartId": 682,
         "CustomFieldsList": []}], "TraceId": "", "ValetOrderSign": "", "SelectCouponGiftList": [], "Exts": [],
           "ChannelSource": 1089, "ChannelType": {}, "CommunitySgId": 0, "CustomChannel": "",
           "OpenId": "ocBN75fozyDQET19r7YISNn5QCh0", "SessionId": "20240514162614ec27afbc-a9ea-4bd5-a736-0ee887f31f78",
           "Version": 20240112}

requests.packages.urllib3.disable_warnings()


def createorder(url, payload, header):
    for i in range(10000):
        res = requests.request(method="POST", url=url, json=payload, headers=header, verify=False)
        result = res.json()
        print(f"第{i + 1}次，状态{res.status_code}，返回:{result}")

# thread1 = threading.Thread(target=createorder, args=(url, payload, header))
# thread2 = threading.Thread(target=createorder, args=(url, payload, header))
#
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()
#
# print("创建完毕")

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(createorder, url, payload, header) for i in range(10)]

    for future in concurrent.futures.as_completed(futures):
        try:
            future.result()
        except Exception as e:
            print(f"An error occured: {str(e)}")

print("创建完毕")
