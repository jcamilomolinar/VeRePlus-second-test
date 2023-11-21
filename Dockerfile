FROM node:18-alpine

WORKDIR /frontend

COPY package.json ./

RUN npm install

COPY . .

RUN npm run build

EXPOSE 9000

CMD ["npm", "run", "start"]

FROM python:latest

WORKDIR /backend

COPY . .

RUN pip install --upgrade pip setuptools
RUN pip install -r backend/requirements.txt

CMD ["python", "index.py"]