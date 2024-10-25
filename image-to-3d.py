from PIL import Image
import numpy as np
from skimage import measure
import trimesh
from datetime import datetime




#load image
image_path = R"C:\Users\goyok\Downloads\png-transparent-blue-snowflake-illustration-snowflake-snowflakes-file-winter-image-file-formats-text-thumbnail.png"

#image_path = r"{}".format(input("image full path here: ")) #windowsだとうまくいかないんだよなぁ

img = Image.open(image_path).convert('RGBA')  # RGBAで読み込み
img_array = np.array(img)

# アルファチャンネルを利用してマスクを生成（非透明部分のみ）
mask = img_array[:, :, 3] > 0  # アルファチャンネルが0より大きい（非透明）

# マスクを基に高さ方向に伸ばし、0〜1の範囲で正規化
height = 10  # height
height_map = np.zeros((mask.shape[0], mask.shape[1], height), dtype=np.float32)
for i in range(height):
    height_map[:, :, i] = mask * (i + 1) / height  # 高さに応じて正規化

# 3D
verts, faces, _, _ = measure.marching_cubes(height_map, level=0.5)  # levelを0.5に設定
mesh = trimesh.Trimesh(vertices=verts, faces=faces)


current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
output_stl = f"output_model_{current_time}.stl"

output_stl_path = R"C:\Users\goyok\Downloads\out-put.stl"+output_stl
# STLファイルとして保存
mesh.export(output_stl_path)
print(f"a STL file has been generated: {output_stl}")
