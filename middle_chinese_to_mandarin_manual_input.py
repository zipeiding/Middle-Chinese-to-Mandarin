# Matches MC Initials to Mandarin Equivalent
match_initials = {
    1: "b",
    2: "p",
    3: "b",
    4: "m",
    5: "d",
    6: "t",
    7: "d",
    8: "n",
    9: "zh",
    10: "ch",
    11: "zh",
    12: "n",
    13: "z",
    14: "c",
    15: "z",
    16: "s",
    17: "s",
    18: "zh",
    19: "ch",
    20: "zh",
    21: "sh",
    22: "s",
    23: "zh",
    24: "ch",
    25: "sh",
    26: "sh",
    27: "sh",
    28: "g",
    29: "k",
    30: "g",
    31: "v",
    32: "h",
    33: "h",
    34: "v",
    35: "v",
    36: "v",
    37: "l",
    38: "r"
}

# Initials from Middle Chinese
middle_chinese_initials = {
    1: "p",
    2: "ph",
    3: "b",
    4: "m",
    5: "t",
    6: "th",
    7: "d",
    8: "n",
    9: "tr",
    10: "trh",
    11: "dr",
    12: "nr",
    13: "ts",
    14: "tsh",
    15: "dz",
    16: "s",
    17: "z",
    18: "tsr",
    19: "tsrh",
    20: "dzr",
    21: "sr",
    22: "zr",
    23: "tsy",
    24: "tsyh",
    25: "dzy",
    26: "sy",
    27: "zy",
    28: "k",
    29: "kh",
    30: "g",
    31: "ng",
    32: "x",
    33: "h",
    34: "ʔ",
    35: "h",
    36: "y",
    37: "l",
    38: "ny",
}

# Voiced Initials from MC
initial_voiced = {
    3: True,
    4: True,
    7: True,
    8: True,
    11: True,
    12: True,
    15: True,
    17: True,
    20: True,
    22: True,
    25: True,
    27: True,
    30: True,
    31: True,
    33: True,
    35: True,
    36: True,
    37: True,
    38: True,
}

voiced_obstruent_true = {
    3: True,
    7: True,
    11: True,
    15: True,
    17: True,
    20: True,
    22: True,
    25: True,
    27: True,
    30: True,
    33: True,
    35: True,
}

voiced_sonorant_true = {
    4: True,
    8: True,
    12: True,
    31: True,
    36: True,
    37: True,
    38: True,
}
# Matches MC Finals to Mandarin Equivalent
match_finals = {
    1: "ong",
    2: "ong",
    3: "u",
    4: "u",
    5: "ong",
    6: "u",
    7: "ong",
    8: "u",
    9: "uang",
    10: "uo",
    11: "i",
    12: "uei",
    13: "i",
    14: "uei",
    15: "i",
    16: "uei",
    17: "i",
    18: "uei",
    19: "i",
    20: "i",
    21: "uei",
    22: "ü",
    23: "u",
    24: "ü",
    25: "ai",
    26: "uei",
    27: "i",
    28: "uei",
    29: "ai",
    30: "uai",
    31: "ai",
    32: "uai",
    33: "ai",
    34: "uai",
    35: "i",
    36: "uei",
    37: "i",
    38: "uei",
    39: "i",
    40: "uei",
    41: "ai",
    42: "uei",
    43: "in",
    44: "in",
    45: "ün",
    46: "en",
    47: "uen",
    48: "i",
    49: "i",
    50: "ü",
    51: "e",
    52: "ü",
    53: "en",
    54: "e",
    55: "uen",
    56: "u",
    57: "in",
    58: "i",
    59: "uen",
    60: "u",
    61: "an",
    62: "uan",
    63: "a",
    64: "uo",
    65: "ian",
    66: "uan",
    67: "ie",
    68: "ua",
    69: "an",
    70: "uan",
    71: "a",
    72: "ua",
    73: "an",
    74: "uan",
    75: "a",
    76: "ua",
    77: "ian",
    78: "uan",
    79: "ian",
    80: "uan",
    81: "ie",
    82: "üe",
    83: "ie",
    84: "üe",
    85: "ian",
    86: "üan",
    87: "ie",
    88: "üe",
    89: "ao",
    90: "ao",
    91: "iao",
    92: "iao",
    93: "iao",
    94: "uo",
    95: "uo",
    96: "ie",
    97: "üe",
    98: "a",
    99: "ua",
    100: "ie",
    101: "ang",
    102: "uang",
    103: "uo",
    104: "uo",
    105: "iang",
    106: "uang",
    107: "üe",
    108: "üe",
    109: "eng",
    110: "uang",
    111: "ing",
    112: "iong",
    113: "e",
    114: "uo",
    115: "i",
    116: "uo",
    117: "eng",
    118: "ong",
    119: "e",
    120: "uo",
    121: "ing",
    122: "ing",
    123: "i",
    124: "i",
    125: "ing",
    126: "iong",
    127: "i",
    128: "ü",
    129: "eng",
    130: "ong",
    131: "e",
    132: "uo",
    133: "ing",
    134: "i",
    135: "ü",
    136: "iou",
    137: "ou",
    138: "iou",
    139: "in",
    140: "in",
    141: "i",
    142: "i",
    143: "an",
    144: "a",
    145: "ian",
    146: "an",
    147: "ie",
    148: "a",
    149: "an",
    150: "ia",
    151: "ian",
    152: "ia",
    153: "ian",
    154: "ian",
    155: "ie",
    156: "ie",
    157: "ian",
    158: "ie",
    159: "an",
    160: "a",
}

