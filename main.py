import json
import requests

def RepositoryCommitNumbers(r,u):
    request = requests.get('https://api.github.com/repos/' +u+'/' + r + '/commits')
    request_text = request.text
    parsed = json.loads(request_text)
    number = len(parsed)
    return number

def RepositoryNames(u):
    all_repositories = []
    request = requests.get('https://api.github.com/users/' + u +'/repos')
    request_text = request.text
    parsed = json.loads(request_text)
    for repository in parsed:
        name = repository["name"]
        all_repositories.append(name)
    return all_repositories

if __name__ == "__main__":
    input = raw_input("Github Name- ")
    print "User: " + input
    repositories = RepositoryNames(input)
    for repository in repositories:
        number = RepositoryCommitNumbers(repository,input)
        n_string = str(number)
        print "Repo: " + repository + " Number of Commits: " + n_string