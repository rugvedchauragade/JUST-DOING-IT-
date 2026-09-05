import qrcode

data = input("enter text or data : ")

qr = qrcode.make(data)
qr.save("qrcode.png")

print("QR code saved as 'qrcode.png'")