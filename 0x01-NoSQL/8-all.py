#!/usr/bin/env python3
'''
Write a Python function that lists all documents in a collection:
'''
def list_all(mongo_collection):
    """Lists all docs"""
    documents = mongo_collection.find()
    return documents

