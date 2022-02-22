#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2022/2/23

from ..base import OpenAPI


class DouDianApi(OpenAPI):
    name = 'dou-dian api'
    API_BASE_URL = 'https://openapi-fxg.jinritemai.com/'
    API_VERSION = 2

    def _request(self, path, params):
        return {}

    def request(self, path: str, params: dict) -> dict:
        """请求抖店API接口
        :param path: 调用的API接口地址，示例：'product/listV2'
        :param params: 业务参数，示例：{'page': 1, 'size': 100}
        """
        return self._request(path=path, params=params)
