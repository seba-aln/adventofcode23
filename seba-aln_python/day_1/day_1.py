import re


def text_to_int(text) -> int:
    result = text.replace('one', '1') \
        .replace('two', '2') \
        .replace('three', '3') \
        .replace('four', '4') \
        .replace('five', '5') \
        .replace('six', '6') \
        .replace('seven', '7') \
        .replace('eight', '8') \
        .replace('nine', '9')
    return int(result)


def solve(input_data, variant) -> str:
    result = 0
    for line in input_data:
        line = line.strip()
        if variant == 1:
            pat = r"([0-9])"
        else:
            pat = r"(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))"

        found = re.findall(pat, line)
        first = text_to_int(found[0])
        last = text_to_int(found[-1])

        result = result + (first * 10 + last)
    return result
