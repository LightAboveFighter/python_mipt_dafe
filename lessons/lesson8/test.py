d = {"a": {"s": 12, "q": 13}, "aa": {"s": 122, "q": 5}}
del d["a"]
print(len(d))
print(d)
print(d["aa"]["s"] - d["aa"]["q"])