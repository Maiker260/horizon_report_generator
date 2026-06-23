from src.analysis.rulesets.RULESETS import RULESETS
from src.analysis.utils.split_rules import split_rules
from src.analysis.utils.build_automaton import build_automaton

def build_engine(component):
    ruleset = RULESETS[component]
    contains_rules, regex_rules = split_rules(ruleset)
    automaton = build_automaton(contains_rules)

    return automaton, regex_rules