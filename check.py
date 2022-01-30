import gzip
import shutil
with gzip.open('chat.png', 'rb') as f_in:
    with open('chats.png', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)