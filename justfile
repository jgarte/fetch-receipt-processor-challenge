alias b := build
alias r := run

build:
    docker build -t fetch-receipts .

run:
    docker run -d --name fetch-container -p 8080:8080 fetch-receipts
