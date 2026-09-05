"""Strict safe YAML decoding shared by the two package validators."""
from pathlib import Path
from typing import Any

import yaml


class UniqueKeyLoader(yaml.SafeLoader):
    """Reject ambiguous mappings instead of letting the last value win."""


def unique_mapping(loader: UniqueKeyLoader, node: yaml.MappingNode, deep: bool = False) -> dict:
    loader.flatten_mapping(node)
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        try:
            duplicate = key in result
        except TypeError as error:
            raise yaml.constructor.ConstructorError(None, None, 'mapping key must be hashable', key_node.start_mark) from error
        if duplicate:
            raise yaml.constructor.ConstructorError(None, None, f'duplicate mapping key: {key!r}', key_node.start_mark)
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def read_frontmatter(path: Path) -> dict[str, Any]:
    lines = path.read_text(encoding='utf-8').splitlines()
    if not lines or lines[0].strip() != '---':
        raise ValueError('missing opening YAML frontmatter delimiter')
    try:
        end = next(index for index, line in enumerate(lines[1:], 1) if line.strip() == '---')
    except StopIteration as error:
        raise ValueError('missing closing YAML frontmatter delimiter') from error
    value = yaml.load('\n'.join(lines[1:end]), Loader=UniqueKeyLoader)
    if not isinstance(value, dict):
        raise ValueError('frontmatter must be a YAML mapping')
    return value
