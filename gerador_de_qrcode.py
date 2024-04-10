import qrcode

# Função para criar o QR Code
def criar_qr_code(texto):
    # Cria um objeto QRCode com o texto fornecido
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(texto)
    qr.make(fit=True)

    # Cria uma imagem do código QR
    img = qr.make_image(fill='black', back_color='white')
    return img

# Obtém o texto do usuário
texto = input("Digite o texto para o QR Code: ")

# Cria o QR Code
qr_code = criar_qr_code(texto)

# Salva o QR Code como um arquivo PNG
nome_arquivo = input("Digite o nome do arquivo de saída (sem extensão): ")
qr_code.save(f"{nome_arquivo}.png")

print("QR Code criado com sucesso!")
