import os
import subprocess

# Paths
audio_dir = "audio_files_new"
output_dir = "./"
checkpoint_path = "checkpoints/wav2lip.pth"

# Images
person1 = "man.jpg"
person2 = "woman.jpg"

# Create output directory if not exists
os.makedirs(output_dir, exist_ok=True)

audio_file = os.path.join(audio_dir, f"output_new_2.wav")
image_file = "recording2.mp4"
output_file = os.path.join(output_dir, f"result_2_video.mp4")

command = [
    "python", "inference.py",
    "--checkpoint_path", checkpoint_path,
    "--face", image_file,
    "--audio", audio_file,
    "--outfile", output_file,
]
    
subprocess.run(command)