def resolve_files(zip_ctx, files):
    all_matched_files = []

    for filename in files:
        is_pattern = any(c in filename for c in "^$.*+?[](){}|\\")

        if is_pattern:
            all_matched_files.extend(zip_ctx.find_pattern(filename))
        elif zip_ctx.exists(filename):
            all_matched_files.append(filename)

    return all_matched_files