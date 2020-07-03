from backend.util.hex_to_binary import hex_to_binary


def test_hex_to_binary():
    hex_num = hex(300)[2:]
    binary_num = hex_to_binary(hex_num)

    assert int(binary_num, 2) == 300
