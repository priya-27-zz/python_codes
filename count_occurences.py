from sys import stdin, stdout
from collections import Counter
raw_input()
cnt = Counter(stdin.readline().rstrip().split())
raw_input()
quers = stdin.read().splitlines()
rez = [str(cnt.get(i,'NOT PRESENT')) for i in quers]
stdout.write('\n'.join(rez))
