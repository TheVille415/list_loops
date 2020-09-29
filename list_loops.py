songs = ["ROCKSTAR", "Do It", "For The Night"]
print(songs[0])
print(songs[2])
print(songs[1:3])

songs[2] = "Beauty & Essex"
print(songs)
songs.extend(["Nasty", "Untitled (How Does It Feel)", "Amphetamine"])
songs.pop(1)

# Option 1
for song in songs:
    print(song)
# Option 2
for i in range(len(songs)):
    print(songs[i])

animals = ["pig", "chicken", "cow"]
animals.extend(["bat", "bear", "deer"])
print(animals[2])
del animals[0]

for i in range(len(animals)):
    print(animals[i])