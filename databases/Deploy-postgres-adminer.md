# Deploying Postgres and Adminer Containers

Deploy a `PostSQL` database and a management front-end called `Adminer`, each in a `Docker` container:

1. Create a new working directory
1. Create a file called `docker-compose.yml`
1. Copy the following YAML into it, save and exit:

```yaml
version: "3.8"

services:
  db:
    image: docker.io/postgres:latest
    container_name: my-postgres
    ports:
      - "5432:5432"
    environment:
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql

  adminer:
    image: docker.io/adminer
    container_name: adminer
    restart: always
    ports:
      - 8080:8080

volumes:
  postgres_data:
```

4. From within the same working directory run `docker compose up -d`
5. Open your browser and navigate to `http://[YOUR_VM_IP:8080`
6. From the Adminer front page connect to your postgres database with the following credentials:

    - POSTGRES_HOST: "YOUR_VM_IP"
    - DB_PORT: "5432"
    - POSTGRES_USER: "postgres"
    - POSTGRES_DB: "postgres"
    - POSTGRES_PASSWORD: "mysecretpassword"

>You can input connection details manually through Adminer, but **DO NOT** hard code credentials into your code; Use an `.env` file - explained in main py-to-db tutorial.

**Troubleshooting:**

If the above deployment fails try creating a `.env` file in the same directory as your `docker-compose.yml`, add this line to it: `POSTGRES_PASSWORD=mysecretpassword`, save and close.

Then type:

```bash
sudo docker compose down -v
sudo docker compose up -d
```

- `-v`: Deletes any created volumes for the container.
