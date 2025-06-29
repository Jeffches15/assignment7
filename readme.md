# Module 7

## My GitHub Repository
![GitHub Repo](qr_codes/QRCode_20250629210121.png "My QR Code Link")

## My DockerHub Image

![Docker QR Image](/qr_codes/QRCode_20250629205811.png "My QR Code Link")

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