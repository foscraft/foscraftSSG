from jinja2 import (
    Environment,
    PackageLoader,
)
from markdown2 import markdown

with open("./components/turkish-pide.md", "r") as f:
    parsed_md = markdown(f.read(), extras=["metadata"])

    env = Environment(
        loader=PackageLoader(
            "ssg",
            "./templates",
        )
    )
    test_template = env.get_template("test.html")


data = {
    "content": parsed_md,
    "title": parsed_md.metadata["title"],
    "date": parsed_md.metadata["date"],
}

print(test_template.render(post=data))
