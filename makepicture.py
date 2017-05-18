import Image

picture = []

im = Image.open("test.jpg").convert("L")

print im.format, im.size, im.mode

out = im.resize((64,64))

pix = out.load()

print pix[0,0]

for i in range(64):
	row = []
	for j in range(64):
		row.append(pix[i,j])
	picture.append(row)

print picture

out.save("test_scaled.jpg")