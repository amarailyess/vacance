type_heber = ['holiday_house','farm',
'camping_suite','hotel',
'pension','other_accommodation',
'holiday_apartment','castle','holiday_park',
'bed_and_breakfast','dedicated_room']

regions = ['5460aeb1b0bf2','5460aead9281b','5460aeb1b1c1f']

min_price = 9
max_price = 1500



def make_links():
    file = open('liste.txt', "w")
    print("scripted started ... ",end='')
    for region in regions:
        for type in type_heber:
            for p in range(min_price, max_price+1):
                try:
                    link = "https://www.vacances.com/search/"+region+"?maxPricePerNight="+str(p+1)+"EUR&minPricePerNight="+str(p)+"EUR&type%5B0%5D="+type+"&_format=json"
                    file.write(link+"\n")
                except:
                    print("ERROR WRITE FILE")
            print("=",end='')
    print(">  ",end='')
    print("** script finished ****")
    file.close()

def make_new_links():
    file_1 = open('liste_1.txt', "w")
    print("scripted started ... ",end='')
    for region in regions:
        for type in type_heber:
            for i in range(1,11):
                for p in range(10,200,1):
                    for j in range(1,6):
                        url = "https://www.vacances.com/search/"+region+"?_format=json&bedrooms="+str(i)+"&type="+type+"&page="+str(j)+"&maxPricePerNight="+str(p+5)+"EUR&minPricePerNight="+str(p)+"EUR"
                        file_1.write(url+"\n")
                for p in range(200,1001,5):
                    for j in range(1,6):
                        url = "https://www.vacances.com/search/"+region+"?_format=json&bedrooms="+str(i)+"&type="+type+"&page="+str(j)+"&maxPricePerNight="+str(p+5)+"EUR&minPricePerNight="+str(p)+"EUR"
                        file_1.write(url+"\n")
            print("=",end='')
    print(">  ",end='')
    print("** script finished ****")
    file_1.close()

if __name__ == '__main__':
    # make_links()
    make_new_links()
    file1 = open("liste_1.txt", "r")
    lines = file1.readlines()
    print("=================", len(lines))
    file1.close()
