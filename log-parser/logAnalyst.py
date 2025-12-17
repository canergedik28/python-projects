import re
from collections import defaultdict


class AuthLogAnalyst: 
    
    def __init__(self) -> None:
       pass
    
    def read_log_file(self,file_path="test.log"):
            with open(file_path,'r') as file:
                file = file.read()
            return file
    
    def get_auth_log_analyst(self):
        log_file = self.read_log_file()
        data = re.findall(r'Failed password for invalid user (.*?) from (.*?) ',log_file)
        grouped_data = defaultdict(list)
        for username, ip in data:
            grouped_data[ip].append(username)
        return grouped_data.items()
    
    def get_sliced_list(self,limit=20):
        data =  list(self.get_auth_log_analyst())[:limit]
        return data
    
    def get_reversed_list_slice(self,limit=-20):
        data =  list(self.get_auth_log_analyst())[limit:][::-1]
        return data

if(__name__ == "__main__"):
    authLogAnalyst = AuthLogAnalyst()
    control = 1
    while (control == 1  or control == 3) or control == 4:
      try: 
          count = 1
          choice = int(input("Bir secim yapiniz:"))
          if choice == 1:
            data = authLogAnalyst.get_auth_log_analyst()
            for ip, usernames in data:
              print(f"{count} - IP: {ip} -> Users: {', '.join(usernames)} ->  attack_count: {len(usernames)}" + "\n\n\n")
              count +=1
          elif choice == 2:
            limit = int(input("Bir limit giriniz: "))
            data = authLogAnalyst.get_sliced_list(limit=limit)
            for ip, usernames in data:
              print(f"{count} - IP: {ip} -> Users: {', '.join(usernames)} ->  attack_count: {len(usernames)}" + "\n\n\n")
              count +=1
          elif choice == 3:
            limit = int(input("Bir limit giriniz: "))
            data = authLogAnalyst.get_reversed_list_slice(limit=-limit)
            for ip, usernames in data:
              print(f"{count} - IP: {ip} -> Users: {', '.join(usernames)} ->  attack_count: {len(usernames)}" + "\n\n\n")
              count +=1
          elif choice == 4:
            text = str(input("Bir text giriniz: "))
            limit = int(input("Bir limit giriniz: "))
            data = authLogAnalyst.get_sliced_list(limit=limit)
            for ip, usernames in data:
               print(f"{count} - IP: {ip} -> Users: {', '.join([search for search in usernames if search.startswith(text) ])} ->  attack_count: {len([search for search in usernames if search.startswith(text) ])}" + "\n\n\n")
               count+=1
          else:
            control = 5
      except:
          control = 4

