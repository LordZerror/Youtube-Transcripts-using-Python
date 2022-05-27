from youtube_transcript_api import YouTubeTranscriptApi

srt = YouTubeTranscriptApi.get_transcript("M576WGiDBdQ", languages=['en'])
# print(len(srt))
with open("subtitles.txt", "w+") as f:
    for i in range(len(srt)):
        f.write("{}\n".format(srt[i]['text']))
        if i == len(srt) - 1:
            print('Successfully Created Subtitles File')

f.close()