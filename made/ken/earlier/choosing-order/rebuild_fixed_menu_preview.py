from PIL import Image,ImageDraw,ImageFont
import numpy as np
from pathlib import Path
p=Path(__file__).resolve().parent
src=Image.open(p/'menu-original-sheet.png').convert('RGBA')
im=Image.open(p/'ken-choosing-order-sheet.png').convert('RGBA')
# One reusable artwork layer, taken from the first original menu.
prop=src.crop((137,247,180,338))
a=np.array(prop); rgb=a[:,:,:3].astype(float); sat=(rgb.max(2)-rgb.min(2))/np.maximum(rgb.max(2),1)
a[:,:,3]=np.where(sat>.38,255,0); prop=Image.fromarray(a)
prop.save(p/'ken-fixed-menu-art.png')
w,h=im.width/4,im.height/3
font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',16)
frames=[]
# Card-relative placements: only translation changes; the artwork is identical.
positions=[(137,247),(137,247),(137,247),(137,247),(137,247),(137,247),(137,247),(137,247),(137,247),(137,247),(137,247),(137,247)]
for i,(x,y) in enumerate(positions):
 cell=im.crop((round(i%4*w),round(i//4*h),round((i%4+1)*w),round((i//4+1)*h)))
 layer=Image.new('RGBA',cell.size);layer.alpha_composite(prop,(x,y))
 # Preserve fingers crossing the artwork by masking warm skin on the card.
 ar=np.array(cell); skin=(ar[:,:,0].astype(int)-ar[:,:,1].astype(int)>55)&(ar[:,:,1].astype(int)-ar[:,:,2].astype(int)>40)
 la=np.array(layer);la[skin,3]=0;cell=Image.alpha_composite(cell,Image.fromarray(la))
 cell=cell.resize((380,380),Image.Resampling.LANCZOS)
 bg=Image.new('RGB',(420,440),(25,29,38));bg.paste(cell,(20,15),cell)
 ImageDraw.Draw(bg).text((210,416),'KEN · CHOOSING AN ORDER',font=font,fill=(237,218,186),anchor='mm');frames.append(bg)
frames[0].save(p/'ken-choosing-order-fixed.gif',save_all=True,append_images=frames[1:],duration=[450,200,280,280,220,600,180,200,500,200,300,450],loop=0,disposal=2)
contact=Image.new('RGB',(420*3,440))
for j,k in enumerate([0,5,8]):contact.paste(frames[k],(420*j,0))
contact.save(p/'fixed-menu-check.png')
print(Image.open(p/'ken-choosing-order-fixed.gif').n_frames)
