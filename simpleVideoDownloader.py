# FIRST INSTALL THE MODULE FOR YOU TUBE VIDEO DOWNLOADER IS 
# [PIP INSTALL  PYTUBE ]

 # then import the module  from pytube import  * -> this means all functions 
 
from pytube import *
import tkinter


# take the input from user which video you want to download 

enterTheVideoName  = input("Enter The YouTube Video Link You Want To download : ")

# After pass into YouTube Funtion 
# first YouTube link Store into variable for other Work 

videoDownloader = YouTube(enterTheVideoName)

#If You Want to show the Title Of Video 
# use the [TITLE keyword to show the title ]
print(videoDownloader.title)


# After that we need to get which type of formate of vidoe avlable and Quality 
# we use the function streams.all -> it will show the video into audio and video download link both 
streamsQuality =  videoDownloader.streams.all()

# After that we need to show into Screen 
# we also want the index  and store into array , list or tuple what type you want to like 

streamsQualityOption = list( enumerate(streamsQuality))

for i in streamsQualityOption:
    print(i)

# after print we want to show into screen so we take into form user 

streamsQualityOptionUserInput = int(input('Enter the Option : '))


# After show we need to tell the function or variable this quality we want to Download 

streamsQuality[streamsQualityOptionUserInput].download()

# AFTER DOWNLOAD WE WANT TO SHOW INTO SHOW MESSEGE  OF CONGRATS 

print("Thank You For Downloading")



