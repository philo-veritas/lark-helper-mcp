#!/usr/bin/env python3
"""
配置文件 - 管理API endpoints和其他配置信息
"""

import os


class Config:
    """配置类"""

    def __init__(self):
        # 飞书应用配置
        self.lark_app_id = os.getenv("LARK_APP_ID", "")
        self.lark_app_secret = os.getenv("LARK_APP_SECRET", "")

    def validate_config(self) -> list:
        """验证配置是否完整"""
        errors = []

        return errors


# 创建全局配置实例
config = Config()
