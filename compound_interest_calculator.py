principle = 0
rate = 0
time = 0

while True:
  principle = float(input("Enter the principle: "))
  if principle < 0:
    print("Principle can't be less than zero.")
  else:
    break

while True:
  rate = float(input("Enter the interset rate: "))
  if rate < 0:
    print("Interest rate can't be less than zero.")
  else:
    break

while True:
  time = int(input("Enter the time in year/s: "))
  if time < 0:
    print("Time can" \
    "t be less than zero.")
  else:
    break

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")