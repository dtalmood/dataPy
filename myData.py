album_info = '''
Album name:The Wall
Artist name:Pink Floyd
Tracklist:
1 "In the Flesh?" Waters 3:16
2 "The Thin Ice" Waters, Gilmour 2:27
3 "Another Brick in the Wall, Part 1" Waters 3:11
4 "The Happiest Days of Our Lives" Waters 1:46
5 "Another Brick in the Wall, Part 2" Waters, Gilmour 3:59
6 "Mother" Waters, Gilmour 5:32
7 "Goodbye Blue Sky" Gilmour 2:45
8 "Empty Spaces" Waters	2:10
9 "Young Lust" Waters, Gilmour 3:25
10 "One of My Turns" Waters 3:41
11 "Don't Leave Me Now"	Waters	4:08
12 "Another Brick in the Wall, Part 3" Waters 1:18
13 "Goodbye Cruel World" Waters 1:16
14 "Hey You" Gilmour, Waters 4:40
15 "Is There Anybody Out There?" Waters, Gilmour 2:44
16 "Nobody Home" Waters 3:26
17 "Vera" Waters 1:35
18 "Bring the Boys Back Home" Waters 1:21
19 "Comfortably Numb" Gilmour, Waters 6:23
20 "The Show Must Go On" Gilmour 1:36
21 "In the Flesh" Waters 4:15
22 "Run Like Hell" Gilmour, Waters 4:20
23 "Waiting for the Worms" Waters, Gilmour 4:04
24 "Stop" Waters 0:30
25 "The Trial" Waters, Ezrin, Waters 5:13
26 "Outside the Wall" Waters 1:41
'''

#time in seconds
song_list = [
    (1, "In the Flesh?", 'Waters', 196, 'C:\\\\1.mp3'),
    (2, "The Thin Ice", 'Waters, Gilmour', 147, 'C:\\\\2.mp3'),
    (3, "Another Brick in the Wall, Part 1", 'Waters', 191, 'C:\\\\3.mp3'),
    (4, "The Happiest Days of Our Lives", 'Waters', 106, 'C:\\\\4.mp3'),
    (5, "Another Brick in the Wall, Part 2", 'Waters, Gilmour', 239, 'C:\\\\5.mp3'),
    (6, "Mother", 'Waters, Gilmour', 332, 'C:\\\\6.mp3'),
    (7, "Goodbye Blue Sky", 'Gilmour', 165, 'C:\\\\7.mp3'),
    (8, "Empty Spaces", 'Waters', 130, 'C:\\\\8.mp3'),
    (9, "Young Lust", 'Waters, Gilmour', 205, 'C:\\\\9.mp3'),
    (10, "One of My Turns", 'Waters', 221, 'C:\\\\10.mp3'),
    (11, "Don't Leave Me Now", 'Waters', 248, 'C:\\\\11.mp3'),
    (12, "Another Brick in the Wall, Part 3", 'Waters', 78, 'C:\\\\12.mp3'),
    (13, "Goodbye Cruel World", 'Waters', 76, 'C:\\\\13.mp3'),
    (14, "Hey You", 'Gilmour, Waters', 280, 'C:\\\\14.mp3'),
    (15, "Is There Anybody Out There?", 'Waters, Gilmour', 164, 'C:\\\\15.mp3'),
    (16, "Nobody Home", 'Waters', 206, 'C:\\\\16.mp3'),
    (17, "Vera", 'Waters', 95, 'C:\\\\17.mp3'),
    (18, "Bring the Boys Back Home", 'Waters', 81, 'C:\\\\18.mp3'),
    (19, "Comfortably Numb", 'Gilmour, Waters', 383, 'C:\\\\19.mp3'),
    (20, "The Show Must Go On", 'Gilmour', 96, 'C:\\\\20.mp3'),
    (21, "In the Flesh", 'Waters', 255, 'C:\\\\21.mp3'),
    (22, "Run Like Hell", 'Gilmour, Waters', 260, 'C:\\\\22.mp3'),
    (23, "Waiting for the Worms", 'Waters, Gilmour', 244, 'C:\\\\23.mp3'),
    (24, "Stop", 'Waters', 30, 'C:\\\\24.mp3'),
    (25, "The Trial", 'Waters, Ezrin, Waters', 313, 'C:\\\\25.mp3'),
    (26, "Outside the Wall", 'Waters', 101, 'C:\\\\26.mp3')
    ]

# add the lyrics later, figure out how to make it not look disgusting

class Song:
    def __init__(self):
        self.trackNumber = 0
        self.songName = ''
        self.vocals = ''
        self.songLength = 0
        self.filePath = ''

    #def __initSong__(self, name, length, newVocals, trackNum, path):
    #    self.trackNumber = trackNum
    #    self.songName = name
    #    self.vocals = newVocals
    #    self.songLength = length
    #    self.filePath = path

    def getTrackNum(self) -> int:
        return self.trackNumber

    def setTrackNum(self, newNum):
        self.trackNumber = newNum