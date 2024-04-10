import qrcode

def criar_qr_code(texto):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(texto)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    return img

texto = input("Digite o texto para o QR Code: ")
qr_code = criar_qr_code(texto)
nome_arquivo = input("Digite o nome do arquivo de saída (sem extensão): ")
qr_code.save(f"{nome_arquivo}.png")

print("QR Code criado com sucesso!")
