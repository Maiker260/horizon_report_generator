from dataclasses import dataclass, field

@dataclass
class Rule:
    name: str
    category: str
    patterns: list[str]
    
    source_files: list[str] = field(default_factory=list)

    recommendations: list[str] = field(default_factory=list)
    references: list[str] = field(default_factory=list)

    match_type: str = "regex"
    
    compiled_patterns: list = field(default_factory=list)
    lower_patterns: list[str] = field(default_factory=list)