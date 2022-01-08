change = {'C': 'G', 'C#': 'G#', 'Db': 'Ab',
          'D': 'A', 'D#': 'Bb', 'Eb': 'Bb',
          'E': 'B', 'F': 'C', 'F#': 'C#',
          'Gb': 'Db', 'G': 'D', 'G#': 'D#',
          'Ab': 'Eb', 'A': 'E', 'Bb': 'F',
          'B': 'F#'}
notes = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B']

# str = "A B D E E G E D A B D E E G E D A B D E E D B A A B D E E D B A A B A A B D E A B D E B D B A G D B D D G F# E D B E D B B A B D B E E D B D A B C D E C# A A B D B E F E D E A C# B A G G G G G G G G G G C B G C B C B G A F# E D D B D E D E E D B D B C C B G A F# E D D D B C B G G D C B C C B C B G G"

print("Enter the concert pitches")
str = input()

# result = ""
# for x in str.split(' '):
#     result += notes[notes.index(x) - 5] + " "
# print(result)

result = ""
for x in str.split(' '):
    result += change.get(x) + " "
print(result)
