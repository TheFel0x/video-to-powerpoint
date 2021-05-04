import os
import cv2 # opencv-python
from pptx import Presentation # python-pptx
from pptx.util import Inches

def main():
    # TODO: take args
    input_file = './test.mp4'   # TODO: make it cross-platform / windows-friendly
    cache_dir = './cache'      # TODO: use actual temp directory
    output_dir = './export'    # TODO: don't do this
    
    # Clear cache
    print('# clearing cache')
    cached_files = os.listdir(cache_dir)
    for file in cached_files:
        os.remove(os.path.join(cache_dir,file))
        print(os.path.join(cache_dir,file)+" deleted")

    # Extract frames from video
    # TODO: option to lower resolution
    print('# extracting frames')
    vidcap = cv2.VideoCapture(input_file)
    success,image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite(os.path.join(cache_dir,'frame%09d.jpg' % count), image) # TODO: decide amount of leading zeros with file count 
        success,image = vidcap.read()
        if success:
            print("%09d"%count)
        count += 1
    print('Extracting frames done.')
    
    # Create PowerPoint
    print('# creating ppp')
    ppp = Presentation()
    layout = ppp.slide_layouts[0] 
    slide = ppp.slides.add_slide(layout)
    slide.shapes.title.text = 'It works!'
    slide.placeholders[1].text = 'https://github.com/thefel0x'

    # Add frames
    frames = os.listdir(cache_dir)
    frames.sort()

    for f in frames:
        print('adding '+f) # should add percentage
        slide = ppp.slides.add_slide(layout)
        slide.shapes.title.text = f
        # TODO: dimension calculations
        pic = slide.shapes.add_picture("./cache/"+f, 0, 0,width=Inches(9), height=Inches(5))
    ppp.save(os.path.join(output_dir,'output.pptx'))
    print('done. saved at:\n'+os.path.join(output_dir,'output.pptx'))




if __name__ == '__main__':
    main()
