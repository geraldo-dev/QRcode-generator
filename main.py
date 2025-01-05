import qrcode

try:
    url = 'https://github.com/geraldo-dev'

    img = qrcode.make(url)
    img.save('qrcode.png')
except Exception as erro:
    print(erro)