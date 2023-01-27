max_line = 10
line = '*'
i=0;
while i < max_line:
    print(line)
    line += "*"
    i=i+1
i = max_line-1
while i >= 0:
    print(line);
    line = line[0:-1]ā
    i=i-1;
