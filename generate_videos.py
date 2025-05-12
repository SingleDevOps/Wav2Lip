import os
import subprocess

# Paths
audio_dir = "audio_files"
output_dir = "results2"
checkpoint_path = "checkpoints/Wav2Lip-SD-GAN.pt"

# Images
person1 = "person1.jpg"
person2 = "person2.jpg"

# Create output directory if not exists
os.makedirs(output_dir, exist_ok=True)

# Loop over 1 to 50
for i in range(1, 51):
    audio_file = os.path.join(audio_dir, f"output_{i}.wav")
    image_file = person1 if i % 2 == 1 else person2
    output_file = os.path.join(output_dir, f"result_{i}.mp4")
    
    command = [
        "python", "inference.py",
        "--checkpoint_path", checkpoint_path,
        "--face", image_file,
        "--audio", audio_file,
        "--outfile", output_file
    ]
    
    print(f"Processing output_{i}.wav with {'person1.jpg' if i % 2 == 1 else 'person2.jpg'}")
    subprocess.run(command)