middle_chinese_finals = {
    1: "uwng",
    2: "juwng",
    3: "uwk",
    4: "juwk",
    5: "owng",
    6: "owk",
    7: "jowng",
    8: "jowk",
    9: "æwng",
    10: "æwk",
    11: "jie",
    12: "jwie",
    13: "je",
    14: "jwe",
    15: "jij",
    16: "jwij",
    17: "ij",
    18: "wi",
    19: "i",
    20: "jɨj",
    21: "jwɨj",
    22: "jo",
    23: "u",
    24: "ju",
    25: "aj",
    26: "waj",
    27: "joj",
    28: "jwoj",
    29: "æj",
    30: "wæj",
    31: "ɛɨ",
    32: "wɛɨ",
    33: "ɛj",
    34: "wɛj",
    35: "jiej",
    36: "jwiej",
    37: "jej",
    38: "jwej",
    39: "ej",
    40: "wej",
    41: "oj",
    42: "woj",
    43: "jin",
    44: "in",
    45: "win",
    46: "in",
    47: "jwin",
    48: "jit",
    49: "it",
    50: "wit",
    51: "it",
    52: "jwit",
    53: "on",
    54: "ot",
    55: "won",
    56: "wot",
    57: "jɨn",
    58: "jɨt",
    59: "jun",
    60: "jut",
    61: "an",
    62: "uan",
    63: "at",
    64: "wat",
    65: "jon",
    66: "jwon",
    67: "jot",
    68: "jwot",
    69: "æn",
    70: "wæn",
    71: "æt",
    72: "wæt",
    73: "ɛn",
    74: "wɛn",
    75: "ɛt",
    76: "wɛt",
    77: "jien",
    78: "jwien",
    79: "jen",
    80: "jwen",
    81: "jiet",
    82: "jwiet",
    83: "jet",
    84: "jwet",
    85: "en",
    86: "wen",
    87: "et",
    88: "wet",
    89: "aw",
    90: "æw",
    91: "jiew",
    92: "jew",
    93: "ew",
    94: "a",
    95: "wa",
    96: "ja",
    97: "jwa",
    98: "æ",
    99: "wæ",
    100: "jæ",
    101: "ang",
    102: "wang",
    103: "ak",
    104: "wak",
    105: "jang",
    106: "jwang",
    107: "jak",
    108: "jwak",
    109: "æng",
    110: "wæng",
    111: "jæng",
    112: "jwæng",
    113: "æk",
    114: "wæk",
    115: "jæk",
    116: "jwæk",
    117: "ɛng",
    118: "wɛng",
    119: "ɛk",
    120: "wɛk",
    121: "jieng",
    122: "jwieng",
    123: "jiek",
    124: "jwiek",
    125: "eng",
    126: "weng",
    127: "ek",
    128: "wek",
    129: "ong",
    130: "wong",
    131: "ok",
    132: "wok",
    133: "ing",
    134: "ik",
    135: "wik",
    136: "juw",
    137: "uw",
    138: "jiw",
    139: "jim",
    140: "im",
    141: "jip",
    142: "ip",
    143: "am",
    144: "ap",
    145: "jæm",
    146: "jom",
    147: "jæp",
    148: "jop",
    149: "æm",
    150: "æp",
    151: "ɛm",
    152: "ɛp",
    153: "jiem",
    154: "jem",
    155: "jiep",
    156: "jep",
    157: "em",
    158: "ep",
    159: "om",
    160: "op",
}

# Matches MC Tones to Mandarin Equivalent
match_tones = {
    1: "1",
    2: "3",
    3: "4",
    4: "v",
}

# MC Labial Initials
labial_true = {
    1: True,
    2: True,
    3: True,
    4: True,
}

# MC Nonsilibant Dental Initials
dental_nonsilibant_true = {
    5: True,
    6: True,
    7: True,
    8: True,
}

# MC Silibant Dental Initials
dental_silibant_true = {
   13: True,
   14: True,
   15: True,
   16: True,
   17: True, 
}

