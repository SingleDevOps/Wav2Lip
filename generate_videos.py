import os
import subprocess

# Paths
audio_dir = "audio_files_new"
output_dir = "results3"
checkpoint_path = "checkpoints/Wav2Lip-SD-GAN.pt"

# Images
person1 = "recording.mp4"
person2 = "recording2.mp4"

# Create output directory if not exists
os.makedirs(output_dir, exist_ok=True)

# Loop over 1 to 50
for i in range(1, 51):
    audio_file = os.path.join(audio_dir, f"output_new_{i}.wav")
    image_file = person1 if i % 2 == 1 else person2
    output_file = os.path.join(output_dir, f"result_video_{i}.mp4")
    
    command = [
        "python", "inference.py",
        "--checkpoint_path", checkpoint_path,
        "--face", image_file,
        "--audio", audio_file,
        "--outfile", output_file,
    ]

    subprocess.run(command)