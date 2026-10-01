import sys
import os
import argparse
from PIL import Image
from pathlib import Path

parser=argparse.ArgumentParser()
parser.add_argument("--input_dir",default="junk",help="where your input picture are")
parser.add_argument("--out",default="junk.gif",help="where your animation will be")
parser.add_argument("-R",default=0,help="rotation angle", type=int)
parser.add_argument("-S",default=1,help="reduce factor size", type=int)
parser.add_argument("-D",default=200,help="refresh interval",type=int)
parser.add_argument("-T",default="jpg", help="image file type")
args=parser.parse_args()



if len(sys.argv) < 2 :
  print("must have at least input file")
  sys.exit()

dir_name = args.input_dir
dir_path = Path(dir_name)
image_path_list = sorted(list(dir_path.glob(f"*.{args.T}"))
                         ,key=lambda p: p.stat().st_ctime)
for path in image_path_list:
  print(path)
  



images = []
for path in image_path_list:
  image = Image.open(path).rotate(args.R).reduce(args.S)
  if image is None:
    print(f"{path} does not exist")
    sys.exit()
  images.append(image)
# end for
if len(images)==0:
  print(f"no image found in {dir_path}")
  sys.exit(1)
output_file_name = f"{dir_name}/{args.out}"
print(f"output animation file is : {output_file_name}")

images[0].save(
  output_file_name,save_all=True, append_images=images[1:], duration=args.D, loop=0
)

# "kungfu_1.jpg kungfu_2.jpg kungfu_3.jpg kungfu_4.jpg kungfu_5.jpg kungfu_6.jpg kungfu_7.jpg"dir_name