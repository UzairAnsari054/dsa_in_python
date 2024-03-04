class Team:
    def __init__(self):
        self.memberList = []
    
    def inputMembers(self):
        memberCount = int(input("Enter number of team members: "))
        for i in range(memberCount):
            membername = input("Enter name: ")
            self.memberList.append(membername)
    
    def showAllMemberName(self):
        print("Team member:", self.memberList)



team = Team()
team.inputMembers()
team.showAllMemberName()