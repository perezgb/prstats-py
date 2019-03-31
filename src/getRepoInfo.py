from github import Github
import os
import json

#using a token for connection
token = os.getenv('GITHUB_TOKEN')
gitAccess = Github(token)

repo = gitAccess.get_user().get_repo('prstats-py')
print(repo.name)

pr = repo.get_pull(2)
pr_out = {
  'id': pr.id,
  'number': pr.number,
  'title': pr.title,
  'state': pr.state,
  'user': {
    'id': pr.user.id,
    'login': pr.user.login
  }
}

print(pr_out)
# dump the pr data to json
with open('pr.json', 'w') as outfile:
  json.dump(pr_out, outfile)

# comments = pr.get_comments()
# for comment in comments:
#   print(comment.raw_data)