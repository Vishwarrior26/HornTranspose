change = {'C': 'G', 'C#': 'G#', 'Db': 'Ab',
          'D': 'A', 'D#': 'Bb', 'Eb': 'Bb',
          'E': 'B', 'F': 'C', 'F#': 'C#',
          'Gb': 'Db', 'G': 'D', 'G#': 'D#',
          'Ab': 'Eb', 'Bb': 'F', 'B': 'F#'}
print("Enter the concert pitches")
str = input()
result = ""
for x in str.split(' '):
    result += change.get(x) + " "
print(result)
