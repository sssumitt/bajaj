# app/services.py

from typing import List, Dict, Any

def process_array_data(data: List[Any]) -> Dict[str, Any]:
    odd_numbers = []
    even_numbers = []
    alphabets = []
    special_characters = []
    all_alphabetic_chars = []
    total_sum = 0

    for item in data:
        item_str = str(item)
        if item_str.isalpha():
            alphabets.append(item_str.upper())
            all_alphabetic_chars.extend(list(item_str))
        elif item_str.isdigit():
            num = int(item_str)
            total_sum += num
            (even_numbers if num % 2 == 0 else odd_numbers).append(item_str)
        else:
            special_characters.append(item_str)

    all_alphabetic_chars.reverse()
    concat_string = "".join(
        c.upper() if i % 2 == 0 else c.lower()
        for i, c in enumerate(all_alphabetic_chars)
    )

    return {
        "odd_numbers": odd_numbers,
        "even_numbers": even_numbers,
        "alphabets": alphabets,
        "special_characters": special_characters,
        "sum": str(total_sum),
        "concat_string": concat_string
    }