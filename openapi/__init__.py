r"""
 ______     ______   ______     __   __     ______     ______   __
/\  __ \   /\  == \ /\  ___\   /\ "-.\ \   /\  __ \   /\  == \ /\ \
\ \ \/\ \  \ \  _-/ \ \  __\   \ \ \-.  \  \ \  __ \  \ \  _-/ \ \ \
 \ \_____\  \ \_\    \ \_____\  \ \_\\"\_\  \ \_\ \_\  \ \_\    \ \_\
  \/_____/   \/_/     \/_____/   \/_/ \/_/   \/_/\/_/   \/_/     \/_/

"""

VERSION = (0, 0, 1, "final", 0)

__title__ = "openapi"
__version_info__ = VERSION
__version__ = ".".join(map(str, VERSION[:3])) + (
    "-{}{}".format(VERSION[3], VERSION[4] or "") if VERSION[3] != "final" else ""
)
__author__ = "ZhiChao Liu"
__license__ = "MIT"
__copyright__ = "Copyright 2021"
