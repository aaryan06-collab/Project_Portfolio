import os
import wikipedia as w
import gtts as g
import pyqrcode as q
import png
print('-----------------------------')
print('Welcome to Coding Bytes')
print('-----------------------------')
while True:
    print('1. Create text file')
    print('2. Read text file')
    print('3. Append the text file')
    print('4. Display current location')
    print('5. Change current location')
    print('6. Change the file name')
    print('7. To get the files and folder at current location')
    print('8. Folder create')
    print('9. Folder delete')
    print('10. File delete')
    print('11. Convert the text file into audio files')
    print('12. Extracting data from the wikipedia to a file')
    print('13. To create a qr code for a link')
    print('14. Exit')
    ch = int(input('enter the choice :'))
    if ch==1:
        a = input('enter your file name :')
        with open(a+'.txt','w') as f:
            s1 = input('enter the string into file :')
            f.write(s1)
        print('File created')
    elif ch==2:
        a = input('enter your file name :')
        with open(a+'.txt','r') as f:
            r = f.read()
            if f.tell()==0:
                print('file is empty...')
            else:
                print(r)
    elif ch==3:
        a = input('enter your file name :')
        with open(a+'.txt','a') as f:
            s1 = input('enter the string into file :')
            f.write(s1)
            f.write(' ')
        print('File appended')
    elif ch==4:
        print('Current location =',os.getcwd())
    elif ch==5:
        chloc=input('enter the new location =')
        os.chdir(chloc)
        print('Changed location successfully...!')
    elif ch==6:
        l = os.listdir()
        print('All files and directies :',l)
        old_name = input('enter the old files name :')
        new_name = input('enter the new file name :')
        os.rename(old_name,new_name)
        print('file named changed')
    elif ch==7:
        l = os.listdir()
        print('All files and directies :',l)
    elif ch==8:
        d = input('enter a directory name :')
        l = os.mkdir(d)
        print('directory created successfully...')
    elif ch==9:
        d = input('enter a directory name :')
        if os.path.isdir(d):
            l = os.rmdir(d)
            print('directory removed successfully...')
        else:
            print('directory does not exist..')
    elif ch==10:
        d = input('enter a file name(with extension of the file) :')
        if os.path.exists(d):
            l = os.remove(d)
            print('file removed successfully...')
        else:
            print('file does not exist..')
    elif ch==11:
        ab = input('enter your file name :')
        with open(ab+'.txt','r') as f:
            r = f.read()
        t = g.gTTS(text=r, lang='en')
        t.save('speech.mp3')
        os.system('speech.mp3')
        print('text is converted to speech successfully...')
    elif ch==12:
        d = input('enter the topic to find :')
        x = w.summary(d)
        a = input('enter your file name :')
        with open(a+'.txt','w') as f:
            f.write(x)
        print('content written...')
    elif ch==13:
        f = input('enter your link here :')
        g = q.create(f)
        g.png('your_qr.png',scale = 50)
    elif ch==14:
        break
    else:
        print('invalid choice...!')
        
