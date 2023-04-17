# bh-downloader

Downloader script for BH full size images.


Prerequisite:
Install python if you don't have it already



1. Download the file generate_download_script.py here to your local machine.

2. Log into BH from BH Family Info Center --> https://familyinfocenter.brighthorizons.com --> Login. After logging in, before clicking on anything else, go to the next step

3. In Firefox, open More Tools, Web Developer Tools

4. Go to Network tab (Can clear all unnecessary network requests that are scrolling by using the Trash button on the left until you are ready with next step)

5. Click on My Bright Day in the middle of the screen. Select your child.

6. The Photos tab of the timeline should be loaded, with the months displayed on the right.

7. You should see activity in the Network tab with request URLs captured for the loaded thumbnails

8. Click on the first thumbnail image which should pop up the original image

9. In the same Network tab, click on the last request which has "object_attachment?key=xxxxxx". [See pic attached]

10. Right click on this row and select Copy Value --> Copy as cURL

11. In your terminal, create a file and paste. 
    E.g. vi sample_curl.txt   <paste the curl command>
    
12. Now go back to the My Bright Day browser tab, and click on all the months on the right one by one, scrolling down to the end.

13. When done, click the settings icon on the lower right and Save All as HAR.  [See pic attached]

14. Go to directory where the HAR was saved - should be in your Downloads folder.

15. Move the HAR file to the same folder as the files from step 1.

16. Run script from current directory, passing in the HAR file and the CURL file saved. This will generate the script "download_script.sh"
    python3 generate_download_script.py -f familyinfocenter.brighthorizons.com_Archive\ \[23-04-17\ 13-13-05\].har -c sample_curl.txt
    
17. Allow executable permissions:
    chmod u+x download_script.sh

18. Run the download script. For 1400 photos this took 30 minutes. 
    ./download_script.sh 

19. Full size images should now be in the ./images folder
