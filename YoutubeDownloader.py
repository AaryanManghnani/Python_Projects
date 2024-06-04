from pytube import YouTube

link = "https://www.youtube.com/watch?v=chdNKjwH0Wk"

yt = YouTube(link)
"""
for i in yt.streams:
    print(i,end="\n")
"""
yt_high = yt.streams.get_highest_resolution()

print("Downloading...")
yt_high.download('C:/Users/aarya/Downloads')
print("Download Completed!")
