from backend.util.generate_hash import generate_hash


def hex_to_binary(hex_string):
    scale = 16

    res = format(int(hex_string, scale), '0256b')

    return res


def main():
    hex_num = hex(300)[2:]
    binary_num = hex_to_binary(hex_num)
    original_number = int(binary_num, 2)
    hex_to_binary_hash = hex_to_binary(generate_hash('data'))

    print(f'hex_number: {hex_num}')
    print(f'binary_number: {binary_num}')
    print(f'original_number: {original_number}')
    print(f'hex_to_binary_hash: {hex_to_binary_hash}')


if __name__ == '__main__':
    main()
