import qrcode
from tkinter import Tk, Label, Entry, Button
from PIL import Image, ImageTk
from tkinter import filedialog

# Função para criar o QR Code
def criar_qr_code():
    texto = entry_texto.get()  # Obtém o texto da entrada
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(texto)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save("qrcode.png")  # Salva a imagem do QR Code
    show_qr_code(img)

# Função para exibir o QR Code na interface
def show_qr_code(img):
    img = img.resize((150, 150))  # Redimensiona a imagem para se adequar à interface
    photo = ImageTk.PhotoImage(img)
    qr_label.imgtk = photo
    qr_label.configure(image=photo)
    qr_label.image = photo

# Configuração da janela da interface gráfica
root = Tk()
root.title("Gerador de QR Code")
root.geometry("300x300")  # Define o tamanho inicial da janela

# Campo de entrada de texto
Label(root, text="Digite o texto para o QR Code:").pack()
entry_texto = Entry(root)
entry_texto.pack()

# Botão para gerar o QR Code
Button(root, text="Gerar QR Code", command=criar_qr_code).pack()

# Label para exibir o QR Code
qr_label = Label(root)
qr_label.pack()

# Botão para salvar o QR Code
def salvar_qr_code():
    filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if filename:
        qr_label.image.save(filename)

Button(root, text="Salvar QR Code", command=salvar_qr_code).pack()

# Inicia o loop principal da interface gráfica
root.mainloop()
