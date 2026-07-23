def format_result(neighbor, indent):
    # Example:
    #     - Last Attempt: 2026-07-15 15:53:19
    #     - Result: 8456 (0x2108)
    #     - Error: The source server is currently rejecting replication requests.

    content = []

    last_attempt = neighbor.get("last_attempt")
    result = neighbor.get("result")
    result_hex = neighbor.get("result_hex")
    error = neighbor.get("error")

    if last_attempt:
        content.append(f"{indent}- Last Attempt: {last_attempt}")

    if result is not None:
        result_text = str(result)

        if result_hex:
            result_text += f" ({result_hex})"

        content.append(f"{indent}- Result: {result_text}")

    if error:
        content.append(f"{indent}- Error: {error}")

    return content