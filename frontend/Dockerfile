FROM node:20-alpine

WORKDIR /app

COPY package*.json ./

RUN npm ci --verbose

COPY . .

CMD ["npm", "run", "dev"]