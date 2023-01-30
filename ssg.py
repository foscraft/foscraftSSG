import os
from datetime import datetime

from jinja2 import (
    Environment,
    PackageLoader,
)
from markdown2 import markdown

articles = {}

for md_article in os.listdir("components"):
    file_path = os.path.join("components", md_article)

    with open(file_path, "r") as f:
        articles[md_article] = markdown(f.read(), extras=["metadata"])

        articles = {
            article: articles[article]
            for article in sorted(
                articles,
                key=lambda article: datetime.strptime(
                    articles[article].metadata["date"], "%Y-%m-%d"
                ),
                reverse=True,
            )
        }
        env = Environment(loader=PackageLoader("ssg", "templates"))
        home_template = env.get_template("home.html")
        article_template = env.get_template("article.html")

        articles_metadata = [
            articles[article].metadata for article in articles
        ]
        home_html = home_template.render(articles=articles_metadata)
