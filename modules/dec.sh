echo "import os
import os.path
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util import Counter
import time
import marshal
time.clock = time.time
files=dir_f_list('$3')
kay='$1'" > $2
cat modules/decryption >> $2
