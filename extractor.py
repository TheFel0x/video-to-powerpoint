# stole this code from the interwebs :^)
# should use tempfile or similar later
# maybe take args

import cv2
vidcap = cv2.VideoCapture('test.mp4')
success,image = vidcap.read()
count = 0
while success:
  #                           |  leading zeros are done a bit odd here maybe make nicer later
  #                           v                          (idk how tho.. lol)
  cv2.imwrite("./cache/frame%09d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1

# more stolen code :^)
# not needed rn at all but i might ujse smth like this later

# import tempfile

# print(tempfile.gettempdir()) # prints the current temporary directory

# f = tempfile.TemporaryFile()
# f.write('something on temporaryfile')
# f.seek(0) # return to beginning of file
# print(f.read()) # reads data back from the file
# f.close() # temporary file is automatically deleted here
