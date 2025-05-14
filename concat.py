import subprocess

# Define input folder and output path
input_folder = "results3"
output_file = "results3/final_output.mp4"

# Create a text file with the list of videos
with open("file_list.txt", "w") as file:
    for i in range(1, 51):
        file.write(f"file '{input_folder}/result_video_{i}.mp4'\n")

# Construct the ffmpeg command to concatenate the videos
command = [
    "ffmpeg",
    "-f", "concat",  # Use concat demuxer
    "-safe", "0",    # Allow file paths
    "-i", "file_list.txt",  # Input file list
    "-c", "copy",    # Copy audio/video codecs without re-encoding
    "-y",            # Overwrite output file
    output_file      # Output file
]

# Run the ffmpeg command
print("Concatenating videos...")
subprocess.run(command)
print("Done! Output saved as final_output.mp4")
