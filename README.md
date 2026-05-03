# DroidScan

DroidScan is a lightweight and modular Android device diagnostic tool built with Python.  
It uses ADB and Fastboot to scan and display detailed device information.

## 🚀 Features

- Device Information (Model, Brand, Android Version, Codename)
- Bootloader Status (Unlocked, Secure, Product)
- Hardware Info (CPU, Memory, Battery)
- Partitions Listing
- Installed Apps (User & System)
- Sensors Information
- Network Details (WiFi, IP, Telephony)
- Security Status (SELinux, Encryption, Verified Boot)
- Logs (Logcat + Kernel)

## 🧰 Requirements

- Python 3.8+
- Android Platform Tools (ADB & Fastboot)

## 📁 Project Structure


adb_scanner/
├── platform-tools/
├── core/
├── scanners/
├── utils/
├── gui/
├── main.py
├── main_gui.py


## ▶️ Usage

### CLI Mode

python main.py


### GUI Mode

python main_gui.py


## ⚠️ Notes

- USB Debugging must be enabled
- Some features may require root access
- Fastboot features require bootloader mode

## 📦 Build Executable

Using PyInstaller:


pyinstaller --onefile main_gui.py


## 🛠️ Future Plans

- Modern GUI improvements
- Real-time monitoring (CPU, RAM, Logs)
- Multi-device support
- Plugin-based scanner system

## 📄 License

MIT License
