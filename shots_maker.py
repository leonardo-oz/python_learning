import sys
import os

from PIL import Image
from pathlib import Path

if len(sys.argv) != 3:
  print("must have only prefix name, such as sleep or kungu")
  sys.exit()

dir_name = sys.argv[1]
dir_path = Path(dir_name)
image_path_list = sorted(list(dir_path.glob(f"*.jpg"))
                         ,key=lambda p: p.stat().st_ctime)
for path in image_path_list:
  print(path)
  



images = []
for path in image_path_list:
  image = Image.open(path).rotate(-90).reduce(4)
  if image is None:
    print(f"{path} does not exist")
    sys.exit()
  images.append(image)
# end for

output_file_name = f"{dir_name}/{sys.argv[2]}"
print(f"output animation file is : {output_file_name}")

images[0].save(
  output_file_name,save_all=True, append_images=images[1:], duration=200, loop=0
)

# "kungfu_1.jpg kungfu_2.jpg kungfu_3.jpg kungfu_4.jpg kungfu_5.jpg kungfu_6.jpg kungfu_7.jpg"dir_name