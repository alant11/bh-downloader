import sys
import getopt
import json
import os

output_dir='images'
curl_list = []

def main(argv):
    har_file = ''
    curl_file = ''

    try:
        opts, args = getopt.getopt(argv,"hf:c:",["help", "har=", "curl="])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == '-h':
            print ('generate_download_script.py -f <har> -c <curl>')
            sys.exit()
        elif opt in ("-f", "--har"):
            print("har")
            har_file = arg
        elif opt in ("-c", "--curl"):
            curl_file = arg

  
    if (har_file and curl_file):
        print ('HAR file is ', har_file)
        print ('CURL file is ', curl_file)

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)  # create folder if it does not exist
 
        f = open(curl_file)
        curl_str = f.read() 

        f = open(har_file)
        data = json.load(f)
        url_list = []

        for entry in data["log"]["entries"]:
            try:
                url = entry["request"]["url"]
                print("Adding image link: " + url) 
                url = url.replace("thumbnail=true&", "")
                url_list.append(url)   
                print("")

            except:
                continue

        curl_split = curl_str.split(' ', 2)
        curl_template = "curl '{image_link}' " + curl_split[2].strip() + " --output images/{num}.jpg"

        count = 1

        for url in url_list:
            curl_final = curl_template.format(image_link = url, num = count)
            curl_list.append(curl_final)
            print(curl_final)
            with open('download_script.sh', 'a') as f:
                f.write(curl_final)
                f.write("\n\n")
            count = count + 1
    else:
        if not har_file:
            print ("HAR file is missing! Usage: python generate_download_script.py -f <har_file> -c <curl_file>")
        elif not curl_file:
            print ("CURL file is missing! Usage: python generate_download_script.py -f <har_file> -c <curl_file>")
        else:
            print ("Usage: python generate_download_script.py -f <har_file> -c <curl_file>")

if __name__ == "__main__":
    main(sys.argv[1:])