# Dotman


A seamless CLI tool for managing your dotfiles 

## Initial Approach



- Have a command to pull from GitHub repo (user provides link)
- Program iterates through repo and for any new config files, it
prompts user for abs path to place config file
- These locations get put into a separate config file so on next pull,
for already existing configs, it copies them to correct folders

- If user wants to sync, have a flag to reset any abs path
if they want to move the config files

- diff command to get paginated view of all modified config files

## Architecture

- dotman will have a main that will execute each time it's called where user can pass in arguments and specify any use flags
- dotman will then parse through all the all the different arguments and commands and call the different subsystems such as diff, sync
and set-repo



## How we'll handle configuration


- Have a config.json file that we'll store in some directory
- Will hold the currently set repo and absolute paths for
the different config files


## Set repo subsystem

- Flag for the cli that takes in a git repo url as an argument
- If the user changes the repo for their config files, then we prompt them 
for the absolute file paths


## Sync subsystem

- Sync config files on the local machine with git repo
- Automatically copy files to appropriate directories based on
file paths in config.json
- If the diff doesn't show any difference in any config files then 
we don't pull from the git repo
