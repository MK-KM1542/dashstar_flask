# src/main/python/models.py
from sqlalchemy import Column, Integer, String, BigInteger, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), unique=True, nullable=False)
    nickname = Column(String(255))
    password = Column(String, nullable=False)
    role = Column(String(50), default='user')

    articles = relationship('Article', back_populates='author')
    comments = relationship('Comment', back_populates='user')


class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    content = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(BigInteger, default=lambda: int(datetime.utcnow().timestamp()))
    label = Column(String(255))

    author = relationship('User', back_populates='articles')
    comments = relationship('Comment', back_populates='article')


class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String, nullable=False)
    article_id = Column(Integer, ForeignKey('articles.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(BigInteger, default=lambda: int(datetime.utcnow().timestamp()))

    article = relationship('Article', back_populates='comments')
    user = relationship('User', back_populates='comments')