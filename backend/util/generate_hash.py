import hashlib


def generate_hash(*args):
    """
    :param args: Arguments used for generating hash
    :return: Return sha256 hash
    """
    list_args = []

    for arg in args:
        list_args.append(str(arg))

    string_args = ''.join(sorted(list_args))

    return hashlib.sha256(string_args.encode('utf-8')).hexdigest()
