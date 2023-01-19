import scrapy
import json

class VacancespiderSpider(scrapy.Spider):
    name = 'vacanceSpider'
    allowed_domains = ['www.vacances.com']
    start_urls = ['http://www.vacances.com/']
    nb_links = 0
    nb_zero = 0
    nb_un = 0
    nb_deux = 0
    nb_trois = 0
    nb_quatre = 0
    nb_cinq = 0
    nb_total = 0
    nb_inf_cinq = 0
    nb_300 = 0
    nb_dup = 0
    nb_non_dup = 0
    annonce_id = []
    # new_file = open('new_liste.txt', "w")
    data_file = open('data_file.txt', "w")
    final_file = open('file_18_11.txt', "w")
    extract_tab = open('extract_tab.txt', "w")
    def start_requests(self):
        file = open("liste_1.txt", "r")
        lines = file.readlines()
        print("=================", len(lines))
        file.close()
        for line in lines:
            yield scrapy.Request(url=line, callback=self.parse)
        print("******************************** self.nb_links: ", self.nb_links)
        print("******************************** 0: ", self.nb_zero)
        print("******************************** 1: ", self.nb_un)
        print("******************************** 2: ", self.nb_deux)
        print("******************************** 3: ", self.nb_trois)
        print("******************************** 4: ", self.nb_quatre)
        print("******************************** 5: ", self.nb_cinq)
        print("******************************** <5: ", self.nb_inf_cinq)
        print("******************************** 300: ", self.nb_300)
        print("******************************** Total: ", self.nb_total)
        print("******************************** Duplication: ", self.nb_dup)
        print("******************************** Non Duplication: ", self.nb_non_dup)
        print("******************************** annonce_id: ", len(self.annonce_id))
        try:
            self.data_file.write("***self.nb_links: "+str(self.nb_links)+"\n")
            self.data_file.write("***self.nb_zero: "+str(self.nb_zero)+"\n")
            self.data_file.write("***self.nb_un: "+str(self.nb_un)+"\n")
            self.data_file.write("***self.nb_deux: "+str(self.nb_deux)+"\n")
            self.data_file.write("***self.nb_trois: "+str(self.nb_trois)+"\n")
            self.data_file.write("***self.nb_quatre: "+str(self.nb_quatre)+"\n")
            self.data_file.write("***self.nb_cinq: "+str(self.nb_cinq)+"\n")
            self.data_file.write("***self.nb_inf_cinq: "+str(self.nb_inf_cinq)+"\n")
            self.data_file.write("***self.nb_300: "+str(self.nb_300)+"\n")
            self.data_file.write("***self.nb_total: "+str(self.nb_total)+"\n")
            self.data_file.write("***self.nb_dup: "+str(self.nb_dup)+"\n")
            self.data_file.write("***self.nb_non_dup: "+str(self.nb_non_dup)+"\n")
            self.data_file.write("***self.annonce_id: "+str(len(self.annonce_id))+"\n")
            self.data_file.write("---------------------------------------------------------------"+"\n")
        except:
            print("Error ...")
        # self.new_file.close()
        self.data_file.close()
        self.final_file.close()
        self.extract_tab.close()
        
        
    def parse(self, response):
        resp = json.loads(response.body)
        self.nb_links +=1
        offers = resp["offers"]
        l = len(offers)
        self.nb_total += l
        dup = False
        for d in offers:
            id = d["id"]
            if id in self.annonce_id:
                self.nb_dup += 1
                dup = True
            else:
                self.annonce_id.append(id)
                self.nb_non_dup += 1
                annonce_link = "https://www.vacances.com/rental/"+id
                self.extract_tab.write(annonce_link+"\n")
        if dup == False and l != 0:
            try:
                self.final_file.write(response.request.url+"\n")
            except:
                print("Error ...")
    # def parse(self, response):
    #     resp = json.loads(response.body)
    #     self.nb_links +=1
    #     offers = resp["offers"]
    #     l = len(offers)
    #     if l == 0:
    #         self.nb_zero += 1
    #     if l == 1:
    #         self.nb_un += 1
    #     if l == 2:
    #         self.nb_deux += 1
    #     if l == 3:
    #         self.nb_trois += 1
    #     if l == 4:
    #         self.nb_quatre += 1
    #     if l == 5:
    #         self.nb_cinq += 1
    #     if l == 300:
    #         self.nb_300 += 1
    #     if l <= 5 and l >=0:
    #         self.nb_inf_cinq +=1
    #     self.nb_total += l
    #     dup = False
    #     for d in offers:
    #         id = d["id"]
            # if id in self.annonce_id:
            #     self.nb_dup += 1
            #     dup = True
            # else:
            #     self.annonce_id.append(id)
    #             self.nb_non_dup += 1
        # if dup == False:
        #     try:
        #         self.final_file.write(response.request.url+"\n")
        #     except:
        #         print("Error ...")
    #     try:
    #         if l != 0:
    #             self.new_file.write(str(l)+" -- "+response.request.url+"\n")
    #     except:
    #         print("Error ...")
    # nb_total = 0
    # nb_links = 0
    # nb_zero = 0
    # new_file_none = open('liste_none.txt', "w")
    # new_file_ok = open('liste_ok.txt', "w")
    # def start_requests(self):
    #     file = open('liste.txt', "r")
    #     lines = file.readlines()
    #     file.close()
    #     for line in lines:
    #         yield scrapy.Request(url=line, callback=self.parse)
    #     print("******************************** len(lines): ", len(lines))
    #     print("******************************** self.nb_total: ", self.nb_total)
    #     print("******************************** self.nb_links: self.nb_links", self.nb_links)
    #     print("******************************** self.zero: ", self.nb_zero)
    #     self.new_file_none.close()
    #     self.new_file_ok.close()


    # def parse(self, response):
    #     resp = json.loads(response.body)
    #     total = resp["offers"]
    #     self.nb_total += len(total)
    #     self.nb_links += 1
    #     try:
    #         if len(total) == 0:
    #             self.nb_zero +=1   
    #             self.new_file_none.write(response.request.url+"\n")
    #         else:
    #             self.new_file_ok.write(str(len(total))+" -- "+response.request.url+"\n")
    #     except:
    #         pass
        
        
