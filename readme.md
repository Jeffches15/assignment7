# Module 7

## My GitHub Repository
![GitHub Repo](qr_codes/QRCode_20250629210121.png "My QR Code Link")

## My DockerHub Image

![Docker QR Image](/qr_codes/QRCode_20250629205811.png "My QR Code Link")

## Screenshot of Container logs
![Container logs](/screenshots/screenshot%20of%20docker%20logs.png)

## Screenshot of GitHub Actions workflow
![GitHub Actions](/screenshots/screenshot%20of%20successful%20github%20actions.png)


# Reflection Document:
- Learning Docker is a fun and interesting experience so far. There are a few main takeaways and challenges that I have encountered with Dockerization.

## Key experiences:
- Even before doing any hands-on work, hearing the xbox analogy helped with understanding images and containers.
    - Xbox disc -> image/program
    - container -> xbox (run time environment that plays the image)
    - we get our images through Docker Hub (ex: GameStop)
- Generating the qr codes was pretty cool and a relatively simple process. The main.py code generates a qr code using the qrcode library, sets up logging, checks if the url for the qr code is valid, and creates a directory to store the qr codes if needed.
- Initially, my GitHub actions was failing whenever I pushed code due to there being no tests. I decided to add one simple test function to assure 100% coverage. In addition, I also had to add code to build and push an image to my .yml file to fulfill the requirement

## Challenges faced:
- The biggest challenge I faced (and still facing but not as often) is my Visual Studio Code "losing connection". Docker and WSL rely on one another, which is a benefit, but also has lead to connection problems. I would be coding per usual, then randomly my VSC would tell me to reconnect. When I click the reconnect button, the program would try to re-establish the connection, but never succeeding. I started to ask ChatGPT questions on how to solve this, and I was told to run a command: WSL --shutdown to "reboot WSL". I did this several times, but the problem would come back every time. Eventually, I created a .wslconfig file in my users directory on Windows. In this file, I wrote: [wsl2] memory=4GB processors=2. In simple terms, this file customizes the resource limits that WSL is permitted to use. Recently, I noticed that my Docker Desktop was not fully up to date either. I just updated this tool so hopefully this issue no longer occurs.
- The only other minor obstacle that I had to overcome was to learn new commands. I mentioned in the discussion post for module 7 that I have some experience with Docker, but not a lot. Docker has its own set of commands, some of which I knew, others I did not. I was not familiar with commands such as docker image, docker logs, docker stop, etc. After using them for this assignment, I feel more comfortable with Docker and the corresponding commands.



# Security Considerations in the Dockerfile:

## Non-Root User: The Dockerfile creates a non-root user (myuser) to run the application, enhancing security by minimizing potential damage from vulnerabilities.

## Ownership of Directories: Directories for logs and QR codes are created and owned by myuser, ensuring that only the non-root user can write to these directories.

## Minimal Base Image: Using a slim variant of Python reduces the attack surface by minimizing the number of installed packages.


# Explanation of Dockerfile Commands:

## FROM: Specifies the base image (python:3.12-slim-bullseye), which is lightweight and secure.
## WORKDIR: Sets the working directory inside the container to /app.
## COPY: Copies requirements.txt first to leverage Docker’s caching mechanism for dependencies.
## RUN: Installs Python dependencies, creates a non-root user, and sets up necessary directories with appropriate permissions.
## USER: Switches to the non-root user (myuser) to run the application.
## ENTRYPOINT and CMD: Defines the default command to run when the container starts, allowing for command-line argument overrides.