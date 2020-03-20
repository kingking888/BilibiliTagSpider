#!/usr/bin/env python
"""处理某个分区下，一段日期内的视频，所包含的标签。"""

import argparse

from helpers import *
from BilibiliTagHandler.tag_handler import TagHandler
from BilibiliTagWeb import settings

# 命令行参数
#     - type_id   -- 分区id
#     - time-from -- 起始日期（输入格式yyyyMMdd)
#     - time-to   -- 结束日期
parser = argparse.ArgumentParser()
parser.add_argument("--type-id", type=int, default=0)
parser.add_argument("--time-from", type=str, default="20100101")
parser.add_argument("--time-to", type=str, default="20100101")
args = parser.parse_args()

type_id = args.type_id
time_from = date_to_timestamp(args.time_from)
time_to_end = date_to_timestamp(args.time_to) + 24 * 3600

# 连接mongo并处理标签
mongo_settings = settings.DATABASES['default']
handler = TagHandler(mongo_settings['HOST'],
                    mongo_settings['NAME'],
                    mongo_settings['USER'],
                    mongo_settings['PASSWORD']) 
print("return", handler.start(type_id, time_from, time_to_end))
# result = handler.get_tag_count_rank(type_id, time_from, time_to_end, 10)
# print(result)
# handler.test()