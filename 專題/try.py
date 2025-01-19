import subprocess

def open_camera():
    command = "adb shell am start -a android.media.action.IMAGE_CAPTURE"
    subprocess.run(command, shell=True)

def collect_logs(output_file="device_log.txt"):
    command = f"adb logcat -d > {output_file}"
    subprocess.run(command, shell=True)
    print(f"Logs saved to {output_file}")

def screen_record(output_file="/sdcard/screen_record.mp4"):
    command = f"adb shell screenrecord {output_file}"
    print("Recording... Press Ctrl+C to stop.")
    try:
        subprocess.run(command, shell=True)
    except KeyboardInterrupt:
        print("Recording stopped.")
        print(f"Video saved to {output_file}")

def take_picture(output_file="/sdcard/photo.jpg"):
    command = "adb shell input keyevent 27" 
    subprocess.run(command, shell=True)
    print("Picture taken.")

    pull_command = f"adb pull {output_file} ./photo.jpg"
    subprocess.run(pull_command, shell=True)
    print(f"Photo saved to ./photo.jpg")

def main():
    while True:
        print("\nAndroid Controller")
        print("1. 開啟相機")
        print("2. 收集 Log")
        print("3. 螢幕錄影")
        print("4. 拍照")
        print("5. 離開")

        choice = input("選擇功能: ")
        if choice == "1":
            open_camera()
        elif choice == "2":
            collect_logs()
        elif choice == "3":
            screen_record()
        elif choice == "4":
            take_picture()
        elif choice == "5":
            print("退出程式")
            break
        else:
            print("無效選項，請重新選擇。")

if __name__ == "__main__":
    main()
