import re
from collections import defaultdict

class AuthLogAnalyst: 
   
    def __init__(self) -> None:
       pass

    def readLogfile(self,logFile="auth.log"):
        with open(logFile,'r') as file:
            files = file.read()
        return files
    

    def getLogAuthAnalyst(self):
        count = 1
        logFile = self.readLogfile()
        data = re.findall(r'Failed password for invalid user (.*?) from (.*?) ',logFile)
        grouped_data = defaultdict(list)
        for username, ip in data:
            grouped_data[ip].append(username)
        for ip, usernames in grouped_data.items():
            print(f"{count} - IP: {ip} -> Users: {', '.join(usernames)} ->  attack_count: {len(usernames)}" + "\n\n\n")
            count+=1

if(__name__ == "__main__"):
    authLogAnalyst = AuthLogAnalyst()
    authLogAnalyst.getLogAuthAnalyst()
