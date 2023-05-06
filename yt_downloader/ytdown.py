import os
import subprocess

def download_video(url, output_path="."):
    try:
        # Downloading the video
        print("Downloading video...")
        command = [
            "yt-dlp",
            url,
            "--output",
            os.path.join(output_path, "%(title)s.%(ext)s"),
        ]
        subprocess.run(command, check=True)
        print("Download completed!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    url = input("Enter the YouTube video URL: ")
    output_path = input("Enter the output directory path (default is current directory): ")

    if not output_path:
        output_path = "."

    download_video(url, output_path)
