import sys
import getopt
import json
import os
import requests
import re

output_dir='images'

def download(url: str, dest_folder: str):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)  # create folder if it does not exist

    r = requests.get(url, stream=True)
     
    if r.ok:
        filename = get_filename_from_cd(r.headers.get('content-disposition'))
        file_path = os.path.join(dest_folder, filename)
        print("saving to", os.path.abspath(file_path))
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
    else:  # HTTP status code 4XX/5XX
        print("Download failed: status code {}\n{}".format(r.status_code, r.text))

def get_filename_from_cd(cd):
    """
    Get filename from content-disposition
    """
    if not cd:
        return None
    fname = re.findall('filename=(.+)', cd)
    if len(fname) == 0:
        return None
    return fname[0]

def main(argv):
    inputFile = ''
    opts, args = getopt.getopt(argv,"hi:",["inputFile="])
    for opt, arg in opts:
      if opt == '-h':
         print ('saveImages.py -i <inputFile>')
         sys.exit()
      elif opt in ("-i", "--input"):
         inputFile = arg

  
    if (inputFile):
        print ('Input file is ', inputFile)
        f = open(inputFile)
        data = json.load(f)

        for entry in data["log"]["entries"]:
            try:
                url = entry["request"]["url"]
                print("Downloading image: " + url) 
                print("")
                download(url, dest_folder=output_dir)
            except:
                continue

        for filename in os.listdir(output_dir):
            f = os.path.join(output_dir, filename)
            if os.path.isfile(f):
                base = os.path.splitext(f)[0]
                os.rename(f, base + '.jpg')  
    else:
        print ('Input file is missing! Usage: python saveImages.py -i <filename>')
if __name__ == "__main__":
    main(sys.argv[1:])