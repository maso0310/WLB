# 使用 Python 3.10 的官方基礎映像檔
FROM python:3.10

# 設定工作目錄
WORKDIR /app

# 安裝 Google Chrome
RUN apt-get update -y && \
    apt-get install -y wget && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' && \
    apt-get update -y && \
    apt-get install -y google-chrome-stable

# 複製當前目錄下的所有檔案到容器的 /app 目錄
COPY . /app

# 安裝任何需要的套件
RUN pip install --no-cache-dir -r requirements.txt

# 定義環境變數（如果有需要）
# ENV NAME World

# 設定容器將要執行的命令
CMD ["gunicorn", "app:app"]
