# src/main/python/schemas.py
from marshmallow import Schema, fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from src.main.python.models import Article, User, Comment

class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    nickname = fields.Str()
    role = fields.Str()

class ArticleSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Article
        load_instance = True

    id = fields.Int(dump_only=True)
    title = fields.Str()
    content = fields.Str()
    author_id = fields.Int()
    created_at = fields.Int()
    label = fields.Str()
    author = fields.Nested(UserSchema, only=('id', 'username', 'nickname', 'role'))

class CommentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Comment
        load_instance = True

    id = fields.Int(dump_only=True)
    content = fields.Str()
    article_id = fields.Int()
    user_id = fields.Int()
    created_at = fields.Int()
    user = fields.Nested(UserSchema, only=('id', 'username', 'nickname', 'role'))

# 单个文章序列化器
article_schema = ArticleSchema()

# 多个文章序列化器
articles_schema = ArticleSchema(many=True)

# 单个评论序列化器
comment_schema = CommentSchema()

# 多个评论序列化器
comments_schema = CommentSchema(many=True)