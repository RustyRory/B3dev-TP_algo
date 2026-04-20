s="abcabcbb"

def length_string(s):
    max_len = 0

    for i in range(len(s)):
        seen = set()

        for j in range(i, len(s)):
            if s[j] in seen:
                break
            seen.add(s[j])
            max_len = max(max_len, j - i + 1)

    
    return max_len

def exec_fcnt():
    s_input = input("Entrer une chaîne de caractères : ")
    return length_string(s_input)

print(exec_fcnt())