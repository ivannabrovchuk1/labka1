- [Docker Hub Link](https://hub.docker.com/repository/docker/ivannabrovchuk1/lab4-examples)
- To download images:
    ```
    docker pull docker pull ivannabrovchuk1/lab4-examples:django
    docker pull docker pull ivannabrovchuk1/lab4-examples:monitoring
    ```
- To run containers:
    ```
    docker run -it --name=django --rm -p 8000:8000 ivannabrovchuk1/lab4-examples:django
    docker run -it --name=monitoring --rm --net=host -v $(pwd)/server.log:/app/server.log ivannabrovchuk1/lab4-examples:monitoring
    ```