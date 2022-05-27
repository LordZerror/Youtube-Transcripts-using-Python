from youtube_transcript_api import YouTubeTranscriptApi

url = input("Enter the URL of the youtube video: ").split('/')
# print(url[-1][8:])
try:
    srt = YouTubeTranscriptApi.get_transcript(url[-1][8:], languages=['en'])
    # print(len(srt))
    with open("subtitles.txt", "w+") as f:
        for i in range(len(srt)):
            f.write("{}\n".format(srt[i]['text']))
            if i == len(srt) - 1:
                print('Successfully Created Subtitles File')
    f.close()

except Exception as e:
    print('-'*90)
    print("An Exception Occurred : ")
    print(e)
