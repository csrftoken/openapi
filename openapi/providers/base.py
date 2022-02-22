#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2021/10/8

import logging


class OpenAPI(object):
    name = 'OpenApi'
    API_BASE_URL = None
    API_VERSION = None

    def enable_logger(self, logger=None):
        if logger is None:
            if self._logger is not None:
                return
            logger = logging.getLogger(__name__)
        self._logger = logger

    def disable_logger(self):
        self._logger = None
