'''Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
'''
strs = ["act","pots","tops","cat","stop","hat"]

def find_grp_anagram(strs):
    hashmap ={}

    for i in strs:
        to_check = tuple(sorted(i))
        if to_check not in hashmap:
            hashmap[to_check]=[i]
        else:
            hashmap[to_check].append(i)
    return list(hashmap.values())

        #print(tuple(sorted(i)))
print(find_grp_anagram(strs))



