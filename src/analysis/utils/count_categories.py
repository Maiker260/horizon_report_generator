def count_categories(data):
    categories = {}

    for finding in data:
        category = finding["category"]
        
        if category not in categories:
            categories[category] = 1
        else:
            categories[category] += 1

    return categories