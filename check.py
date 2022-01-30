# import gzip
# import shutil
# with gzip.open('chat.png', 'rb') as f_in:
#     with open('chats.png', 'wb') as f_out:
#         shutil.copyfileobj(f_in, f_out)

import mimetypes
mime = mimetypes.guess_type("text2.txt")[0].split("/")[0]
print(mime)