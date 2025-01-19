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
        print("1. Open Camera")
        print("2. Collect Logs")
        print("3. Screen Recording")
        print("4. Take Picture")
        print("5. Exit")

        choice = input("Select a function: ")
        if choice == "1":
            open_camera()
        elif choice == "2":
            collect_logs()
        elif choice == "3":
            screen_record()
        elif choice == "4":
            take_picture()
        elif choice == "5":
            print("Exiting program")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()