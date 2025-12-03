import useful
import re
from itertools import chain

print(sum(j for j in chain(*[range(*map(int, i.split('-'))) for i in useful.get_lines("2")[0].split(",")]) if re.match(r'^(\d+)\1+$', str(j))))
