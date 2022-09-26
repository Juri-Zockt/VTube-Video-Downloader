from pytube import YouTube
import PySimpleGUI as sg
import os

sg.theme("DarkBrown4")

layout = [
	[sg.Text("Youtube Video Downloader")],
	[sg.Text("Enter your Youtube Link here: "), sg.InputText()],
	[sg.Text("Where should the file be saved: "), sg.FolderBrowse(key="-IN-")],
	[sg.Button("Enter!")]
]  

window = sg.Window("Youtube Video Downloader",  icon="Icon.ico", element_justification='c').Layout(layout)

while True:
	event, values = window.read()

	if event == sg.WIN_CLOSED:
		break
	elif event == "Enter!":
		yt = YouTube(values[0])
		file = yt.streams.get_highest_resolution()
		file.download(values["-IN-"])
		sg.Popup("Done!")
		window.close()

window.close()
