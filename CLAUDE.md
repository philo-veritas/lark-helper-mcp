# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

这是一个 **Lark Helper MCP Server** 项目，用于为 Lark（飞书）消息平台提供 MCP (Model Context Protocol) 工具集成。项目基于 FastMCP 框架构建，使用 Python 3.12+ 开发。

## 常用开发命令

### 环境和依赖管理
```bash
uv venv                    # 创建虚拟环境
uv sync                    # 安装/更新依赖
uv add <package>           # 添加新的依赖包
uv run python main.py      # 运行 MCP 服务器
```

### 代码质量检查
```bash
ruff check                 # 运行代码检查
ruff format               # 格式化代码
```

### 运行 MCP 服务器
```bash
uv run python main.py     # 启动 MCP 服务器
```

## 核心架构

### 项目结构
```
├── main.py                 # 项目入口点，设置 Python 路径并调用主函数
├── src/lark_helper_mcp/    # 核心模块目录
│   ├── __init__.py         # 包初始化文件
│   ├── config.py           # 配置管理，处理环境变量和验证
│   └── server.py           # MCP 服务器实现，包含工具注册
├── pyproject.toml          # 项目配置和依赖声明
└── uv.lock                # 锁定的依赖版本
```

### 关键组件

1. **MCP 服务器 (`src/lark_helper_mcp/server.py`)**
   - 使用 `FastMCP("Demo")` 创建 MCP 服务器实例
   - 通过 `@mcp.tool()` 装饰器注册工具函数
   - 当前包含示例工具：`add()`

2. **配置管理 (`src/lark_helper_mcp/config.py`)**
   - 管理 Lark 应用凭据：`LARK_APP_ID` 和 `LARK_APP_SECRET`
   - 提供配置验证功能
   - 使用环境变量进行配置

3. **入口点 (`main.py`)**
   - 设置 `src` 目录到 Python 路径
   - 导入并调用服务器主函数

## 开发指南

### 环境变量配置
项目需要以下环境变量：
- `LARK_APP_ID`: 飞书应用 ID
- `LARK_APP_SECRET`: 飞书应用密钥

### 添加新的 MCP 工具
1. 在 `src/lark_helper_mcp/server.py` 中定义函数
2. 使用 `@mcp.tool()` 装饰器注册
3. 添加类型注解和文档字符串
4. 实现具体的 Lark API 集成逻辑

### 代码风格要求
- 遵循 ruff 配置的代码风格（见 `pyproject.toml`）
- 目标 Python 版本：3.12
- 行长度限制：100 字符
- 启用的检查：pycodestyle、pyflakes、isort、flake8-bugbear 等

### MCP 工具模式
当前项目采用工具导向的架构：
- 每个功能作为独立的 MCP 工具实现
- 工具函数应该有明确的输入输出类型
- 使用装饰器模式进行工具注册
- 保持工具函数的原子性和可组合性