lines = []
with open('payload.py') as f:
    lines = f.readlines()
print(lines)
with open('payload_clone.py', 'w') as f:
    for line in lines:
        f.write(line)
    f.close()

exec(open("payload_clone.py").read())