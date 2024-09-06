FROM node:20-slim as development-stage

# SET WORKING DIRECTORY
WORKDIR /app



COPY frontend/ ./

# Install ALL Dependencies
RUN npm install

EXPOSE 3000
