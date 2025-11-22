# In this file, I will try to use as many new text functions as I can to learn python

original_text: str = " 'That FROOT looks familiar' -Marina & The Diamonds "

upper_text: str = original_text.upper()
lower_text: str = original_text.lower()
strip_text: str = original_text.strip()
replace_text: str = original_text.replace("FROOT","BRAT").replace("Marina & The Diamonds","Charli xcx")
split_text = original_text.split()
join_text = " ".join(split_text)

full_text: str = f"""
original: {original_text}
upper: {upper_text}
lower: {lower_text}
strip: {strip_text}
replace: {replace_text}
split: {split_text}
join: {join_text}
"""

print(full_text)