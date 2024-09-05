# Task Tracker Project
Task tracker is a project used to track and manage your tasks. In this task, you will build a simple command line interface (CLI) to track what you need to do, what you have done, and what you are currently working on.

## Requirements:
- Python 3.x

## Installation:
    ```sh   
    git clone
    python3 -m venv env    
    source env/bin/activate
    cd task-tracker
    pip3 install -r requirements.txt
    ``` 
## Commands - CLI
### Add
    ```sh  
    python3 main.py add "New Description"
    ```
### List
    ```sh  
    python3 main.py list
    python3 main.py list [done|todo|in-progress]
    ```
### Update
    ```sh  
    python3 main.py update 1 "Updated Description"
    ```
### Delete
    ```sh  
    python3 main.py delete 1
    ```
### Mark In Progress
    ```sh  
    python3 main.py mark-in-progress 1
    ```
### Mark Done
    ```sh  
    python3 main.py mark-done 1
    ```    
## Project url
[roadmap.sh projects](https://roadmap.sh/projects/task-tracker)

## Contributing
If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature/new-feature).
3. Make your changes and commit them (git commit -am 'Add new feature').
4. Push the branch to your fork (git push origin feature/new-feature).
5. Open a new Pull Request.


## License
This project is licensed under the MIT License.