import json
from math import log
from string import punctuation
import timeit

start = timeit.default_timer()
dat = None
d = dict()
fil = punctuation + "\n\t "
N = 0

def get_weight(word, gram):
  try:
    ret = -log(d[word]/gram)
  except (ValueError, KeyError):
    ret = 100
  return ret

# lấy file data ở https://filedn.com/lit4DCIlHwxfS1gj9zcYuDJ/SNOW/VNTQcorpus-big.txt
with open("VNTQcorpus-big.txt", "r") as f:
  for line in f.readlines():
    print(f"Reading line no.{N:08d}", end="")
    print("\b"*(16+8), end='')
    line = line.strip(fil).split()
    N += len(line)
    for idx in range(len(line)):
      try:
        pre1 = line[idx-1].lower()
      except:
        pre1 = ""
      try:
        pre2 = line[idx-2].lower() + "_" + pre1
      except:
        pre2 = ""
      # try:
      #   pre3 = line[idx-3].lower() + "_" + pre2
      # except:
      #   pre3 = ""

      #1gram
      word = line[idx].lower()
      if (pre1 + "#" + word) in d:
        d[(pre1 + "#" + word)] += 1
      else:
        d[(pre1 + "#" + word)] = 0

      if (pre2 + "#" + word) in d:
        d[(pre2 + "#" + word)] += 1
      else:
        d[(pre2 + "#" + word)] = 0

      # if (pre3 + "#" + word) in d:
      #   d[(pre3 + "#" + word)] += 1
      # else:
      #   d[(pre3 + "#" + word)] = 0

      #2gram
      word += "_" + line[(idx+1)%len(line)].lower()
      if (pre1 + "#" + word) in d:
        d[(pre1 + "#" + word)] += 1
      else:
        d[(pre1 + "#" + word)] = 0

      if (pre2 + "#" + word) in d:
        d[(pre2 + "#" + word)] += 1
      else:
        d[(pre2 + "#" + word)] = 0

      # if (pre3 + "#" + word) in d:
      #   d[(pre3 + "#" + word)] += 1
      # else:
      #   d[(pre3 + "#" + word)] = 0

      #3gram
      # word += "_" + line[(idx+2)%len(line)].lower()
      # if (pre1 + "#" + word) in d:
      #   d[(pre1 + "#" + word)] += 1
      # else:
      #   d[(pre1 + "#" + word)] = 0

      # if (pre2 + "#" + word) in d:
      #   d[(pre2 + "#" + word)] += 1
      # else:
      #   d[(pre2 + "#" + word)] = 0

      # if (pre3 + "#" + word) in d:
      #   d[(pre3 + "#" + word)] += 1
      # else:
      #   d[(pre3 + "#" + word)] = 0
print()

stop = timeit.default_timer()

print("It took:", stop-start, "seconds")

with open("static", "w") as f:
  f.write(str(N))
  f.write("\n")
  f.write(json.dumps(d))

with open("static", "r") as f:
  dat = f.readlines()

N, d = dat
N = int(N)
d = json.loads(d)

while True:
  try:
    inp = input("prev: ")
    prev = "_".join([w.strip().lower() for w in inp.split()])
    inp = input("word: ")
    word = prev + "#" + "_".join([w.strip().lower() for w in inp.split()])
    print("w =", get_weight(word, N))
  except KeyboardInterrupt:
    print()
    print("Bye")
    break



