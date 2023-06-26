import customtkinter as ctk

def convert_and_show_decimal():
    binario = entry_number.get()
    binario_sin_separadores = binario.replace(" ", "").replace("-", "")
    bit_length = len(binario_sin_separadores)

    decimal_sin_signo = int(binario_sin_separadores, 2)

    if binario_sin_separadores[0] == '1':
        binario_complemento = ''
        for bit in binario_sin_separadores:
            binario_complemento += '1' if bit=='0' else '0'  
        decimal_con_signo = -(int(binario_complemento, 2) + 1)  
    else:
        decimal_con_signo = decimal_sin_signo

    # Calcular rangos
    rango_sin_signo = (0, 2**bit_length - 1)
    rango_con_signo = (-2**(bit_length-1), 2**(bit_length-1) - 1)

    output_text.delete(1.0, 'end')
    output_text.insert(
        'end',
        f"El número binario es: {binario} \n"
        f"La longitud del número binario es de: {bit_length} bits\n"
        f"El número en decimal sin signo es: {decimal_sin_signo}\n"
        f"El número en decimal con signo (complemento a dos) es: {decimal_con_signo}\n"
        f"El rango de números para esta longitud de bits (sin signo) es: {rango_sin_signo}\n"
        f"El rango de números para esta longitud de bits (con signo) es: {rango_con_signo}\n"
    )


def convert_and_show_binary():
    number = int(entry_number.get())
    number_of_bits = int(entry_bits.get())

    if number < 0:
        if abs(number) > (1 << (number_of_bits - 1)):
            binary_formatted = hexadecimal_formatted = "*"*number_of_bits
        else:
            binary = format(number & ((1 << number_of_bits) - 1),
             f"0{number_of_bits}b")
            binary_formatted = " ".join([binary[i:i + 4] \
            for i in range(0, len(binary), 4)]) \
            if len(binary) % 4 == 0 \
            else binary[:len(binary)%4] + " " \
            + " ".join([binary[i:i + 4] \
            for i in range(len(binary)%4, len(binary), 4)])
            hexadecimal = format(number & ((1 << number_of_bits) - 1), "x").zfill(number_of_bits // 4)
            hexadecimal_formatted = " ".join([hexadecimal[i:i + 4] \
            for i in range(0, len(hexadecimal), 4)]) \
            if len(hexadecimal) % 4 == 0 \
            else hexadecimal[:len(hexadecimal)%4] + " " \
            + " ".join([hexadecimal[i:i + 4] \
            for i in range(len(hexadecimal)%4, len(hexadecimal), 4)])
    else:
        if number > ((1 << number_of_bits) - 1):
            binary_formatted = hexadecimal_formatted = "*"*number_of_bits
        else:
            binary = format(number, f"0{number_of_bits}b")
            binary_formatted = " ".join([binary[i:i + 4] \
            for i in range(0, len(binary), 4)]) \
            if len(binary) % 4 == 0 \
            else binary[:len(binary)%4] + " " \
            + " ".join([binary[i:i + 4] \
            for i in range(len(binary)%4, len(binary), 4)])
            hexadecimal = format(number, "x").zfill(number_of_bits // 4)
            hexadecimal_formatted = " ".join([hexadecimal[i:i + 4] \
            for i in range(0, len(hexadecimal), 4)]) \
            if len(hexadecimal) % 4 == 0 \
            else hexadecimal[:len(hexadecimal)%4] + " " \
            + " ".join([hexadecimal[i:i + 4] \
            for i in range(len(hexadecimal)%4, len(hexadecimal), 4)])

    output_text.delete(1.0, 'end')
    output_text.insert(
        'end',
        f"El número decimal es: {number} \n"
        f"El número en binario es: {binary_formatted}\n"
        f"El número en hexadecimal es: {hexadecimal_formatted}\n\n"
    )




ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
window_width = 800
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)

root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

my_font = ctk.CTkFont(family="Segoe UI", size=20)

entry_number = ctk.CTkEntry(root, font=my_font)
entry_number.pack(fill='both', expand=True, ipady=20)

entry_bits = ctk.CTkEntry(root, font=my_font)
entry_bits.pack(fill='both', ipady=20)

output_text = ctk.CTkTextbox(root, width=window_width-0.1*window_width,
                             height=window_height-0.5*window_height,
                             wrap='word', font=my_font)  
output_text.pack(fill='both', expand=True)


button_decimal = ctk.CTkButton(root, text="Bin a Decimal",
                       command=convert_and_show_decimal, font=my_font)
button_decimal.pack(fill='both', expand=True, ipady=20)  


button_bin = ctk.CTkButton(root, text="Decimal a Bin",
                       command=convert_and_show_binary, font=my_font)
button_bin.pack(fill='both', expand=True, ipady=20)  


root.mainloop()
