#!/usr/bin/env python3

import csv


def read_file(fn, k):
    with open(fn) as csvfile:
        reader = csv.DictReader(csvfile)
        data = [r for r in reader]

        def map_func(r):
            r["identifier"] = r[k]
            return r

        return list(map(map_func, data))


def development_policy_categories():
    cats = read_file(
        "data/development-policy-category.csv", "development-policy-category"
    )
    return {
        "list_name": "development policy categories",
        "field": "Category",
        "data": cats,
        "parent": {
            "name": "Development plans guidance",
            "href": "/guidance/development-plans-data",
        },
    }
