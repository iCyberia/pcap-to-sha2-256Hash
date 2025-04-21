# PCAP File Hash Calculator

A small Python GUI utility to compute the SHA‑256 hash of a `.pcap` packet‑capture file. Ideal for quickly verifying file integrity when handling network captures.

---

## Features

- **Browse & Hash**  
  Select any `.pcap` file via a standard file‑dialog and instantly compute its SHA‑256 checksum.  
- **Lightweight GUI**  
  Built with Tkinter—no extra dependencies beyond the Python standard library.  
- **Scroll‑aware Output**  
  The hash output is displayed in a read‑only, scrollable text box for easy copy/paste.

---

## Table of Contents

- [Requirements](#requirements)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Extending to Other Algorithms](#extending-to-other-algorithms)  
- [License](#license)  

---

## Requirements

- **Python 3.6+** (Tkinter comes bundled with standard installs)  
- No external packages

---

## Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/pcap-hash-calculator.git
   cd pcap-hash-calculator
   ```
2. (Optional) **Create & activate** a virtual environment  
   ```bash
   python3 -m venv venv
   source venv/bin/activate    # macOS/Linux
   venv\Scripts\activate     # Windows
   ```

---

## Usage

Run the main script:

```bash
python main.py
```

1. Click **Browse**.  
2. Select your `.pcap` file.  
3. The SHA‑256 checksum will appear in the text box—copy it as needed.

---

## Extending to Other Algorithms

By default, the tool uses SHA‑256. To support MD5, SHA‑1, or any algorithm available in `hashlib`, you can:

1. Edit the call in `browse_file()`:
   ```python
   file_hash = get_file_hash(file_path, hash_algo='md5')
   ```
2. Or modify the GUI to let users choose from `hashlib.algorithms_available`.

---

## License

© 2024 Hiroshi Thomas  
Released under the **GNU General Public License (GPL)**. See [LICENSE](LICENSE) for full terms.

