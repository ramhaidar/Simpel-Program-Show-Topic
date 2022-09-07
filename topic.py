#main program
#Value pada key 'Activities' berupa list berisi id_activity
list_topic = [{'Title': 'Dummy Topic 1', 'Description': 'Ini deskripsi topic 1', 'Activities':[0, 1]},
                    {'Title': 'Dummy Topic 2', 'Description': 'Ini deskripsi topic 2', 'Activities':[2]}
                  ]
# key pada dict_activity adalah id_activity 
dict_activity = {0: {'Title': 'Dummy Assignment 1', 'Type': 'assignment', 'Description': 'buatlah program Game'},
                         1: {'Title': 'Dummy material', 'Type': 'material', 'Description': 'slide minggu ini'},
                         2: {'Title': 'Dummy Assignment 2', 'Type': 'assignment', 'Description': 'buatlah program LMS'}
                         }

#fungsi
def show_topic(list_topic, dict_activity):
    '''
    Menampilkan setiap topik beserta detil aktifitasnya
    '''
    print('----Fungsi "show_topic" dijalankan----')
    #jawaban anda di bawah ini
    print("")
    for a in list_topic: #mengakses satu per satu list dictionary pada list topic
        desk = dict(a)#mengubah tipe list menjadi dictionary
        print("Title\t\t:", desk["Title"])#mengakses value pada key Title
        print("Description\t:", desk["Description"])#mengakses value pada key description
        print("List Activity\t:")
        print("ID\t| Title\t\t\t| Type\t\t| Description\t\t")#judul pada tabel
        print("-"*70)
        for n in desk["Activities"]:
            tabel = dict(dict_activity[n])
            print(n, "\t|", tabel["Title"], "\t|", tabel["Type"], "\t|", tabel["Description"])
        print("")
    
    try:
        a = (input("Tekan Enter untuk kembali ke menu utama...")=='')
        pass
    except Exception:
        pass
    

    
    
            
        
    


