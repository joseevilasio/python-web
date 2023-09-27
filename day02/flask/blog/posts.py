from blog.database import mongo
from datetime import datetime
import pymongo
import unicodedata


def get_all_posts(published: bool = True):
    posts = mongo.db.posts.find({"published": published})
    return posts.sort("date", pymongo.DESCENDING)


def get_post_by_slug(slug: str) -> dict:
    post = mongo.db.posts.find_one({"slug": slug})
    return post


def update_post_by_slug(slug: str, data: dict) -> dict:
    
    if mongo.db.posts.find_one({"slug": slug}):
        raise FileExistsError("Post already exist")
    else:
        return mongo.db.posts.find_one_and_update({"slug": slug}, {"$set": data})


def new_post(title: str, content: str, published: bool = True) -> bool:

    text = "".join(c for c in unicodedata.normalize("NFD", title) if unicodedata.category(c) != "Mn")
    slug = text.replace(" ", "-").replace("_", "-").lower()
   
    if mongo.db.posts.find_one({"slug": slug}):
        raise FileExistsError("Post already exist")
    
    mongo.db.posts.insert_one(
        {
            "title": title,
            "content": content,
            "published": published,
            "slug": slug,
            "date": datetime.now(),
        }
    )
    return slug


def unpublish(slug: str) -> dict:
    return mongo.db.posts.find_one_and_update({"slug": slug}, {"$set": {"published": False}})


def delete(slug: str) -> str:
    if mongo.db.posts.delete_one({"slug": slug}):
        return f"Post {slug} deleted"