# MC Nonsilibant Retroflex Initials
retroflex_nonsilibant_true = {
    9: True,
    10: True,
    11: True,
}

# MC Silibant Retroflex Initials
retroflex_silibant_true = {
    18: True,
    19: True,
    20: True,
    21: True,
}

# MC Palatal Initials
palatal_true = {
    23: True,
    24: True,
    25: True,
    26: True,
    27: True,
    38: True,
}

# MC Velar and Glottal Initals
velar_true = {
    28: True,
    29: True,
    30: True,
    31: True,
    32: True,
    33: True,
    34: True,
    35: True,
    36: True,
}

# Labial Dictionaries
match_labial_finals = {
    "ong": "eng",
    "uang": "ang",
    "uo": "o",
    "uei": "ei",
    "uai": "ei",
    "uen": "en",
    "uan": "an",
    "uang": "ang",
    "e": "o",
    "ü": "u",
}

labialdentalization_obstruents_true = {
    2: True,
    4: True,
    7: True,
    8: True,
    21: True,
    24: True,
    28: True,
    59: True,
    60: True,
    66: True,
    68: True,
    106: True,
    136: True,
    146: True,
    148: True,
}

m_lenition_true = {
    2: True,
    4: True,
    7: True,
    8: True,
    21: True,
    24: True,
    28: True,
    59: True,
    60: True,
    66: True,
    68: True,
    106: True,
    146: True,
    148: True,   
}
# Velar and Silibant Dental Dictionaries
velar_special_finals = {
    2: "iong",
    4: "ü",
    7: "iong",
    8: "ü",
    9: "iang",
    10: "üe",
    47: "ün",
    59: "ün",
    60: "ü",
    63: "e",
    66: "üan",
    68: "üe",
    69: "ian",
    71: "ia",
    73: "ian",
    75: "ia",
    78: "üan",
    80: "üan",
    90: "iao",
    94: "e",
    98: "ia",
    103: "e",
    144: "e",
    160: "e",
}

velar_finals_palatalization_true = {
    2: True,
    4: True,
    7: True,
    8: True,
    9: True,
    10: True,
    11: True,
    13: True,
    15: True,
    17: True,
    19: True,
    20: True,
    35: True,
    37: True,
    39: True,
    43: True,
    44: True,
    45: True,
    47: True,
    48: True,
    49: True,
    50: True,
    52: True,
    57: True,
    58: True,
    59: True,
    60: True,
    65: True,
    66: True,
    67: True,
    68: True,
    69: True,
    71: True,
    73: True,
    75: True,
    77: True,
    78: True,
    79: True,
    80: True,
    81: True,
    82: True,
    83: True,
    84: True,
    85: True,
    86: True,
    87: True,
    88: True,
    90: True,
    91: True,
    92: True,
    93: True,
    96: True,
    97: True,
    98: True,
    100: True,
    105: True,
    107: True,
    108: True,
    111: True,
    112: True,
    115: True,
    121: True,
    122: True,
    123: True,
    125: True,
    126: True,
    127: True,
    128: True,
    133: True,
    134: True,
    135: True,
    136: True,
    138: True,
    139: True,
    140: True,
    141: True,
    142: True,
    145: True,
    147: True,
    149: True,
    150: True,
    151: True,
    152: True,
    153: True,
    154: True,
    155: True,
    156: True,
    157: True,
    158: True,
}

dental_silibant_special_finals = {
    47: "ün",
    78: "üan",
    80: "üan",
    133: "eng",
}

dental_silibant_finals_palatalization_true = {
    22: True,
    23: True,
    35: True,
    37: True,
    39: True,
    43: True,
    44: True,
    47: True,
    48: True,
    49: True,
    52: True,
    77: True,
    78: True,
    79: True,
    80: True,
    81: True,
    82: True,
    83: True,
    84: True,
    85: True,
    87: True,
    91: True,
    92: True,
    93: True,
    100: True,
    105: True,
    107: True,
    121: True,
    122: True,
    123: True,
    125: True,
    127: True,
    134: True,
    136: True,
    139: True,
    140: True,
    141: True,
    142: True,
    153: True,
    154: True,
    155: True,
    156: True,
    157: True,
    158: True,
}

dental_silibant_velar_initial_palatalization = {
    "z": "j",
    "c": "q",
    "s": "x",
    "g": "j",
    "k": "q",
    "h": "x",
}

# Retroflex and Palatal Dictionaries
palatal_retroflex_depalatalization = {
    "in": "en",
    "ian": "an",
    "ie": "e",
    "iao": "ao",
    "iang": "ang",
    "üe": "uo",
    "ing": "eng",
    "iou": "ou",
    "ia": "a",
    "ü": "u",
}

retroflex_special_finals = {
    52: "uai",
    99: "a",
    105: "uang",
    134: "e",
}

