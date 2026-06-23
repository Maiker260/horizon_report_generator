import ahocorasick

def build_automaton(rules):
    automaton = ahocorasick.Automaton()

    for rule in rules:
        if rule.match_type != "contains":
            continue

        for pattern in rule.lower_patterns:
            automaton.add_word(
                pattern,
                (rule, pattern)
            )

    automaton.make_automaton()

    return automaton