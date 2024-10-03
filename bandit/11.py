data = "Gur cnffjbeq vf 7k16JArUVv5LxVuJfsSVdbbtaHGlw9D4"

r = 13

rotated = []
for c in data:
    t = ord(c)
    if c.islower():
        t = (t + r - ord('a')) % 26 + ord('a')
    elif c.isupper():
        t = (t + r - ord('A')) % 26 + ord('A')
    print(f"{c} -> {chr(t)}")
    rotated.append(chr(t) if c.isalpha() else c)

print(''.join(rotated))
