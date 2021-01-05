1. File `requirements.txt` contains dependencies for running the application.
2. Tests passed successfully:

   ![image](images/1.png)

3. Description of Makefile and its directives:
   - `STATES` and `REPO` - variables that contain tag names and the Docker Hub repository name;
   - `.PHONY` - a `make` utility that tells the file that the following targets are not files;
   - `$(STATES)` - target purpose build container;
   - `run` - target designation for creating network that will run the application; launch the application and repository `redis`;
   - `test-app` - target to run tests;
   - `docker-prune` - target to clean resources to be used in the operation of `Docker`.

4. All pages of site:

   ![image](images/2.png)
   
   ![image](images/3.png)
   
   ![image](images/4.png)

5. The project in this version of deployment has two networks: `secret` and` public`:
   - There are` app` and `redis` in the `secret` network. The latter does not have access to external resources;
   - The `public` network includes `app` and `tests`. `tests` and` redis` do not have access to each other.

6. The website launched at address `http:/127.0.0.1/`. 
7. Images have tags`compose-tests` and `compose-app`.
8. In my opinion, both `docker-compose.yaml` and `Makefile` have their own areas of use: `Makefile` is useful build tool, but it has more difficult implementation and can be difficult; `docker-compose` allows to define a multi-container structure in one file and works with it, using simple command.
