#!/usr/bin/env python
# Copyright: (c) OpenSpug Organization. https://github.com/openspug/spug
# Copyright: (c) <spug.dev@gmail.com>
# Released under the AGPL-3.0 License.
"""Django's command-line utility for administrative tasks."""
"""
这个脚本允许你从命令行运行Django管理命令，并确保在运行这些命令之前Django的环境设置是正确的
"""

import os
import sys


def main():

    # 设置Django环境变量
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spug.settings')

    # 导入Django
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # 执行Django命令
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
