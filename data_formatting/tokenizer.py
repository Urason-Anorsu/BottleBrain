import re
from typing import List

def basic_tokenize(text: str) -> List[str]:
    unclean_string = text
    
    clean_string = re.sub(r"[,\(\)\[\]\{\};:\"'`_+=!?*#@\\|-]","",unclean_string.lower())
    cleaner_string = re.sub(r"\s+", " ", clean_string).strip()
    tokenized_string = cleaner_string.split(" ")
    
    for character in range(len(tokenized_string) - 1, -1, -1):
        if tokenized_string[character] == "":
            del tokenized_string[character]

    return tokenized_string

def normalize_tokens(tokens: List[str]) -> List[str]:
    normalized = []
    for t in tokens:
        # 1. size normalization
        # 2. pack normalization
        # 3. junk filtering
        # 4. vendor abbreviation expansion (light)
        # 5. flavor/type prep
        normalized.append(t)
    return normalized


def normalize_size_step(tokens: List[str]) -> List[str]:
    ...

def normalize_pack_step(tokens: List[str]) -> List[str]:
    ...

def remove_junk_step(tokens: List[str]) -> List[str]:
    ...

def apply_vendor_abbrvs_step(tokens: List[str]) -> List[str]:
    ...

def prep_flavor_step(tokens: List[str]) -> List[str]:
    ...

def prep_type_step(tokens: List[str]) -> List[str]:
    ...