#!/usr/bin/env python

def insert_school(mongo_collection, **kwargs):
    """inserts a new document"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
