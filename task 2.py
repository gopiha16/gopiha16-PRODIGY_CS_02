from PIL import Image

def encrypt_image(input_path,output_path,key):
    img= Image.open (input_path)
    pixels = img.load()

    width , height =img.size

    for i in range(width):
        for j in range (height):
            r,g,b = pixels [i,j]

            encrypted_pixel= (b,g,r)
            pixels [i,j] = encrypted_pixel

    img.save(output_path)
    print ("Image encrypted successfully")

def decrypt_image(input_path,output_path,key):
    img = Image.open (input_path)
    pixels = img.load()

    width , height = img.size

    for i in range(width):
        for j in range (height):
            r,g,b= pixels [i,j]

            decrypted_pixel= (b,g,r)
            pixels [i,j] = decrypted_pixel

    img.save(output_path)
    print("Image decrypted successfully")


input_image = r"C:\Users\HARSHITHA R\desktop\Gopiha\input.jpeg"
encrypted_image = r"C:\Users\HARSHITHA R\desktop\Gopiha\encrypted.bmp"
decrypted_image = r"C:\Users\HARSHITHA R\desktop\Gopiha\decrypted.bmp"
encrypt_image(input_image,encrypted_image,key=None)
decrypt_image(encrypted_image,decrypted_image,key=None)

