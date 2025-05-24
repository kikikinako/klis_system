

# Example data
data = {"apple": ["a.txt", "b.txt"], 
        "banana": ["a.txt"], 
        "coconuts": ["c.txt"], 
        "durian": ["b.txt", "d.txt"], 
        "eggplant": ["c.txt", "d.txt", "e.txt"]}

# ソート未実装
def search(keywords, sort):
    keywords = keywords.split()
    result = []
    for keyword in keywords:
        if keyword in data:
            for file in data[keyword]:
                if file not in result:
                    result.append(file)
    return result