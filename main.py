change = {'C': 'G', 'C#': 'G#', 'Db': 'Ab',
          'D': 'A', 'D#': 'Bb', 'Eb': 'Bb',
          'E': 'B', 'F': 'C', 'F#': 'C#',
          'Gb': 'Db', 'G': 'D', 'G#': 'D#',
          'Ab': 'Eb', 'A': 'E', 'Bb': 'F',
          'B': 'F#'}

print("Enter the concert pitches")
str = input()
# str = "D E F E C F D E F E C A G D E F E C G F D F E D"
result = ""
for x in str.split(' '):
    result += change.get(x) + " "
print(result)
