#prints out for the user to see, and the users input the number they want.
print("what the width?")
width= int(input ())

print("what the height?")
height= int(input ())

print("what is the depth?")
depth= int(input ())

def volume(w,h,d):

    #muiltiple w,h,d.
    volume = w*h*d;
    print(volume);

volume(width,height,depth) #users number.
