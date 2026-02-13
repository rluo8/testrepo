# Test Repository - Cython Coverage Demo

这是一个展示如何正确配置 Cython Coverage 的示例项目。

## 📁 项目结构

```
testrepo/
├── mypackage/                      # Python 包
│   ├── __init__.py                # 包入口
│   ├── calculator.py              # 纯 Python 模块
│   └── cython_math.pyx            # Cython 模块（性能优化）
├── tests/                         # 测试目录
│   ├── test_calculator.py         # calculator 测试
│   └── test_cython_math.py        # cython_math 测试
├── .github/workflows/             # CI/CD
│   └── coverage.yml               # 自动化测试和 Codecov 上传
├── setup.py                       # 构建配置
├── pyproject.toml                 # 项目元数据
├── .coveragerc                    # Coverage 配置
├── run_coverage.bat               # Windows 本地运行脚本
├── run_coverage.sh                # Linux/Mac 本地运行脚本
├── rebuild_coverage.bat           # Windows 重建脚本
├── CYTHON_COVERAGE_DEBUG.md       # ⭐ 详细调试文档
└── README.md                      # 本文件
```

## 🚀 快速开始

### 本地开发（Windows）

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 重建（带 coverage 支持）
rebuild_coverage.bat

# 3. 运行测试和 coverage
run_coverage.bat
```

### 本地开发（Linux/Mac）

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 重建（带 coverage 支持）
export COVERAGE_MODE=1
python setup.py build_ext --inplace

# 3. 运行测试和 coverage
./run_coverage.sh
```
