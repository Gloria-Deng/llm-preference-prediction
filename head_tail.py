"""Keep both ends of a long conversation before applying the prompt template."""


def keep_head_and_tail(token_ids, max_tokens=4096):
    """Return a list of at most max_tokens IDs, keeping the original order."""
    ids = list(token_ids)
    if len(ids) <= max_tokens:
        return ids

    tail = min(1200, max_tokens // 3)
    head = ids[:max_tokens - tail]
    return head + ids[-tail:] if tail else head


if __name__ == '__main__':
    tokens = list(range(1, 13))
    budget = 6
    print('Original: ', tokens)
    print('Head only:', tokens[:budget])
    print('Head+tail:', keep_head_and_tail(tokens, budget))
