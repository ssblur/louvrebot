#!/usr/bin/env python

from dotenv import load_dotenv

load_dotenv()

from os import getenv
from sys import exit
from atproto import Client
from atproto_client.models.app.bsky.feed.search_posts import Params as SearchParams

username = getenv("BSKY_USER")
password = getenv("BSKY_PASS")

if username is None or password is None:
    print("Username and password must be set!")
    exit()

client = Client()
profile = client.login(username, password)

author_posts = client.get_author_feed(profile.did, include_pins=False, limit=1)

results = client.app.bsky.feed.search_posts(SearchParams(q="#TinyLouvre", since=author_posts.feed[0].post.indexed_at))
for post in results.posts:
    client.like(post.uri, post.cid)
    client.repost(post.uri, post.cid)