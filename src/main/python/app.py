# src/main/python/app.py
from flask import Flask, jsonify
from src.main.python.repository.database import get_session
from src.main.python.models import Article, Comment
from src.main.python.schemas import article_schema, articles_schema, comment_schema, comments_schema

app = Flask(__name__)

@app.route('/api/articles', methods=['GET'])
def get_all_articles():
    session = get_session()
    try:
        articles = session.query(Article).all()
        articles_dict = articles_schema.dump(articles)
        response = {
            "code": "OK",
            "data": articles_dict,
            "totalArticles": len(articles)
        }
        return jsonify(response), 200
    finally:
        session.close()

@app.route('/api/articles/<int:article_id>', methods=['GET'])
def get_article_by_id(article_id):
    session = get_session()
    try:
        article = session.query(Article).filter(Article.id == article_id).first()
        if article is None:
            return jsonify({"code": "NOT_FOUND", "message": "Article not found"}), 404
        article_dict = article_schema.dump(article)  # 确保使用单个对象的序列化器
        response = {
            "code": "OK",
            "data": article_dict
        }
        return jsonify(response), 200
    finally:
        session.close()

@app.route('/api/articles/<int:article_id>/comments', methods=['GET'])
def get_comments_by_article_id(article_id):
    session = get_session()
    try:
        comments = session.query(Comment).filter(Comment.article_id == article_id).all()
        if not comments:
            return jsonify({"code": "NOT_FOUND", "message": "No comments found for this article"}), 404
        comments_dict = comments_schema.dump(comments)
        response = {
            "code": "OK",
            "data": comments_dict
        }
        return jsonify(response), 200
    finally:
        session.close()


if __name__ == '__main__':
    app.run(debug=True, port=8080)