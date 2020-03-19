import os

BASE_DIR = os.getenv("BASE_DIR", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CORS_WHITE = os.getenv("CORS_WHITELIST", '*')
DB_NAME = os.getenv("DB_NAME", "xiaosu")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = os.getenv("DB_PORT", "3306")
REDIS_HOST = os.getenv("REDIS_HOST", "127.0.0.1")
REDIS_PORT = os.getenv("REDIS_PORT", "6379")

# PC_URL = os.getenv("PC_URL", "http://10.168.2.100:8080")  # PC端页面地址
# API_URL = os.getenv("API_URL", "http://10.168.2.100:8000")  # PC端接口地址
# MOBILE_URL = os.getenv("MOBILE_URL", "http://10.168.2.100:8000")  # 手机端页面地址

# PAYMENT_NOTIFY_URL = os.getenv("PAYMENT_NOTIFY_URL", "https://81c55584.ngrok.io" + "/paypal/")  # paypal接收通知地址，必须https

# ONLINE_URL = PC_URL  # 前端地址
# ONLINE_PAYMENT_RETURN_URL = PC_URL + "/orders/pay/success/"
# ONLINE_PAYMENT_CANCEL_URL = PC_URL + "/orders/"
