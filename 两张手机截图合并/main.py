'''
Author：@caspiankexin
Language：python
Date：2022.3.1
'''

from gooey import Gooey, GooeyParser
from PIL import Image, ImageFont, ImageDraw # 导入模块

def merge_pictures(first_image, second_image, title):
    im = Image.open(first_image)
    x, y = im.size
    im = im.resize((260, int(260 / x * y)), Image.ANTIALIAS)  # 对图片的大小进行调整

    img = Image.open(second_image)
    x, y = img.size
    img = img.resize((260, int(260 / x * y)), Image.ANTIALIAS)  # 对图片的大小进行调整

    image = Image.new('RGB', (598, 842), "white")
    image.paste(im, (35, 170))
    image.paste(img, (310, 170))

    draw = ImageDraw.Draw(image)  # 修改图片
    font = ImageFont.truetype('C:\Windows\Fonts\simsun.ttc', size=60)
    draw.text((225, 50), title, fill=(150, 0, 0), font=font)  # 利用ImageDraw的内置函数，在图片上写入文字
    image.save(title + '合成后图片.jpg')
    print('all images are ok.')


@Gooey (program_name="手机截图合成工具V1.0版本", language='chinese')
def main():
    parser = GooeyParser(description="将健康码和行程码合并打印，手机截图合并。——@caspniankexin制作并免费分享")
    parser.add_argument('first_image', help="第一张图，可以直接拖拽到选择框中", widget="FileChooser")
    parser.add_argument('second_image', help="第二张图，可以直接拖拽到选择框中", widget="FileChooser")
    parser.add_argument('title', help="标题，姓名")
    args = parser.parse_args()
    merge_pictures(args.first_image, args.second_image, args.title)

main()