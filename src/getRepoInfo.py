from github import Github
import os

#using a token for connection
token = os.getenv('GITHUB_TOKEN')

gitAccess = Github(token)

repo = gitAccess.get_user().get_repo('prstats-py')

print(repo.name)
print(dir(repo))