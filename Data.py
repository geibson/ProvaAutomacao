import datetime

def periodo()
    now = datetime.datetime.now()
    file.write(str(now.day)+"/")
    file.write(str(now.month)+"/")
    file.write(str(now.year))
    file.write("\n")
    file.write(str(now.hour)+":")
    file.write(str(now.minute)+":")
    file.write(str(now.second))
    
