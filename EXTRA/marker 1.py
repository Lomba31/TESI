# Open the file and read the contents into a string
with open("marker.txt") as file:
  s = file.read().strip()

# Initialize a window of four characters
window = s[:4]

# Iterate through the input string, starting from the fifth character
for i in range(4, len(s)):
  # Check if all characters in the window are different
  if len(set(window)) == 4 and len(set(window)) == len(window):
    # If they are, print the index of the last character in the window and exit the loop
    print(i - 1)
    break
  # Shift the window to the right by one character
  window = window[1:] + s[i]
else:
  # If no marker is found, print -1
  print(-1)