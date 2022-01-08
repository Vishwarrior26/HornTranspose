change = {'C': 'G', 'C#': 'G#', 'Db': 'Ab',
          'D': 'A', 'D#': 'Bb', 'Eb': 'Bb',
          'E': 'B', 'F': 'C', 'F#': 'C#',
          'Gb': 'Db', 'G': 'D', 'G#': 'D#',
          'Ab': 'Eb', 'Bb': 'F', 'B': 'F#'}
# str = "E E F# G C B"
print("Enter the concert pitches")
str = input()
for x in str.split(' '):
    print(change.get(x))
