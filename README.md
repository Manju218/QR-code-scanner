# 🔳 QR Code & Barcode Scanner

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.5+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A real-time QR code scanner that detects and decodes QR codes through your webcam, drawing a live bounding box and displaying the decoded content on screen.



## ✨ Features
- 📷 Real-time QR code detection and decoding via webcam
- 🟩 Live bounding box drawn around detected codes
- 🖥️ Decoded content displayed directly on the video feed
- ⚡ Uses OpenCV's built-in detector — no external libraries, no color tuning, works reliably in any lighting

## 🛠️ Tech Stack
- Python 3
- OpenCV (`opencv-python`)

## 📦 Installation
```bash
git clone https://github.com/yourusername/qr-code-scanner.git
cd qr-code-scanner
pip install -r requirements.txt
```

## 🚀 Usage
```bash
python qr_scanner.py
```
Hold any QR code up to your webcam — the content is decoded and displayed instantly, and also printed to the console.

Press `q` to quit.

## 🧠 How It Works
1. Capture live frames from the webcam
2. Use OpenCV's `cv2.QRCodeDetector` to detect and decode QR codes in each frame
3. Draw a bounding box around the detected code using the returned corner points
4. Overlay the decoded text on the video feed in real time

## 📂 Project Structure
```
qr-code-scanner/
├── qr_scanner.py
├── requirements.txt
└── README.md
```

## 🔮 Future Improvements
- [ ] Support for traditional barcodes using `pyzbar`
- [ ] Save scan history to a log file
- [ ] Auto-open URLs decoded from QR codes
- [ ] Batch scan from a folder of images

## 📄 License
This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## 🙋 Author
Built by [MANJU](https://github.com/Manju218)
