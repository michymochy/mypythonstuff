import filters
import classFilters

def main():
  # Ask what image the user wants to edit
    
   filename=input("Enter the name of the image file to edit:")

   # Load the image from the specified file

   img = filters.load_img(filename)

   newImage=classFilters.dogFilter(img)
    
   filters.save_img(newImage, "newImage.jpg")    
    
    


    
main()

