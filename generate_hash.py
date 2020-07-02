import hashlib


def generate_hash(*args):
    """
    :param args: Arguments used for generating hash
    :return: Return sha256 hash
    """
    sorted_args = sorted(args)
    string_args = ''

    for arg in sorted_args:
        string_args += str(arg)

    return hashlib.sha256(string_args.encode('utf-8')).hexdigest()
