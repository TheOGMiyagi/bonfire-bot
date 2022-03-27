"""Roll table logic for Sparks Of Memory.
"""
from random import choice

from src.rpg.roll_tables.variables import shards_of_memory_variables as _VARS


_SHARDS = { 'Anger' : _VARS.SHARDS_OF_ANGER,
    'Calm' : _VARS.SHARDS_OF_CALM,
    'Despair' : _VARS.SHARDS_OF_DEPAIR,
    'Fear' : _VARS.SHARDS_OF_FEAR,
    'Need' : _VARS.SHARDS_OF_NEED,
    'Regret' : _VARS.SHARDS_OF_REGRET,}

def rt_shard_of_memory(**kwargs):
    _return_type = kwargs.get('return_type', 'tuple')
    _emotion = choice(list(_SHARDS))
    _shard_text = choice(_SHARDS[_emotion])
    if _return_type == 'string':
        return f'{_emotion}\n{_shard_text}'
    elif _return_type == 'tuple':
        return _emotion, _shard_text


def main():
    for _ in range(10):
        _emotion, _shard_text = rt_shard_of_memory()
        print('\n\n', f'Shard Emotion: {_emotion}\n{_shard_text}')


if __name__ == '__main__':
    main()
