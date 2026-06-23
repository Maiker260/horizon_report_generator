def split_rules(ruleset):
    contains = []
    regex = []

    for r in ruleset:
        if r.match_type == "contains":
            contains.append(r)
        else:
            regex.append(r)

    return contains, regex