import subprocess as p

#insert text
#ffmpeg -i in.mp4 -vf drawtext="Sans.ttf: \text='Stack Overflow': fontcolor=white: fontsize=24: box=1: boxcolor=black@0.5: \boxborderw=5: x=(w-text_w)/2: y=(h-text_h)/2" -codec:a copy output.mp4

#insert image
#ffmpeg -i in.mp4 -i temp.jpg -filter_complex "[0:v][1:v] overlay=25:25:enable='between(t,0,20)'" -pix_fmt yuv420p -c:a copy out.mp4

def insertSpace(str):
	result = ""
	for s in str:
		result += s + " "
	return result

input1 = '-i in.mp4'
input2 = '-i temp.jpg'
output = '-c:a copy out.mp4'

#insert text
insertText  = '-vf drawtext=\"Sans.ttf: \\text=\'Stack Overflow\': fontcolor=white: fontsize=24: box=1: boxcolor=black@0.5: \\boxborderw=5: x=(w-text_w)/2: y=(h-text_h)/2\"'
p.call(insertSpace(["ffmpeg",input1,insertText,output]))

#insert image
insertImage = "-filter_complex \"[0:v][1:v] overlay=25:25:enable='between(t,0,20)'\" -pix_fmt yuv420p"
#p.call(insertSpace(["ffmpeg",input1,input2,insertImage,output]))
