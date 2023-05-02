
# ModSecurity Deployment with Docker + Flask Website

This repository contains a Dockerfile and a sample configuration file to deploy [ModSecurity](https://modsecurity.org/) with [NGINX](https://nginx.org/) in a Docker container.

## Prerequisites

To use this repository, you will need:

-   [Docker](https://www.docker.com/) installed on your machine
-   Docker Compose
-   Basic understanding of Docker commands and usage

## Usage

To deploy ModSecurity with NGINX using this repository, follow these steps:

1.  Clone this repository to your local machine.
      `git clone https://github.com/nalonal/insidentil-waf-agent.git` 
    
2.  Navigate to the cloned directory in your terminal.
      `cd insidentil-waf-agent.git`
    
3.  Run the Docker Compose using the following command:
    
    Copy code
    
    `docker-compose up -d` 

    
## Configuration

The configuration file for ModSecurity is located at `/config/modsecurity.conf`. You can modify this file to customize the behavior of ModSecurity.

Additionally, you can modify the NGINX configuration by editing the file located at `/config/nginx/nginx.conf`.

## Credits

This repository is based on the work of [Nalonal](https://nalonal.com)