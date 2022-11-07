from pytube import YouTube

x = input("Enter the link: ")
yt = YouTube(x)
print("Title: ", yt.title)
print("Number of views: ", yt.views)
min = yt.length / 60
sec = yt.length % 60
print("Length of video: ", min, 'min', sec, 's')
print("Downloading...")
ys = yt.streams.get_highest_resolution()
ys.download()
print("Downloaded")
