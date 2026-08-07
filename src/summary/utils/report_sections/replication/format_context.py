from .format_single_neighbor import format_single_neighbor
from .format_multiple_neighbors import format_multiple_neighbors

def format_context(naming_context, neighbors, naming_context_max_width, sub_content_indent):
    # Format one replication naming context.

    # The output format changes depending on whether
    # there is one or multiple replication neighbors.

    if not neighbors:
        return []

    if len(neighbors) == 1:
        return format_single_neighbor(naming_context, neighbors[0], naming_context_max_width, sub_content_indent)

    return format_multiple_neighbors(naming_context, neighbors, naming_context_max_width, sub_content_indent)