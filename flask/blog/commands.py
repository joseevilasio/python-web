import click

from blog.posts import (
    get_all_posts,
    get_post_by_slug,
    new_post,
    update_post_by_slug,
    unpublish,
    delete
)


@click.group()
def post():
    """Manage posts"""


@post.command()
@click.option("--title")
@click.option("--content")
def new(title, content):
    """Creates a new post"""
    new = new_post(title=title, content=content)
    if new[0]:
        click.echo(f"New post {new[1]} created!")
    else:
        click.echo(f"New post {new[1]} FAIL! Post already exists")


@post.command("list")
def _list():
    """Lists all posts"""
    for post in get_all_posts():
        click.echo(post)


@post.command()
@click.argument("slug")
def get(slug):
    """Get post by slug"""
    post = get_post_by_slug(slug)
    click.echo(post or "post not found")


@post.command()
@click.argument("slug")
@click.option("--content", default=None, type=str)
@click.option("--published", default=None, type=str)
def update(slug, content, published):
    """Update post by slug"""
    data = {}
    if content is not None:
        data["content"] = content
    if published is not None:
        data["published"] = published.lower() == "true"
    if update_post_by_slug(slug, data)[0]:
        click.echo("Post updated")
    else:
        click.echo(f"Post updated FAIL!")


@post.command("unpublish_post")
@click.argument("slug")
def _unpublish(slug):
    """Unpublished on post by slug"""
    post = unpublish(slug)    
    click.echo(post or "post not found")


@post.command()
@click.argument("slug")
def delete_post(slug):
    """Delete on post by slug"""
    result = delete(slug)    
    click.echo(result or "post not found")


def configure(app):
    app.cli.add_command(post)
