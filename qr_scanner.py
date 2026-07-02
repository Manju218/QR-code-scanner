"""
QR Code & Barcode Scanner
----------------------------
Detects and decodes QR codes in real time using your webcam,
drawing a box around each code and displaying its content live.

Usage:
    python qr_scanner.py

Controls:
    'q' -> quit

Author: YourName
"""

import cv2

def main():
    cap = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()

    print("Show a QR code to the webcam. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        data, points, _ = detector.detectAndDecode(frame)

        if points is not None and data:
            points = points[0].astype(int)

            # Draw bounding box around the QR code
            for i in range(len(points)):
                pt1 = tuple(points[i])
                pt2 = tuple(points[(i + 1) % len(points)])
                cv2.line(frame, pt1, pt2, (0, 255, 0), 3)

            # Display decoded text above the box
            x, y = points[0]
            cv2.putText(frame, data, (x, y - 15),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            print("Decoded:", data)

        cv2.imshow("QR Code Scanner", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
