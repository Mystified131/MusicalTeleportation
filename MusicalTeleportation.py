import random

alist = ["https://archive.org/download/ThomasParkAudioFragments/1a.mp3", "https://archive.org/download/ThomasParkAudioFragments/1b.mp3", "https://archive.org/download/ThomasParkAudioFragments/1c.mp3", "https://archive.org/download/ThomasParkAudioFragments/1d.mp3", "https://archive.org/download/ThomasParkAudioFragments/1e.mp3"]
random.shuffle(alist)

outfile = open("musicwork.m3u", "w")
for ctr in range(len(alist)):
    wrtstr = alist[ctr]
    outfile.write(wrtstr + '\n')
outfile.close()

print("The musical piece, 'musicwork', has been created in your program's directory.")
print("If you click on it to open it, it should play in most media players.")
print("This musical piece may be 'teleported', or simultaneously shared, with as many people as you like, by sharing the .m3u.")
print("Recipients must play the .m3u without using shuffle.")
print("")
print("The notion is, large portions of data are indexed and composed at one end, then simply this composition is shared, rather than the audio data itself.")
print("The bulk of the data already exists and has been stored, either at a third-party location, or at each user's terminal.")





