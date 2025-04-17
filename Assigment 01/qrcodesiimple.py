import qrcode
import cv2

def generate_qr():
    data = input("Enter text or link: ")
    qr = qrcode.make(data)
    qr.save("my_qr.png")
    print("QR saved as 'my_qr.png'")

def scan_qr():
    image_name = input("Enter QR image name (e.g., my_qr.png): ")
    try:
        detector = cv2.QRCodeDetector()
        value, _, _ = detector.detectAndDecode(cv2.imread(image_name))
        print("Scanned data:", value if value else "No QR found")
    except:
        print("Error: File not found")

# Main Menu
while True:
    print("\n1. Generate QR\n2. Scan QR\n3. Exit")
    choice = input("Choose (1/2/3): ")
    if choice == "1":
        generate_qr()
    elif choice == "2":
        scan_qr()
    elif choice == "3":
        break
    else:
        print("Invalid choice")