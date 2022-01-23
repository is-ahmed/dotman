from git.repo import Repo



def clone(url: str):

    Repo.clone_from(url, "~/") 


