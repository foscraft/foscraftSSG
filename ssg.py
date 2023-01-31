import os
from datetime import datetime

from jinja2 import (
    Environment,
    PackageLoader,
)
from markdown2 import markdown

articles = {}

for md_article in os.listdir("markdownfiles"):
    file_path = os.path.join("markdownfiles", md_article)

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

articles_metadata = [articles[article].metadata for article in articles]
tags = [article["tags"] for article in articles_metadata]
home_html = home_template.render(articles=articles_metadata, tags=tags)

with open("index.html", "w") as f:
    f.write(home_html)

    for article in articles:
        article_metadata = articles[article].metadata

        article_data = {
            "content": articles[article],
            "title": article_metadata["title"],
            "date": article_metadata["date"],
        }

        article_html = article_template.render(article=article_data)

        article_file_path = "articles/{slug}.html".format(
            slug=article_metadata["slug"]
        )

        os.makedirs(os.path.dirname(article_file_path), exist_ok=True)
        with open(article_file_path, "w") as f:
            f.write(article_html)
