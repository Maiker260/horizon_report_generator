from src.analysis.utils.rule_constructor import Rule

CUSTOMIZATION_RULES = [
    Rule(
        name="Horizon Connection server 2512 administrators may face issues managing vGPU-enabled desktop pools, such as editing automated IC/FC pools and adding NVIDIA vGPU-backed VMs to manual pools",
        is_version_specific= True,
        category="customization",
        match_type="contains",
        patterns=[
            "[ExceptionHandlerAdvice] max_number_of_monitors cannot be set if grid_vgpus_enabled is set to true"
        ],
        source_files=[
            r"debug-.*\.txt",
        ],
        recommendations=[],
        references=[
            "https://kb.omnissa.com/s/article/6001280",
        ]
    ),
]