# ArticleRepository.py
from database import get_session
from src.main.python.models import Article
from src.main.python.schemas import ArticleSchema
import json

def find_all_articles():
    session = get_session()
    try:
        articles = session.query(Article).all()
        article_schema = ArticleSchema(many=True)
        articles_dict = article_schema.dump(articles)
        return articles_dict
    finally:
        session.close()

if __name__ == '__main__':
    articles = find_all_articles()
    articles_json = json.dumps(articles, ensure_ascii=False, indent=4)
    print(articles_json)