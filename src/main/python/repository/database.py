# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import Config

# 创建数据库引擎
engine = create_engine(Config().DB_URL, echo=True)

# 创建会话工厂
Session = sessionmaker(bind=engine)

# 创建会话
def get_session():
    return Session()