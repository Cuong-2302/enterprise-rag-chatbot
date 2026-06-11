from collections import defaultdict


def build_parent_map(chunks):

    parent_map = defaultdict(list)

    for chunk in chunks:

        parent_id = chunk.metadata.get(
            "parent_id"
        )

        parent_map[parent_id].append(
            chunk
        )

    return parent_map