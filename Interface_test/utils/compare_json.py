import json
import logging

import allure


def compare_json_data(data1, data2):
    mismatched_keys = compare_json_keys(data1, data2)
    mismatched_value_types = compare_json_value_types(data1, data2)

    log_messages = []

    if mismatched_keys or mismatched_value_types:
        logging.warning("JSON 数据不一致:")
        log_messages.append("JSON 数据不一致:")
        if mismatched_keys:
            logging.warning("不一致的键:")
            log_messages.append("不一致的键:")
            for key in mismatched_keys:
                logging.warning(f"{key}")
                log_messages.append(f"{key}")
        if mismatched_value_types:
            logging.info("值类型不一致的键和类型:")
            log_messages.append("值类型不一致的键和类型:")
            for key, value_type in mismatched_value_types.items():
                logging.info(f"{key} ({value_type})")
                log_messages.append(f"{key} ({value_type})")
        result = False
    else:
        logging.info("JSON 数据一致")
        log_messages.append("JSON 数据一致")
        result = True

    allure.attach("\n".join(log_messages), name="JSON Compare Result", attachment_type=allure.attachment_type.TEXT)
    return result



def compare_json_keys(data1, data2, path=""):
    mismatched_keys = set()

    if isinstance(data1, dict) and isinstance(data2, dict):
        for key in data1:
            if key not in data2:
                mismatched_keys.add(f"{path}.{key}")
            else:
                result = compare_json_keys(data1[key], data2[key], f"{path}.{key}")
                mismatched_keys |= result
    else:
        if isinstance(data1, list) and isinstance(data2, list):
            min_length = min(len(data1), len(data2))
            for i in range(min_length):
                result = compare_json_keys(data1[i], data2[i], f"{path}[{i}]")
                mismatched_keys |= result

            if len(data1) > len(data2):
                for i in range(min_length, len(data1)):
                    mismatched_keys.add(f"{path}[{i}]")
        #     for i in range(min(len(data1), len(data2))):
        #         result = compare_json_keys(data1[i], data2[i], f"{path}[{i}]")
        #         mismatched_keys |= result
        # # elif type(data1) != type(data2):
        # #     mismatched_keys.add(path)

    return mismatched_keys


def compare_json_value_types(data1, data2, path=""):
    mismatched_value_types = {}

    if isinstance(data1, dict) and isinstance(data2, dict):
        for key in data1:
            if key in data2:
                result = compare_json_value_types(data1[key], data2[key], f"{path}.{key}")
                mismatched_value_types.update(result)
    else:
        if isinstance(data1, list) and isinstance(data2, list):
            for i in range(min(len(data1), len(data2))):
                result = compare_json_value_types(data1[i], data2[i], f"{path}[{i}]")
                mismatched_value_types.update(result)
        elif type(data1) != type(data2):
            mismatched_value_types[path] = f"{type(data1).__name__} vs {type(data2).__name__}"

    return mismatched_value_types

# 测试数据
# json_data1 = {"key1": 5.6, "key2": "text", "key3": [{"a": 123, "b": 456, "c": 789}, {"d": 123}], "key4": 2, "key5": 3}
# json_data2 = {"key1": "value1", "key2": 123, "key3": [{"a": "aaa", "b": 123}], "key4": ["val1", "val2"]}

# compare_json_data(json_data1, json_data2)

# def compare_json_types(data1, data2):
#     # 比较键的类型
#     if type(data1) != type(data2):
#         return False
#
#     # 如果是字典类型，递归比较其键值对的类型
#     if isinstance(data1, dict):
#         if len(data1) != len(data2):
#             return False
#         for key in data1:
#             if key not in data2:
#                 return False
#             if not compare_json_types(data1[key], data2[key]):
#                 return False
#
#     # 如果是列表类型，递归比较其元素的类型
#     elif isinstance(data1, list):
#         if len(data1) != len(data2):
#             return False
#         for i in range(len(data1)):
#             if not compare_json_types(data1[i], data2[i]):
#                 return False
#
#     return True


# def compare_json_types(data1, data2, path=""):
#
#     if type(data1) != type(data2):
#         print(f"类型不一致: {path} ({type(data1)} vs {type(data2)})")
#         return False
#
#     if isinstance(data1, dict):
#         # # 如果新接口返回的数据少于老接口返回的数据
#         # if len(data1) > len(data2):
#         #     print(f"老数据键数量为: {len(data1)}")
#         #     print(f"新数据键数量为: {len(data2)}")
#         #     print(f"键数量不一致: {path}")
#         #     for key in data1:
#         #         if key not in data2:
#         #             print(f"键不一致: {path}.{key}")
#         #     return False
#
#         # if len(data1) != len(data2):
#         #     print(f"老数据键数量为: {len(data1)}")
#         #     print(f"新数据键数量为: {len(data2)}")
#         #     print(f"键数量不一致: {path}")
#         #     for key in data1:
#         #         if key not in data2:
#         #             print(f"键不一致: {path}.{key}")
#         #     return False
#         for key in data1:
#             if key not in data2:
#                 print(f"键不一致: {path}.{key}")
#                 return False
#             if not compare_json_types(data1[key], data2[key], f"{path}.{key}"):
#                 return False
#
#     elif isinstance(data1, list):
#         if len(data1) != len(data2):
#             print(f"列表长度不一致: {path}")
#             return False
#         for i in range(len(data1)):
#             if not compare_json_types(data1[i], data2[i], f"{path}[{i}]"):
#                 return False
#
#     return True

# # 原始的 JSON 数据
# json_data1 = '{"key1": "value1", "key2": 123}'
# json_data2 = '{"key1": "5.6", "key3": 456}'
#
# # 将 JSON 数据解析为 Python 对象
# data1 = json.loads(json_data1)
# data2 = json.loads(json_data2)
#
# # 比较类型
# if compare_json_types(data1, data2):
#     print("JSON 数据的键和值类型一致")
# else:
#     print("JSON 数据的键和值类型不一致")
