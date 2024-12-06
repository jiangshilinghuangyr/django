# 使用官方 Python 基础镜像
FROM python:3.11-slim

# 安装系统依赖，特别是 mysqlclient 和其他构建工具
RUN apt-get update && apt-get install -y \
    pkg-config \
    libmariadb-dev \
    build-essential

# 设置工作目录
WORKDIR /app

# 复制项目文件
COPY . /app

# 安装项目依赖
RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt



# 收集静态文件（如果需要）
RUN python manage.py collectstatic --noinput

# 启动命令
CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000"]