palatal_nasal_special_finals = {
    11: "er",
    13: "er",
    15: "er",
    17: "er",
    19: "er",
    141: "ru",
    142: "ru",
}

# Voiced Initial Dictionaries
voiced_initial_devoicing = {
    "b": "p",
    "d": "t",
    "g": "k",
    "z": "c",
    "zh": "ch",
    "sh": "ch",
}

# Pinyin Dictionaries
simplify_final = {
    "uen": "un",
    "uei": "ui",
    "iou": "iu",
}

simplify_results = {
    "i": "yi",
    "u": "wu",
    "ü": "yu",
    "ie": "ye",
    "ia": "ya",
    "iu": "you",
    "iao": "yao",
    "in": "yin",
    "ian": "yan",
    "ing": "ying",
    "iang": "yang",
    "uo": "wo",
    "ua": "wa",
    "ui": "wei",
    "uai": "wai",
    "un": "wen",
    "uan": "wan",
    "ong": "weng",
    "uang": "wang",
    "üe": "yue",
    "ün": "yun",
    "üan": "yuan",
    "iong": "yong",
    "jü": "ju",
    "qü": "qu",
    "xü": "xu",
    "jüe": "jue",
    "qüe": "que",
    "xüe": "xue",
    "jün": "jun",
    "qün": "qun",
    "xün": "xun",
    "jüan": "juan",
    "qüan": "quan",
    "xüan": "xuan",
}
# Main Script; Creates output
def main():
    # Matches the Initials Finals and Tone to get a first result
    initial = int(input("Input Initial "))
    final = int(input("Input Final "))
    tone = int(input("Input Tone "))
    initial_result = match_initials.get(initial)
    final_result = match_finals.get(final)
    tone_result = match_tones.get(tone)

    if initial_voiced.get(initial) == True:
        # Voiced Program
        if tone == 1:
            tone_result = "2"
            initial_result = voiced_initial_devoicing.get(initial_result, initial_result)
        if tone == 4:
            if voiced_obstruent_true.get(initial) == True:
                tone_result = "2"
            if voiced_sonorant_true.get(initial) == True:
                tone_result = "4"
        if tone == 2:
            if voiced_obstruent_true.get(initial) == True:
                tone_result = "4"

    if labial_true.get(initial) == True:
        # Labial Program
        final_result = match_labial_finals.get(final_result, final_result)
        if initial == 1 or initial == 2 or initial == 3:
            if labialdentalization_obstruents_true.get(final) == True:
                initial_result = "f"
        if initial == 4:
            if m_lenition_true.get(final) == True:
                initial_result = "w"
    elif dental_silibant_true.get(initial) == True:
        # Dental Silibant Program
        final_result = dental_silibant_special_finals.get(final, final_result)
        if dental_silibant_finals_palatalization_true.get(final, False):
            initial_result = dental_silibant_velar_initial_palatalization.get(initial_result, initial_result)
    elif velar_true.get(initial) == True:
        # Velar Program
        final_result = velar_special_finals.get(final, final_result)
        if velar_finals_palatalization_true.get(final, False):
            initial_result = dental_silibant_velar_initial_palatalization.get(initial_result, initial_result)
    elif retroflex_nonsilibant_true.get(initial) == True:
        # Retroflex Nonsilibant Program
        final_result = palatal_retroflex_depalatalization.get(final_result, final_result)
    elif palatal_true.get(initial) == True:
        # Palatal Program
        if initial == 38:
            final_result = palatal_nasal_special_finals.get(final)
            initial_result = "v"
            if final_result == None:
                final_result = match_finals.get(final)
                initial_result = match_initials.get(initial)
        final_result = palatal_retroflex_depalatalization.get(final_result, final_result)
    elif retroflex_silibant_true.get(initial) == True:
        # Retroflex Silibant Program
        final_result = palatal_retroflex_depalatalization.get(final_result, final_result)
        final_result = retroflex_special_finals.get(final, final_result)
    
    final_result = simplify_final.get(final_result, final_result)

    result = initial_result + final_result
    result = result.replace("v", "")

    result = simplify_results.get(result, result)
    result = result + tone_result
    result = result.replace("v", "")

    middle_chinese_initial = middle_chinese_initials.get(initial)
    middle_chinese_final = middle_chinese_finals.get(final)
    middle_chinese_tone = str(tone)

    if middle_chinese_tone == "4":
        middle_chinese_tone = ""
    elif middle_chinese_tone == "1":
        middle_chinese_tone = ""
    elif middle_chinese_tone == "2":
        middle_chinese_tone = "X"
    elif middle_chinese_tone == "3":
        middle_chinese_tone = "H"

    middle_chinese_result = middle_chinese_initial + middle_chinese_final + middle_chinese_tone

    print(middle_chinese_result)
    print(result)

main()