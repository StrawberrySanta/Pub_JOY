with open("text5.txt", "rb") as file:
    bytes_text = file.read()
bytes_text = list(bytes_text)

gamma = "seventythis"
bytes_gamma = gamma.encode('utf-8')
bytes_gamma = list(bytes_gamma)

shifr_bytes_text = []

len_bytes_text = len(bytes_text) 

for i in range(len_bytes_text):
    c = bytes_text[i] + (bytes_gamma[i] % 256)
    shifr_bytes_text.append(c)

bytes_text = []
for i in range(len_bytes_text):
    m = ((shifr_bytes_text[i] - bytes_gamma[i]) % 256)
    bytes_text.append(m)

text = bytes(bytes_text)

with open("text6.txt", "wb") as file:
    file.write(text)
    
file.close()

print(shifr_bytes_text)
print(bytes_text)
print(text)