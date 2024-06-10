import hashlib
from tkinter import Tk, Label, Button, Text, Scrollbar, filedialog, END, VERTICAL

def get_file_hash(file_path, hash_algo='sha256'):
    """Compute the hash of the given file using the specified hashing algorithm."""
    hash_function = hashlib.new(hash_algo)
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash_function.update(chunk)
    return hash_function.hexdigest()

def browse_file():
    """Open a file dialog to select a .pcap file and display its hash."""
    file_path = filedialog.askopenfilename(filetypes=[("PCAP files", "*.pcap")])
    if file_path:
        file_hash = get_file_hash(file_path)
        hash_textbox.config(state='normal')
        hash_textbox.delete(1.0, END)
        hash_textbox.insert(END, file_hash)
        hash_textbox.config(state='disabled')

def main():
    global hash_textbox

    # Create the Tkinter window
    root = Tk()
    root.title("PCAP File Hash Calculator")
    
    # Create and place the widgets
    Label(root, text="Select a .pcap file to calculate its hash:").pack(pady=10)
    
    browse_button = Button(root, text="Browse", command=browse_file)
    browse_button.pack(pady=5)
    
    hash_textbox = Text(root, height=4, width=64, wrap='none', state='disabled')
    hash_textbox.pack(pady=10)
    
    scrollbar = Scrollbar(root, orient=VERTICAL, command=hash_textbox.yview)
    hash_textbox.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side='right', fill='y')
    
    root.mainloop()

if __name__ == "__main__":
    main()
