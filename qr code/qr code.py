import qrcode as qr
img = qr.make("https://www.youtube.com/@DrBro")
img.save("youtube_1.png")