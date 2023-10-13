# change 1.3 TB to that counting by bytes

def num_length_info(length_info) -> int:
    multiplier = 1
    units = {"KB": 1024, "MB": 1024 ** 2, "GB": 1024 ** 3, "TB": 1024 ** 4, "B": 1}
    size = length_info.upper().strip()
    for unit, value in units.items():
        if size.endswith(unit):
            size = size[: -len(unit)].strip()
            multiplier = value
            break
    return int(float(size) * multiplier)
