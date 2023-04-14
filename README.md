# bh-downloader

1. Log into BH from mybrightdayapp.brighthorizons.com . Do not go through BH Family Info Center or else it may not work.
2. In Firefox, open More Tools, Web Developer Tools
3. Go to Network tab
4. Can clear all unnecessary network requests that are scrolling by using the Trash button on the left until you are ready
5. When ready, click on Memories tab on the page (see example screenshot)
6. Keep scrolling down slowly through all the images and you should see the request URLs captured as you keep scrolling
7. Scroll all the way to the end (might take several minutes.....)
8. When done, click the settings icon on the lower right and Save All as HAR
9. Go to directory where you saved the HAR
10. Install python and pip if you haven't already
11. Install python requests package (pip install requests)
12. Create images folder  
    mkdir images
13. Run script current dir 
    python saveImages.py -i mybrightdayapp.brighthorizons.com_Archive [23-04-13 17-16-40].har 
14. Thumbnails should be in images folder
