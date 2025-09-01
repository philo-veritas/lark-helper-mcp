#!/usr/bin/env python3
"""
MCP Server 入口点
"""

import sys
from pathlib import Path

# 将 src 目录添加到 Python 路径
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from lark_helper_mcp.server import main

if __name__ == "__main__":
    main()
