import re
from collections import defaultdict
from pprint import pprint
import argparse


class AuthLogAnalyst: 
    user_attack = {}
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
    
    def get_attack_user_count(self,data = []):
        for user in data:
            if(user in self.user_attack):
               self.user_attack[user] +=1
            else:
              self.user_attack[user] = 1
        return self.user_attack
    def get_sorted_user_attack_count(self,limit=2,reverse=True):
        return sorted(self.user_attack.items(), key=lambda x: x[1], reverse=reverse)[:limit]

class Run:
   @staticmethod
   def main():
        authLogAnalyst = AuthLogAnalyst() 
        parent_parser = argparse.ArgumentParser(add_help=False)
        parent_parser.add_argument('--main')
        parent_parser.add_argument('--first_attack',type=str)
        parent_parser.add_argument('--last_attack',type=str)
        parent_parser.add_argument('--reversed_list_slice',action='store_true')
        parent_parser.add_argument('--sliced_list',action='store_true')
        parent_parser.add_argument('--search_filter',action='store_true')
        parent_parser.add_argument('--user',type=str)
        parent_parser.add_argument('--limit',type=int)
        args = parent_parser.parse_args()
        count = 1
        if args.main == "main":
            data = authLogAnalyst.get_auth_log_analyst()
            for ip, usernames in data:
              authLogAnalyst.get_attack_user_count(usernames)
            pprint(authLogAnalyst.user_attack,indent=5)
            pprint(authLogAnalyst.get_sorted_user_attack_count(limit=4,reverse=False),indent=5)
            pprint(authLogAnalyst.get_sorted_user_attack_count(limit=4,reverse=True),indent=5)
            authLogAnalyst.user_attack.clear()
        if args.first_attack == "first_attack":
            data = authLogAnalyst.get_sliced_list()[0]
            pprint(data)
        if args.last_attack == "last_attack":
            data = authLogAnalyst.get_reversed_list_slice()[0]
            pprint(data)
        if args.reversed_list_slice and (args.limit and args.limit > 0):
            data = authLogAnalyst.get_reversed_list_slice(limit=-args.limit)
            for ip, usernames in data:
                print(f"{count} - IP: {ip} -> Users: {', '.join(usernames)} ->  attack_count: {len(usernames)}" + "\n\n\n")
                count+=1
        if args.sliced_list and (args.limit and args.limit >0):
            data = authLogAnalyst.get_sliced_list(limit=args.limit)
            for ip, usernames in data:
               print(f"{count} - IP: {ip} -> Users: {', '.join(usernames)} ->  attack_count: {len(usernames)}" + "\n\n\n")
               count+=1
        if args.search_filter and (args.user and args.limit > 0 ):
            data = authLogAnalyst.get_sliced_list(limit=args.limit)
            for ip, usernames in data:
               print(f"{count} - IP: {ip} -> Users: {', '.join([search for search in usernames if search.startswith(args.user) ])} ->  attack_count: {len([search for search in usernames if search.startswith(args.user) ])}" + "\n\n\n")
               authLogAnalyst.get_attack_user_count([search for search in usernames if search.startswith(args.user)  ])
               count+=1
            pprint(authLogAnalyst.user_attack,indent=5)
            pprint(authLogAnalyst.get_sorted_user_attack_count(limit=4,reverse=False),indent=5)
            pprint(authLogAnalyst.get_sorted_user_attack_count(limit=4,reverse=True),indent=5)
            authLogAnalyst.user_attack.clear()
        
if(__name__ == "__main__"):
    Run.main()
       
