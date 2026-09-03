import barcode 
from barcode.writer import ImageWriter

data = input("enter text or data : ").strip()

if not data :
    print("error : input cannot be empty!")
    exit()
try :
    code = barcode.get("code128" , data , writer = ImageWriter())
    filename = code.save("pycodify_barcode" ,

                        options = {
                            "module_width" : 0.3 ,
                            "module_height" : 15 ,
                            "font_size" : 10 ,
                            "text_distance" : 5 ,
                            "quite_zone" : 6
                        
                        })
    print("\n barcode generated successfully")
    print(f" saved as : {filename}.png ")

except Exception as e :
    print(f"error: {e}")